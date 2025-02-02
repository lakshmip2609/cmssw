import FWCore.ParameterSet.Config as cms

#Parameterset for the hadronic shower trigger for Run-3
showerPSet = cms.PSet(
    ## what kind of shower triggers the logic?
    ## 0: cathode-only (TMB/OTMB)
    ## 1: anode-only (from ALCT board)
    ## 2: cathode or anode showers
    ##    loose -> 'loose anode or loose cathode'
    ##    nominal -> 'nominal anode or nominal cathode'
    ##    tight -> 'tight anode or tight cathode'
    ## 3: cathode and anode showers
    ##    loose -> 'loose anode and loose cathode'
    ##    nominal -> 'nominal anode and nominal cathode'
    ##    tight -> 'tight anode and tight cathode'
    source  = cms.uint32(3),

    ## settings for cathode showers (counting CSCComparatorDigi)
    cathodeShower = cms.PSet(
        ## {loose, nominal, tight} thresholds for hit counters
        ## loose ~ 0.75 kHz
        ## nominal ~ 0.5  kHz
        ## tight ~ 0.25 kHz
        showerThresholds = cms.vuint32(
            # ME1/1
            100, 100, 100,
            # ME1/2
            19, 38, 42,
            # ME1/3
            8, 11, 15,
            # ME2/1
            17, 33, 35,
            # ME2/2
            10, 20, 24,
            # ME3/1
            15, 31, 33,
            # ME3/2
            9, 18, 22,
            # ME4/1
            17, 34, 36,
            # ME4/2
            11, 22, 26
        ),
        showerMinInTBin = cms.uint32(6),
        showerMaxInTBin = cms.uint32(8),
        showerMinOutTBin = cms.uint32(2),
        showerMaxOutTBin = cms.uint32(5),
        minLayersCentralTBin = cms.uint32(5),
    ),
    ## settings for anode showers (counting CSCWireDigi)
    anodeShower = cms.PSet(
        ## {loose, nominal, tight} thresholds for hit counters
        showerThresholds = cms.vuint32(
            # ME1/1
            140, 140, 140,
            # ME1/2
            20, 41, 45,
            # ME1/3
            8, 12, 16,
            # ME2/1
            28, 56, 58,
            # ME2/2
            9, 18, 22,
            # ME3/1
            26, 55, 57,
            # ME3/2
            8, 16, 20,
            # ME4/1
            31, 62, 64,
            # ME4/2
            13, 27, 31
        ),
        showerMinInTBin = cms.uint32(8),
        showerMaxInTBin = cms.uint32(8),
        showerMinOutTBin = cms.uint32(4),
        showerMaxOutTBin = cms.uint32(7),
        minLayersCentralTBin = cms.uint32(5),
    )
)
