from ophyd import Device, Component as Cpt, EpicsMotor, EpicsSignalRO

class XYMotor(Device):
	x = Cpt(EpicsMotor, '-Ax:X}Mtr')
	y = Cpt(EpicsMotor, '-Ax:Y}Mtr')

class XYZMotor(XYMotor):
	z = Cpt(EpicsMotor, '-Ax:Z}Mtr')

class XYPitchMotor(XYMotor):
	pitch = Cpt(EpicsMotor, '-Ax:P}Mtr')

class MonoDCM(Device):
	bragg = Cpt(EpicsMotor, '-Ax:Bragg}Mtr')
	x = Cpt(EpicsMotor, '-Ax:X}Mtr')
	y = Cpt(EpicsMotor, '-Ax:Of2}Mtr')
	pitch2 = Cpt(EpicsMotor, '-Ax:P2}Mtr')
	roll2 = Cpt(EpicsMotor, '-Ax:R2}Mtr')
	fine_pitch = Cpt(EpicsMotor, '-Ax:PF2}Mtr')
	ccm_fine_pitch = Cpt(EpicsMotor, '-Ax:CCM_PF}Mtr')
	pitch2_rb = Cpt(EpicsSignalRO, '-Ax:PF_RDBK}Mtr.RBV')

class KBMirrorHorizontal(Device):
	x1 = Cpt(EpicsMotor, '-Ax:XU}Mtr')
	x2 = Cpt(EpicsMotor, '-Ax:XD}Mtr')
	y1 = Cpt(EpicsMotor, '-Ax:YU}Mtr')
	y2 = Cpt(EpicsMotor, '-Ax:YD}Mtr')
	fine_pitch = Cpt(EpicsMotor, '-Ax:PF}Mtr')
	pitch_rb = Cpt(EpicsSignalRO, '-Ax:PF_RDBK}Mtr.RBV')

class KBMirrorVertical(Device):
	x = Cpt(EpicsMotor, '-Ax:X}Mtr')
	y1 = Cpt(EpicsMotor, '-Ax:YU}Mtr')
	y2 = Cpt(EpicsMotor, '-Ax:YD}Mtr')
	fine_pitch = Cpt(EpicsMotor, '-Ax:PF}Mtr')
	pitch_rb = Cpt(EpicsSignalRO, '-Ax:PF_RDBK}Mtr.RBV')

class Blades(Device):
    top = Cpt(EpicsMotor, '-Ax:T}Mtr')
    bottom = Cpt(EpicsMotor, '-Ax:B}Mtr')
    outboard = Cpt(EpicsMotor, '-Ax:O}Mtr')
    inboard = Cpt(EpicsMotor, '-Ax:I}Mtr')

class SlitsCenterAndGap(Device):
	x = Cpt(EpicsMotor, '-Ax:X}Mtr')
	dx = Cpt(EpicsMotor, '-Ax:dX}Mtr')
	y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
	dy = Cpt(EpicsMotor, '-Ax:dY}Mtr')

class HRM1(Device):
	y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
	pitch = Cpt(EpicsMotor, '-Ax:Th}Mtr')

class HRM2(Device):
	y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
	pitch = Cpt(EpicsMotor, '-Ax:Th}Mtr')
	# Upstream
	bend1 = Cpt(EpicsMotor, '-Ax:BU}Mtr')
	# Downstream
	bend2 = Cpt(EpicsMotor, '-Ax:BD}Mtr')

class StageScan(Device):
	x = Cpt(EpicsMotor, '-Ax:X}Mtr')
	y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
	r = Cpt(EpicsMotor, '-Ax:Rot}Mtr')

class Microscope(Device):
	x = Cpt(EpicsMotor, '-Ax:X}Mtr')
	y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
	focus = Cpt(EpicsMotor, '-Ax:F}Mtr')
	polarizer = Cpt(EpicsMotor, '-Ax:Pol}Mtr')
	zoom = Cpt(EpicsMotor, '-Ax:Zm}Mtr')

class WAXSBeamstop(XYMotor):
	phi = Cpt(EpicsMotor, '-Ax:Z}Mtr')

