# coding=utf8
from mididings import *
from mididings.extra.osc import OSCInterface
from mididings.extra.inotify import AutoRestart
from mididings.extra.osc import SendOSC
from customosc import OSCCustomInterface

import liblo


config(
	backend='jack',
	client_name='PedalBoardsRoutes',
	out_ports=['PBseq24', 'PBAMSClassicalSynth', 'PBTapeutape', 'PBCtrlOut'],
	in_ports=['PBCtrlIn']
)

hook(
    OSCInterface(56422, 56423), # "osc.udp://CtrlOrl:56423"),
    OSCCustomInterface(56418),
    AutoRestart()
)


#### Ports OSC ################################################

klickport = 1234
slport = 9951
# testport = 1111
# qlcport = ("192.168.0.13", 7772)
# qlcstopport = ("192.168.0.13", 7771)
# #qlcport = 7777
# videoCport = ("192.168.0.31", 56418)
# videoCseqport = 12346
# videoJport = ("192.168.0.30", 56418)
# videoJseqport = 12347
# videoKport = ("192.168.0.32", 56418)
# videoKseqport = 12348
# qlcseqport = 12345 #("CtrlRegie", 12345)
# #videoseqport = ("CtrlDag", 12346)
# audioseqport=12344
# mainseqport = ("CtrlDag", 12343)
# desktoporlport = ("CtrlOrl", 12345)

# Non Mixers
# mainmixport = 6666
# drumsport = 6667
# bassesport = 6668
# guitarsport = 6669
# mxsynthport = 6670
# mxdrumsport = 6671
# vocalsport = 6672
# tomsport = 6673
# acousticsport = 6674
# mondagport = 6675
# monjeport = 6676
# monorlport = 6677
# mainsport = 6678



#### Outputs ################################################
seq24=Output('PBseq24',1)
seq24once=Output('PBseq24',2)

tapeutape=Output('PBTapeutape',10)


#### Functions #############################################
#### Trigger seq24 ####
p_firstpart=[range(1,65)]
p_secondpart=[range(65,129)]

note2seq = ProgramFilter(p_firstpart) >> seq24 # mute-groups seq24
note2seqNplay = ProgramFilter(p_secondpart) >> [ # mute-groups + play
			NoteOn(EVENT_PROGRAM,127) >> Transpose(-62) >> Program('PBseq24',1,EVENT_NOTE) >> seq24,
			Program('PBseq24',1,1),
		]


seq24start = Program('PBseq24',1,1)

seqtrigger = Filter(PROGRAM) >> [
		ChannelFilter(1) >> [ 
             		note2seq,
			note2seqNplay,
		],
		ChannelFilter(2) >> [
			seq24once,
		]
	]

cseqtrigger = Channel(1) >> seqtrigger

#### Bass ####

#### Vocals ####

#### Stop ####
stop = [
        Program(2) >> cseqtrigger,
        SendOSC(slport, '/sl/-1/hit', 'pause_on') >> Discard(),
        SendOSC(klickport, '/klick/metro/stop') >> Discard(),

        # [
        #     SendOSC(qlcstopport, '/AllStop', 1),
        #     SendOSC(qlcseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoCseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoCport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(videoJseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoJport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(videoKseqport, '/Sequencer/DisableAll', 1),
        #     SendOSC(videoKport, '/pyta/slide/visible', -1, 0),
        #     SendOSC(audioseqport, '/Sequencer/DisableAll', 1),
        #     ] >> Discard()
]

#### FX Pedals #############################################
# ORL

#### Scenes ################################################

#### Climat ####
climat = PortFilter('PBCtrlIn') >> [
    ProgramFilter(1) >> stop, # !!!STOP!!! #
    ProgramFilter(2) >> [
        Program(65) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 74),
            SendOSC(slport, '/set', 'tempo', 150),

            SendOSC(klickport, '/klick/simple/set_tempo', 150),
            SendOSC(klickport, '/klick/simple/set_meter', 74, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x.x.xX.x.x.x.X.x.x.x.X.x.x.x.X.x.x.x.X.x'),
            SendOSC(klickport, '/klick/metro/start'),
            ] >> Discard()
        ],
    ]


#### RUN ###################################################

run(
    scenes = {
        1: SceneGroup("Climat", [
  		Scene("Bass ORL",
                      [
                        climat,
                        ]
		),
		Scene("Guitar ORL",
                      [
                        climat,
                        ]
		),
	    ]
        ),
        # 2: SceneGroup("", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte1,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte1,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte1,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte1,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte1,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte1,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte1
	# 	),
	# 	Scene("Bank Select",
        #               acte1
	# 	),
	# 	Scene("Tune Select",
        #               acte1
	# 	)
	#     ]
        # ),
        # 3: SceneGroup("Acte II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte2,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte2,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte2,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte2,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte2,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte2,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte2
	# 	),
	# 	Scene("Bank Select",
        #               acte2
	# 	),
	# 	Scene("Tune Select",
        #               acte2
	# 	)
	#     ]
        # ),
        # 4: SceneGroup("Forain Acte II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 forainacte2,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 forainacte2,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 forainacte2,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 forainacte2,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 forainacte2,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 forainacte2,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               forainacte2
	# 	),
	# 	Scene("Bank Select",
        #               forainacte2
	# 	),
	# 	Scene("Tune Select",
        #               forainacte2
	# 	)
	#     ]
        # ),
        # 5: SceneGroup("Acte III", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3
        #               ),
	# 	Scene("Bank Select",
        #               acte3
        #               ),
	# 	Scene("Tune Select",
        #               acte3
	# 	)
	#     ]
        # ),
        # 6: SceneGroup("Acte III Part II", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3partII,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3partII,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3partII,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3partII,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3partII,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3partII,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3partII
	# 	),
	# 	Scene("Bank Select",
        #               acte3partII
	# 	),
	# 	Scene("Tune Select",
        #               acte3partII
	# 	)
	#     ]
        # ),
        # 7: SceneGroup("Acte III Part III", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte3partIII,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte3partIII,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte3partIII,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte3partIII,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte3partIII,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte3partIII,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
        #               acte3partIII,
	# 	),
	# 	Scene("Bank Select",
        #               acte3partIII
	# 	),
	# 	Scene("Tune Select",
        #               acte3partIII
	# 	)
	#     ]
        # ),
        # 8: SceneGroup("Acte IV", [
  	# 	Scene("Bass ORL",
        #               [
        #                 acte4,
        #                 orl_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar ORL",
        #               [
        #                 acte4,
        #                 orl_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix ORL",
        #               [
        #                 acte4,
        #                 orl_vxpedal
        #                 ]
	#         ),
	# 	Scene("Bass Dag",
        #               [
        #                 acte4,
        #                 dag_basspedal
        #                 ]
	# 	),
	# 	Scene("Guitar Dag",
        #               [
        #                 acte4,
        #                 dag_gtrpedal
        #                 ]
	# 	),
	# 	Scene("Voix Dag",
        #               [
        #                 acte4,
        #                 dag_vxpedal
        #                 ]
	# 	),
	# 	Scene("Boucles",
	# 	    acte4
	# 	),
	# 	Scene("Bank Select",
	# 	    acte4
	# 	),
	# 	Scene("Tune Select",
	# 	    acte4
	# 	)
	#     ]
        # ),

    },
)

