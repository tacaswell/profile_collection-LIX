from ophyd import ( Component as Cpt, ADComponent,
                    EpicsSignal, EpicsSignalRO,
                    ROIPlugin, StatsPlugin, ImagePlugin,
                    SingleTrigger, PilatusDetector)

from ophyd.areadetector.filestore_mixins import FileStoreBulkWrite

from ophyd.utils import set_and_wait
from filestore.handlers_base import HandlerBase
import filestore.api as fs
import fabio
import os


def first_Pilatus():
    #print("checking first Pialtus")
    for det in gs.DETS:
        if det.__class__ == LIXPilatus:
            #print(det.name)
            return det.name
    return None


class PilatusFilePlugin(Device, FileStoreBulkWrite):
    file_path = ADComponent(EpicsSignalWithRBV, 'FilePath', string=True)
    file_number = ADComponent(EpicsSignalWithRBV, 'FileNumber')
    file_name = ADComponent(EpicsSignalWithRBV, 'FileName', string=True)
    file_template = ADComponent(EpicsSignalWithRBV, 'FileTemplate', string=True)
    reset_file_number = Cpt(Signal, name='reset_file_number', value=1)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._datum_kwargs_map = dict()  # store kwargs for each uid

    def stage(self):
        global proposal_id
        global run_id
        global current_sample
        global data_path
        global collection_lock_file

        set_and_wait(self.file_template, '%s%s_%6.6d_'+self.parent.detector_id+'.cbf', timeout=99999)
        if self.reset_file_number.get() == 1:
            set_and_wait(self.file_number, 1, timeout=99999)

        # original code by Hugo
        # this is done now when login()
        #path = '/GPFS/xf16id/exp_path/'
        #rpath = str(proposal_id)+"/"+str(run_id)+"/"
        #fpath = path + rpath
        #makedirs(fpath)
        
        # modified by LY
        # camserver saves data to the local ramdisk, a background process then move them to data_path
        # interesting to note that camserver saves the data to filename.tmp, then rename it filename after done writing
        # must have the '/' at the end, since camserver will add it to the RBV
        # this should done only once for all Pilatus detectors
        if self.parent.name == first_Pilatus():
            #print("first Pilatus is %s" % self.parent.name)
            change_path()
        
        #set_and_wait(self.file_path, "/ramdisk/", timeout=99999)
        set_and_wait(self.file_path, data_path, timeout=99999)
        set_and_wait(self.file_name, current_sample, timeout=99999)
        
        super().stage()
        res_kwargs = {'template': self.file_template.get(),
                      'filename': self.file_name.get(),
                      'frame_per_point': self.get_frames_per_point(),
                      'initial_number': self.file_number.get()}
        #self._resource = fs.insert_resource('AD_CBF', rpath, res_kwargs, root=path)
        self._resource = fs.insert_resource('AD_CBF', data_path, res_kwargs, root="/")
        
        if self.parent.name == first_Pilatus():
            caput("XF:16IDC-ES:Sol{ctrl}ready", 1)

    def unstage(self):        
        super().unstage()
        #if self.parent.name == first_Pilatus():
        #    release_lock()
        
    def get_frames_per_point(self):
        return 1

class PilatusCBFHandler(HandlerBase):
    specs = {'AD_CBF'} | HandlerBase.specs

    def __init__(self, rpath, template, filename, frame_per_point=1, initial_number=1):
        self._path = rpath
        self._fpp = frame_per_point
        self._template = template
        self._filename = filename
        self._initial_number = initial_number

    def __call__(self, point_number):
        start, stop = self._initial_number + point_number * self._fpp, (point_number + 2) * self._fpp
        ret = []
        # commented out by LY to test scan speed imperovement, 2017-01-24
        for j in range(start, stop):
            fn = self._template % (self._path, self._filename, j)
            #print("call Open File: ", fn)
            img = fabio.open(fn)
            ret.append(img.data)
        return np.array(ret).squeeze()

    def get_file_list(self, datum_kwargs_gen):
        file_list = []
        for dk in datum_kwargs_gen:
            point_number = dk['point_number']
            start, stop = self._initial_number + point_number * self._fpp, (point_number + 2) * self._fpp
            ret = []
            for j in range(start, stop):
                fn = self._template % (self._path, self._filename, j)
                #print("Will open file: ", fn)
                file_list.append(fn)
        return file_list



class LIXPilatus(SingleTrigger, PilatusDetector):
    file = Cpt(PilatusFilePlugin, suffix="cam1:",
               write_path_template="")

    roi1 = Cpt(ROIPlugin, 'ROI1:')
    roi2 = Cpt(ROIPlugin, 'ROI2:')
    roi3 = Cpt(ROIPlugin, 'ROI3:')
    roi4 = Cpt(ROIPlugin, 'ROI4:')

    stats1 = Cpt(StatsPlugin, 'Stats1:')
    stats2 = Cpt(StatsPlugin, 'Stats2:')
    stats3 = Cpt(StatsPlugin, 'Stats3:')
    stats4 = Cpt(StatsPlugin, 'Stats4:')

    def __init__(self, *args, **kwargs):
        self.detector_id = kwargs.pop('detector_id')
        super().__init__(*args, **kwargs)


def pilatus_number_reset(status):
    for det in pilatus_detectors:
        val = 1 if status else 0
        det.file.reset_file_number.put(val)

def pilatus_ct_time(exp):
    pil1M.cam.acquire_time.put(exp)
    pilW1.cam.acquire_time.put(exp)
    pilW2.cam.acquire_time.put(exp)

db.fs.register_handler('AD_CBF', PilatusCBFHandler)

pil1M = LIXPilatus("XF:16IDC-DT{Det:SAXS}", name="pil1M", detector_id="SAXS")
pilW1 = LIXPilatus("XF:16IDC-DT{Det:WAXS1}", name="pilW1", detector_id="WAXS1")
pilW2 = LIXPilatus("XF:16IDC-DT{Det:WAXS2}", name="pilW2", detector_id="WAXS2")

pilatus_detectors = [pil1M, pilW1, pilW2]

for det in pilatus_detectors:
   det.read_attrs = ['file']


