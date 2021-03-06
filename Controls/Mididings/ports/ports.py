#encoding: utf-8

from mididings import *

## OSC

klickport = 1234
slport = 9951
testport = 1111

# Non Mixers

vxorlpreport = 6666
vxorlmeufport = 6667
vxorlpostport = 6668
vxmainport = 6669
vxorlgarsport = 6670

vxjeannotpreport = 6671
vxjeannotmeufport = 6672
vxjeannotgarsport = 6673
vxjeannotpostport = 6674


samplespitchport = 7000
samplesdelaymungeport = 7001
samplesreversedelayport = 7002
samplesringmodport = 7003
samplestremoloport = 7005
samplesscapeport = 7006
samplesdisintegratorport = 7007
samplesmainport = 7008
samplesdegradeport = 7009

keyboardsport = 7010

bassmainport = 7020
monitorsorlport = 7030
monitorsjeannotport = 7031

vocoderjeannotport = 7050
vocoderjeannotportgars = 7051
vocoderjeannotportmeuf = 7052

vocoderorlport = 7060
vocoderorlportgars = 7061
vocoderorlportmeuf = 7062


## Vx pitchshiter
vxpitchshifterport  = 7040



## OSC Sequencers

trapcutport = 8001
audioseqport = 8002
lightseqport = 8003

## Zynadd

zyntrebleport = 10000
zynbassport = 10001

## CME keyboard programs

cmeinport = 56424
cmeoutport = 56425

## Mk2 keyboard programs

mk2inport = 56426
mk2outport = 56427

## Mono Synth Microtonal Pitcher

monosynthpitcherport = 56428

## Control Surfaces

surfaceorlport = 11000
surfaceorltomidiport = 11001

## QLC

qlcappport = 12000
qlcport = 12001 # delayed messages -> le port sur lequel écrire
qlcstopport = 12001 # stop (all off)

## pyta
rpijardinport = 'osc.udp://127.0.0.1:5555'
rpicourport = 'osc.udp://127.0.0.1:5556'
vporlport = 'osc.udp://192.168.0.102:56418'
vpjeannotport = 'osc.udp://192.168.0.103:56418'

## misc
gxtunermanagerport = 13000

## BCR

bcrinport = 12345
bcroutport = 12346

## MIDI

seq24 = None
seq24once = None
tapeutape = None
tapeutapecontrol = None

try:

    seq24=Output('PBseq24',1)
    seq24once=Output('PBseq24',2)

    tapeutape=Output('PBTapeutape',10)
    tapeutapecontrol=Output('PBTapeutape',1)

except:

    pass