class SAXSBeamstop(XYMotor):
	r1 = Cpt(EpicsMotor, '-Ax:R1}Mtr')
	r2 = Cpt(EpicsMotor, '-Ax:R2}Mtr')
	r3 = Cpt(EpicsMotor, '-Ax:R3}Mtr')
	tilt1 = Cpt(EpicsMotor, '-Ax:T1}Mtr')
	tilt2 = Cpt(EpicsMotor, '-Ax:T2}Mtr')
    
class SolutionScatteringEnclosure(Device):
    y = Cpt(EpicsMotor, '-Ax:Y}Mtr')
    yu = Cpt(EpicsMotor, '-Ax:YU}Mtr')
    # xu: upper horizontal stage
    # xl: lower horizontal stage

class ScanningStack1(Device):
    x = Cpt(EpicsMotor, 'Ax:X}Mtr')
    y = Cpt(EpicsMotor, 'Ax:Y}Mtr')


class ScanningStack2(Device):
    x = Cpt(EpicsMotor, '{Ax:X}Mtr')
    y = Cpt(EpicsMotor, '{Ax:Y}Mtr')
    rx = Cpt(EpicsMotor, '{Ax:RX}Mtr')
    ry = Cpt(EpicsMotor, '{Ax:RY}Mtr')    

class WAXS1(Device):
    x=Cpt(EpicsMotor, 'Ax:X}Mtr')
    y=Cpt(EpicsMotor, 'Ax:Y}Mtr')
    z=Cpt(EpicsMotor, 'Ax:Z}Mtr')      
          
class WAXS2(Device):
    x=Cpt(EpicsMotor, 'Ax:X}Mtr')
    y=Cpt(EpicsMotor, 'Ax:Y}Mtr')
    z=Cpt(EpicsMotor, 'Ax:Z}Mtr')      
   
#######################################################
### LIX First Optical Enclosure FOE Optics Hutch A
#######################################################

## White Beam Mirror
wbm = XYPitchMotor('XF:16IDA-OP{Mir:WBM', name='wbm')

## Si(111) Mono DCM
mono = MonoDCM("XF:16IDA-OP{Mono:DCM", name="dcm")

## Beam-viewing screen #3
scn3y = EpicsMotor('XF:16IDA-BI{FS:3-Ax:Y}Mtr', name='scn3y')

## Beam-viewing screen #4
scn4y = EpicsMotor('XF:16IDA-BI{FS:4-Ax:Y}Mtr', name='scn4y')

## KB Mirror System
# Horizontal
hfm = KBMirrorHorizontal('XF:16IDA-OP{Mir:KBH', name="hfm")
# Vertical
vfm = KBMirrorVertical('XF:16IDA-OP{Mir:KBV', name='vfm')

## Slits
mps = Blades('XF:16IDA-OP{Slt:1', name='mps')


#######################################################
### LIX Secondary Source Enclosure SOE Hutch B
#######################################################

## Beam Position Monitor
bpm_pos = XYMotor('XF:16IDB-BI{BPM:1', name='bpm_pos')

bpm2 = EpicsMotor('XF:16IDC-BI{BPM:2-Ax:Y}Mtr', name='bpm2')

## Secondary Source Aperture (SSA)
ssa = XYMotor('XF:16IDB-OP{Slt:SSA-', name='ssa')


## Attenuator
# Absorber Set #1
atn1x = EpicsMotor('XF:16IDB-OP{Fltr:Atn-Ax:X1}Mtr', name='atn1x')
# Absorber Set #2
atn2x = EpicsMotor('XF:16IDB-OP{Fltr:Atn-Ax:X2}Mtr', name='atn2x')
# Absorber Set #3
atn3x = EpicsMotor('XF:16IDB-OP{Fltr:Atn-Ax:X3}Mtr', name='atn3x')

## Alternative SSA
assa = SlitsCenterAndGap('XF:16IDB-OP{Slt:aSSA', name="aSSA")

## Visual Beam Monitor (VBM)
# Focus
vbm_focus = EpicsMotor('XF:16IDB-BI{FS:VBM-Ax:F}Mtr', name='vbm_focus')
# Zoom
vbm_zoom = EpicsMotor('XF:16IDB-BI{FS:VBM-Ax:Zm}Mtr', name='vbm_zoom')


