#encoding: utf-8

from ports import *
from aliases import *

from mididings import *
from mididings.extra.osc import SendOSC

#######################################

le5_mk2lights = {
    1:'blue',
    2:'purple',
    3:'purple',
    4:'purple',
    5:'white',
    6:'white',
    7:'white',
    8:'red',
}

coffee_redseas = " ".join(["Coffee_" + str(i) for i in range(1,11)])
coffee_redseas+=" Dunes_1"
coffee_redseas+=" Rock_1"
coffee_redseas+=" Moon_1"
coffee_redseas+=" Moon_2"
coffee_redseas+=" Mars_1"
coffee_redseas+=" Mars_2"
coffee_redseas+=" Mountains_1"
coffee_redseas+=" Mountains_2"


twerks = " ".join(['Twerk_'+str(i) for i in range(1,33)])

#### Le5 ####
le5 = [
    Init([
        Program(seq24PageMap[5]) >> seq24once,
        Ctrl(0, 3) >> tapeutapecontrol,

        enable_microtonal,
        set_microtonal(0, 0.35, 0, 0.35, 0, 0, 0, 0, 0.35, 0, 0, 0),
        # zynmicrotonal_on,
        # SendOSC(zyntrebleport, '/microtonal/tunings', '100.0\n200.0\n300.0\n435.0\n500.0\n635.0\n700.0\n800.0\n900.0\n1000.0\n1135.0\n2/1'),

        SendOSC(mk2inport, '/mididings/switch_scene', 1),
        mk2lights(le5_mk2lights),
        ]),
    [orl, jeannot] >> ProgramFilter(1) >> stop, # !!!STOP!!! #
    jeannot_padrelease >> mk2lights(le5_mk2lights),
    [orl, jeannot] >> ProgramFilter([range(1,12)]) >> [
        SendOSC(audioseqport, '/Audioseq/Sequence/Disable', '*'),
        SendOSC(samplesmainport, '/strip/SamplesMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxJeannotMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(vxmainport, '/strip/VxORLMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(bassmainport, '/strip/BassMain/AM%20pitchshifter/Pitch%20shift/unscaled', 1.),
        SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',20000.),

    ] >> Discard(),
    orl >> ProgramFilter([range(2,12)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter([range(2,8)]) >> light_reset >> Discard(),
    jeannot >> ProgramFilter(2) >> [ # Intro Shut your dickhole + break fitting me suit - Bouton 2
        Program(65) >> cseqtrigger,
        NoteOn(66,127) >> Output('PBTapeutape', 3), # gunshot
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),
            SendOSC(slport, '/sl/-1/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(2) >> [ # Couplet A - Bouton 2
        Program(66) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(3) >> [ # Couplet B - Bouton 3
        Program(67) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(rpijardinport, '/pyta/slide/alpha', coffee_redseas, 0.2),
            SendOSC(rpicourport, '/pyta/slide/alpha', coffee_redseas, 0.2),
            SendOSC(rpijardinport, '/pyta/slide/scale', coffee_redseas, 800, 600, 1),
            SendOSC(rpicourport, '/pyta/slide/scale', coffee_redseas, 800, 600, 1),
            SendOSC(lightseqport, '/Lightseq/Bpm', 160),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(4) >> [ # Couplet C - Bouton 4
        Program(68) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(rpijardinport, '/pyta/slide/animate', coffee_redseas, 'alpha', 0.3, 0.9, 2),
            SendOSC(rpicourport, '/pyta/slide/animate', coffee_redseas, 'alpha', 0.3, 0.9, 2),
            SendOSC(rpijardinport, '/pyta/slide/rgb', coffee_redseas, 1, 0, 0),
            SendOSC(rpicourport, '/pyta/slide/rgb', coffee_redseas, 1, 0, 0),
            SendOSC(lightseqport, '/Lightseq/Bpm', 160),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    jeannot >> ProgramFilter(3) >> [ # Refrain (meeeaaan) - Bouton 3
        Program(69) >> cseqtrigger,
        [
            SendOSC(audioseqport, '/Audioseq/Bpm', 320),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'le5_refrain_cutdown'),

            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(rpijardinport, '/pyta/text/strobe', 0, 1, 4, 0.5),
            SendOSC(rpicourport, '/pyta/text/strobe', 0, 1, 4, 0.5),
            SendOSC(rpijardinport, '/pyta/text/size', 0, 0.8),
            SendOSC(rpicourport, '/pyta/text/size', 0, 0.8),
            SendOSC(lightseqport, '/Lightseq/Bpm', 320),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_refrain'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_on,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_on,

            bassscape,
            bassdegrade,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(5) >> [ # Couplet A (niggah don't you know) - Bouton 6
        Program(70) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(rpijardinport, '/pyta/text/size', 2, 0.06),
            SendOSC(rpicourport, '/pyta/text/size', 2, 0.06),
            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_niggahdontyou'),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    jeannot >> ProgramFilter(4) >> [ # Couplet Bbis (call your jesus) - Bouton 4
        Program(71) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 80),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(trapcutport, '/Trapcut/Bpm', 320),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(rpijardinport, '/pyta/slide/alpha', coffee_redseas, 0.2),
            SendOSC(rpicourport, '/pyta/slide/alpha', coffee_redseas, 0.2),
            SendOSC(lightseqport, '/Lightseq/Bpm', 160),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),


            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],
    orl >> ProgramFilter(6) >> [ # Couplet Cbis (ain't no challenger left)- Bouton 6
        Program(72) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 160),

            SendOSC(klickport, '/klick/simple/set_tempo', 160),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(160)),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(160)),
            SendOSC(samplesscapeport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(160)),


            SendOSC(rpijardinport, '/pyta/slide/animate', coffee_redseas, 'alpha', 0.3, 0.9, 2),
            SendOSC(rpicourport, '/pyta/slide/animate', coffee_redseas, 'alpha', 0.3, 0.9, 2),
            SendOSC(rpijardinport, '/pyta/slide/rgb', coffee_redseas, 1, 0, 0),
            SendOSC(rpicourport, '/pyta/slide/rgb', coffee_redseas, 1, 0, 0),
            SendOSC(rpijardinport, '/pyta/slide/scale', coffee_redseas, 800, 600, 1),
            SendOSC(rpicourport, '/pyta/slide/scale', coffee_redseas, 800, 600, 1),
            # SendOSC(rpijardinport, '/pyta/slide/animate', coffee_redseas, 'zoom', 1, 1, 12),
            # SendOSC(rpicourport, '/pyta/slide/animate', coffee_redseas, 'zoom', 1, 2, 12),

            SendOSC(lightseqport, '/Lightseq/Bpm', 160),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_coffee_redsea_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_coffee_redsea_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_off,
            vxjeannotmeuf_on,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
        ],

    orl >> ProgramFilter(7) >> [ # Cloud rap ballade rhodes - Bouton 7
        stop,
        Program(73) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 60),

            SendOSC(klickport, '/klick/simple/set_tempo', 60),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 8),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),
            SendOSC(cmeinport, '/mididings/switch_scene', 10),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(60)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(60)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(60)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(60)),

            SendOSC(monitorsjeannotport, '/strip/Klick/Gain/Mute', 1.0),

            SendOSC(rpijardinport, '/pyta/slide/animate', 'stars1', 'scale_x', 0, 800, 300),
            SendOSC(rpicourport, '/pyta/slide/animate', 'stars2', 'scale_x', 0, 800, 300),
            SendOSC(rpijardinport, '/pyta/slide/visible', 'stars1', 1),
            SendOSC(rpicourport, '/pyta/slide/visible', 'stars2', 1),
            SendOSC(rpijardinport, '/pyta/text', 2, 'cute is obvious'),
            SendOSC(rpijardinport, '/pyta/text/align', 2, 'top', 'left'),
            SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
            SendOSC(rpicourport, '/pyta/text', 2, 'cute is obvious'),
            SendOSC(rpicourport, '/pyta/text/align', 2, 'top', 'right'),
            SendOSC(rpicourport, '/pyta/text/visible', 2, 1),

            ] >> Discard(),
        [

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotgars_off,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotdelay_off,
            vxjeannotvocode_on,

            ] >> Discard()
        ],
    orl >> ProgramFilter(8) >> [ # Bouclage rhodes  - Bouton 8
            SendOSC(slport, '/sl/8/hit', 'record'),
        ],
    jeannot >> ProgramFilter(5) >> [ # gros ragga (coupure cloud rap let's party) - bouton 5
        Program(75) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(slport, '/sl/8/hit', 'pause_on'),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),


		#TODO Positionnement
	    SendOSC(rpijardinport, '/pyta/text', 2, 'nAfr0-tRap'),
	    SendOSC(rpicourport, '/pyta/text', 1, 'NYMPH0 TRAP'),
	    SendOSC(rpijardinport, '/pyta/text/visible', 2, 1),
	    SendOSC(rpijardinport, '/pyta/text/strobe', 2, 1, 12, 0.5),
	    SendOSC(rpijardinport, '/pyta/text/alpha', 2, 0.5),
	    SendOSC(rpicourport, '/pyta/text/visible', 1, 1),
	    SendOSC(rpicourport, '/pyta/text/strobe', 1, 1, 11, 0.5),
	    SendOSC(rpijardinport, '/pyta/text/alpha', 1, 0.5),

	    SendOSC(lightseqport, '/Lightseq/Bpm', 125),
	    SendOSC(lightseqport, '/Lightseq/Sequence/Enable', 'le5_nymphotrap_blow'),
	    SendOSC(rpijardinport, '/pyta/slide/alpha', twerks, 0.15),
	    SendOSC(rpicourport, '/pyta/slide/alpha', twerks, 0.15),
	    SendOSC(lightseqport, '/Lightseq/Play', timestamp),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_on,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxjeannotvocode_off,

            bassdry,
            basswobble,

            ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_off,
            bassbufferst_off,
            ]
    ],
    orl >> ProgramFilter(9) >> [ # Instouboul sans batterie - Bouton 9
        Program(76) >> cseqtrigger,
        [
            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(bassmainport, '/strip/BassScapePost/' + scapebpmpath, scapebpm(120)),
            SendOSC(samplesscapeport, '/strip/SamplesScape/' + scapebpmpath, scapebpm(120)),
            SendOSC(vxorlpostport, '/strip/VxORLDelayPost/' + delaybpmpath, delaybpm(120)),
            SendOSC(vxjeannotpostport, '/strip/VxJeannotDelayPost/' + delaybpmpath, delaybpm(120)),

            SendOSC(lightseqport, '/Lightseq/Bpm', 120),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),
            SendOSC(rpijardinport, '/pyta/text', 0, "Instouboul"),
            SendOSC(rpicourport, '/pyta/text', 0, "Instouboul"),
            SendOSC(rpijardinport, '/pyta/text/align', 0, 'top', 'left'),
            SendOSC(rpicourport, '/pyta/text/align', 0, 'top', 'right'),
            SendOSC(rpijardinport, '/pyta/text/animate', 0, 'size', 0, 1, 300),
            SendOSC(rpicourport, '/pyta/text/animate', 0, 'size', 0, 1, 300),
            SendOSC(rpijardinport, '/pyta/text/animate', 0, 'alpha', 0.1, 1, 300),
            SendOSC(rpicourport, '/pyta/text/animate', 0, 'alpha', 0.1, 1, 300),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpicourport, '/pyta/text/visible', 0, 1),

            vxorlgars_on,
            vxorlmeuf_off,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            vxjeannotdelay_off,
            vxjeannotgars_on,
            vxjeannotmeuf_off,
            vxjeannotdisint_off,
            vxorlvocode_off,

            SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',200.),


            SendOscState([

                [samplesmainport, '/strip/Samples1Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples2Dry/Gain/Mute', 0.0],
                [samplesmainport, '/strip/Samples3Dry/Gain/Mute', 0.0],

            ]),
        ] >> Discard(),
        [
            bassdetunest_on,
            bassringst_on,
            bassvibest_on,
            bassbufferst_on,
            ]
        ],
    orl >> ProgramFilter(10) >> [ # Instouboul bouclage voix + bass - Bouton 10
        [

            SendOSC(samplesmainport, '/strip/SamplesMain/Calf%20Filter/Frequency/unscaled',200.),

            SendOSC(slport, '/sl/0/hit', 'record'), # bass pre
            SendOSC(slport, '/sl/2/hit', 'record'), # vxorl pre
            SendOSC(slport, '/sl/4/hit', 'record'), # vxjeannot pre

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(6) >> [ # Instouboul entrée batterie meshuggah - bouton 7
        Program(77) >> cseqtrigger,
        [

            SendOSC(slport, '/set', 'eighth_per_cycle', 5),
            SendOSC(slport, '/set', 'tempo', 120),

            SendOSC(klickport, '/klick/simple/set_tempo', 120),
            SendOSC(klickport, '/klick/simple/set_meter', 5, 4),
            SendOSC(klickport, '/klick/simple/set_pattern', 'Xxxxx'),
            SendOSC(klickport, '/klick/metro/start'),

            SendOSC(audioseqport, '/Audioseq/Bpm', 120),
            SendOSC(audioseqport, '/Audioseq/Play', timestamp),
            SendOSC(audioseqport, '/Audioseq/Sequence/Enable', 'le5_louboutin'),

            SendOSC(slport, '/sl/0/hit', 'pause_on'), # bass
            SendOSC(slport, '/sl/2/hit', 'pause_on'), # vxorlpre
            SendOSC(slport, '/sl/4/hit', 'pause_on'), # vxjeannotpre

            SendOSC(lightseqport, '/Lightseq/Bpm', 960),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_jardin', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Random', 'le5_boum_cour', 1),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_jardin'),
            SendOSC(lightseqport, '/Lightseq/Sequence/Play', 'le5_boum_cour'),
            SendOSC(lightseqport, '/Lightseq/Play', timestamp),

            vxorlgars_off,
            vxorlmeuf_on,
            vxorldisint_off,
            vxorldelay_off,
            vxorlvocode_off,

            ] >> Discard()
        ],
    jeannot >> ProgramFilter(7) >> [  # stop reverse Instouboul => Louboutin - Bouton 10
        Program(73) >> cseqtrigger,
        [

            SendOSC(slport, '/sl/-1/hit', 'reverse'),
            SendOSC(surfaceorlport, '/sl/-1/hit', 'reverse', 1),

            SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_instouboulouboutin'),
            SendOSC(rpijardinport, '/pyta/text/visible', 0, 1),
            SendOSC(rpicourport, '/pyta/text/visible', 0, 1),


            ] >> Discard()
        ],
    jeannot >> ProgramFilter(8) >> [
        SendOSC(trapcutport, '/Trapcut/Scene/Play', 'I') >> Discard(),
        SendOSC(lightseqport, '/Lightseq/Scene/Play', 'le5_trapcup'),
    ],
    # orl >> ProgramFilter(11) >> [ # trapone (disabled)
    #     SceneSwitch(6) >> Discard(),
    #     Program(2) >> Output('PBCtrlOut', 1)
    #     ],
    orl >> ProgramFilter(11) >> [ # SW
        SceneSwitch(7) >> Discard(),
        Program(2) >> Output('PBCtrlOut', 1)
        ],

    ]
