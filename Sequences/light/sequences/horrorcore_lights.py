#encoding: utf-8

import sys
sys.path.append("../Controls/Mididings/")

from ports import *

# aliases généraux
whiteC_Play = [":/Lightseq/Scene/Play", "horrorcore_couplet_crepitement"]
whiteC_Stop = [":/Lightseq/Scene/Play", "horrorcore_couplet_crepitement_stop"]



horrorcore_couplet_blinkBass = [
    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), (None, None, whiteC_Play), whiteC_Stop,
    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), None, None,

    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), (None, None, whiteC_Play), whiteC_Stop,
    None, None, None, whiteC_Play,
    None, (None, whiteC_Stop), None, ([qlcport, '/TuttiLointain/Red/Segment/All', 89], [qlcport, '/TuttiLointain/Red/Segment/All', 0], None, None, None, None, None, None)
]


rougeOn1 = [qlcport, '/TuttiProche/Red/Segment/[3-5]', 255]
rougeOff1 = [qlcport, '/TuttiProche/Red/Segment/[3-5]', 0]
rougeOn2 = [qlcport, '/TuttiProche/Red/Segment/[6-8]', 255]
rougeOff2 = [qlcport, '/TuttiProche/Red/Segment/[6-8]', 0]
whiteOn = [qlcport, '/Tutti/White/Segment/All', 255]
whiteOff = [qlcport, '/Tutti/White/Segment/All', 0]
horrorcore_ragga = [
   ([rougeOn1], [rougeOff1], None, [rougeOn2]), ([rougeOff2], None, whiteOn, whiteOff),
   ([rougeOn1], [rougeOff1], None, [rougeOn2]), ([rougeOff2], None, whiteOn, whiteOff),
   (whiteOn, whiteOff), (whiteOn, whiteOff), (whiteOn, whiteOff), None
]

greenOnOrl=[qlcport, '/ProcheJardin/Green/Segment/[6-8]', 255]
greenOnJeannot=[qlcport, '/ProcheCour/Green/Segment/[6-8]', 255]
greenOnBoth=[qlcport, '/TuttiProche/Green/Segment/[1-3]', 255]
greenOff=[qlcport, '/{ProcheJardin,ProcheCour}/Green/Segment/{1,2,3,6,7,8}', 0]
redOff=[qlcport,  '/Stop']
horrorcore_meshuragga = [
    (greenOnJeannot,None,greenOnOrl), (None,greenOnBoth,None),
    (greenOff, [':/Lightseq/Scene/Play', 'horrorcore_mooncup_maison'], None, None), None,
    [[':/Lightseq/Scene/Stop', 'horrorcore_mooncup_maison'], redOff], (None, [':/Lightseq/Scene/Play', 'horrorcore_mooncup_maison'], None, None),
    [[':/Lightseq/Scene/Stop', 'horrorcore_mooncup_maison'], redOff], None
]