#######################################################
### LIX Experimental End Station Enclosure EESE Hutch C
#######################################################

## Harmonic Rejection Mirror HRM1
hrm1 = HRM1('XF:16IDC-OP{Mir:HRM1', name='hrm1')

## Harmonic Rejection Mirror HRM2
hrm2 = HRM2('XF:16IDC-OP{Mir:HRM2', name='hrm2')

## Divergence Defining Aperture (DDA)
dda = SlitsCenterAndGap('XF:16IDC-OP{Slt:DDA', name='dda')

## Beam Position Monitor (BPM)
bimy = EpicsMotor('XF:16IDC-BI{BPM:2-Ax:Y}Mtr', name='bimy')

## Guard Slits 1
sg1 = SlitsCenterAndGap('XF:16IDC-OP{Slt:G1', name='sg1')

## Guard Slits 2
sg2 = SlitsCenterAndGap('XF:16IDC-OP{Slt:G2', name='sg2')

#########################################
## In-air transmission measurement module
#########################################

## Coarse-resolution scanning
smc = XYMotor('XF:16IDC-ES:InAir{Stg:ScanC', name='smc')

## Fine-resolution scanning
smf = StageScan('XF:16IDC-ES:InAir{Stg:ScanF', name='smf')

## Microscope
microscope = Microscope('XF:16IDC-ES:InAir{Mscp:1', name='microscope')

#########################################
## Scanning Stack 1--Coarse Stage
#########################################
ss1 = ScanningStack1('XF:16IDC-ES:InAir{Stg:ScanC-', name='ss1')


#########################################
## Scanning probe stack with Newport stages 
#########################################
ss2 = ScanningStack2('XF:16IDC-ES:Scan2', name='ss2')

#########################################
## Solution scattering 
#########################################

sol_en = SolutionScatteringEnclosure('XF:16IDC-ES:Sol{Enc', name='sol_en')

# test ss2.rx

#ss2.rx=EpicsMotor('XF:16IDC-ES:Scan2{Ax:RX}Mtr', name='ss2.rx')

# SolHdl
        
#########################################
## In-vaccum GISAXS/GID module
#########################################

## Guard Slits 2 in VAC
# TODO: Review this motor
#sg2dx = EpicsMotor('XF:16IDC-ES:GI{Slt:G2-Ax:X}Mtr', name='sg2dx')
#sg2dy = EpicsMotor('XF:16IDC-ES:GI{Slt:G2-Ax:dX}Mtr', name='sg2dy')


#########################################
## Detector System
#########################################

## WAXS Detector Positioning Stage 1
waxs1 = XYZMotor('XF:16IDC-ES{Stg:WAXS1', name='waxs1')

## WAXS Detector Positioning Stage 2
waxs2 = XYZMotor('XF:16IDC-ES{Stg:WAXS2', name='waxs2')

## WAXS Beamstop
wbs = WAXSBeamstop('XF:16IDC-ES{BS:WAXS', name='wbs')

## SAXS Detector Positioning Stage
saxs = XYZMotor('XF:16IDC-ES{Stg:SAXS', name='saxs')

## WAXS Detector Positioning Stage
waxs1 = WAXS1('XF:16IDC-ES{Stg:WAXS1-', name='waxs1')
waxs2 = WAXS2('XF:16IDC-ES{Stg:WAXS2-', name='waxs2')

## SAXS Beamstop
sbs = SAXSBeamstop('XF:16IDC-ES{BS:SAXS', name='sbs')

## shutter # TODO: Check with Shirish and Lin and remove it
#shutter = EpicsMotor('XF:16ID-TS{EVR:C1-Out:FP0}Src:Scale-SP', name='shutter')

focus = EpicsMotor('XF:16IDC-ES:InAir{Mscp:1-Ax:F}Mtr', name='focus')
sh=EpicsMotor('XF:16IDC-ES:Sol{Enc-Ax:XL}Mtr', name='hand_low_encl')
#SolExU=EpicsMotor('XF:16IDC-ES:Sol{Enc-Ax:XU}Mtr', name='Sol_Up_encl')
