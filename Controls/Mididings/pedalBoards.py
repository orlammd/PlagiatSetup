# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from utils import OSCCustomInterface


config(
	backend='jack',
	client_name='PedalBoardsRoutes',
	out_ports=['PBseq24', 'PBAMSClassicalSynth', 'PBTapeutape', 'PBCtrlOut'],
	in_ports=['PBCtrlIn', 'PBMk2In']
)

from scenes import *

hook(
    OSCInterface(56422, 56423), # "osc.udp://CtrlOrl:56423"),
    OSCCustomInterface(56418),
    AutoRestart()
)

run(
    scenes = {
        1: SceneGroup("Climat", [
  		Scene("Bass ORL",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        climat,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        climat,
                        basspedal,
                        ]
		),
	    ]
        ),
        2: SceneGroup("ConnassesSACEM", [
  		Scene("Bass ORL",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        connassessacem,
                        basspedal,
                        ]
		),
	    ]
        ),
        3: SceneGroup("Fifty", [
  		Scene("Bass ORL",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        fifty,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        fifty,
                        basspedal,
                        ]
		),
	    ]
        ),
        4: SceneGroup("Le5", [
  		Scene("Bass ORL",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        le5,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        le5,
                        basspedal,
                        ]
		),
	    ]
        ),
        5: SceneGroup("SW", [
  		Scene("Bass ORL",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        sw,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        sw,
                        basspedal,
                        ]
		),
	    ]
        ),
        6: SceneGroup("Wholeworld", [
  		Scene("Bass ORL",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        wholeworld,
                        basspedal,
                        ]
		),
	    ]
        ),
        7: SceneGroup("Da Fist", [
  		Scene("Bass ORL",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        dafist,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        dafist,
                        basspedal,
                        ]
		),
	    ]
        ),
        8: SceneGroup("GetYourFreakOn", [
  		Scene("Bass ORL",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        geturfreakon,
                        basspedal,
                        ]
		),
	    ]
        ),
        9: SceneGroup("Horrorcore", [
  		Scene("Bass ORL",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        horrorcore,
                        basspedal,
                        ]
		),
	    ]
        ),
        10: SceneGroup("Trapone", [
  		Scene("Bass ORL",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Nope",
                      [
                        trapone,
                        basspedal,
                        ]
		),
		Scene("Tune Select",
                      [
                        trapone,
                        basspedal,
                        ]
		),
	    ]
        ),

    },
)
