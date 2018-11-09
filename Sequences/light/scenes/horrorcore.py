#encoding: utf-8
import sys
sys.path.append("../Controls/Mididings/")

from ports import *

def hc_notheft(seq, timer):
    seq.send('/pyta/text/position_y', 1, 200)

    seq.send(rpijardinport, '/pyta/text/visible', 1, 1)
    seq.send(rpicourport, '/pyta/text/visible', 1, 1)
    timer.wait(3, 's')
    seq.send('/pyta/text/strobe', 1, 1, 4, 0.5)
    seq.send(rpijardinport, '/pyta/text', 1, "Copying ain't no Theft"),
    seq.send(rpicourport, '/pyta/text', 1, "Copulefting ain't no Rape"),
    timer.wait(1, 's')
    seq.send('/pyta/text/strobe', 1, 0)
    timer.wait(2, 's')
    seq.send('/pyta/text/animate', 1, 'alpha', 1, 0, 4)
