import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',          action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',             action='store_true',    help="Update current entry in db?")
    argParser.add_argument('--check_completeness', action='store_true',    help="Check competeness?")
    return argParser

# Logging
if __name__=="__main__":
    import Samples.Tools.logger as logger
    logger = logger.get_logger("INFO", logFile = None )
    import RootTools.core.logger as logger_rt
    logger_rt = logger_rt.get_logger("INFO", logFile = None )
    options = get_parser().parse_args()
    ov = options.overwrite
    if options.update:
        ov = 'update'
else:
    import logging
    logger = logging.getLogger(__name__)
    ov = False

# Redirector
#try:
#    redirector = sys.modules['__main__'].redirector
#except:
#    if "clip" in os.getenv("HOSTNAME").lower():
#        if __name__ == "__main__" and not options.check_completeness:
#            from Samples.Tools.config import redirector_global as redirector
#        else:
#            #from Samples.Tools.config import redirector_clip_local as redirector
#            from Samples.Tools.config import redirector_global as redirector
#    else:
#        from Samples.Tools.config import redirector as redirector
#print redirector
## DB
#from Samples.Tools.config import dbDir
#dbFile = dbDir+'/DB_UL16v2_private.sql'
#
#logger.info("Using db file: %s", dbFile)

## DY
DYJetsToLL_M50_HT70to100      =   Sample.fromDirectory("DYJetsToLL_M50_HT70to100"    ,     "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141355/",         xSection=169.9*1.23)
DYJetsToLL_M50_HT100to200     =   Sample.fromDirectory("DYJetsToLL_M50_HT100to200",        "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141418/",         xSection=147.4*1.23)
DYJetsToLL_M50_HT200to400     =   Sample.fromDirectory("DYJetsToLL_M50_HT200to400",        "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141443/",         xSection=40.99*1.23)
#DYJetsToLL_M50_HT400to600     =   Sample.fromDirectory("DYJetsToLL_M50_HT400to600",        "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/",         xSection=5.678*1.23)
DYJetsToLL_M50_HT600to800     =   Sample.fromDirectory("DYJetsToLL_M50_HT600to800"   ,     "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141535/",         xSection=1.367*1.23 )
#DYJetsToLL_M50_HT800to1200    =   Sample.fromDirectory("DYJetsToLL_M50_HT800to1200"  ,     "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/",         xSection=0.6304*1.23 )
DYJetsToLL_M50_HT1200to2500   =   Sample.fromDirectory("DYJetsToLL_M50_HT1200to2500" ,     "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141642/",         xSection=0.1514*1.23 )
DYJetsToLL_M50_HT2500toInf    =   Sample.fromDirectory("DYJetsToLL_M50_HT2500toInf"  ,     "/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141708/",         xSection=0.003565*1.23 )
#
DYJetsM50HT = [
    DYJetsToLL_M50_HT70to100 , 
    DYJetsToLL_M50_HT100to200,
    DYJetsToLL_M50_HT200to400,
    #DYJetsToLL_M50_HT400to600,
    DYJetsToLL_M50_HT600to800  ,
#    DYJetsToLL_M50_HT800to1200 ,
    DYJetsToLL_M50_HT1200to2500,
    DYJetsToLL_M50_HT2500toInf ,
]

#DYJetsToLL_M5to50_HT70to100      = Sample.fromDirectory("DYJetsToLL_M5to50_HT70to100"     , "",         xSection=303.4) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT100to200     = Sample.fromDirectory("DYJetsToLL_M5to50_HT100to200"    , "",         xSection=224.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT200to400     = Sample.fromDirectory("DYJetsToLL_M5to50_HT200to400"    , "",         xSection=37.2) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT400to600     = Sample.fromDirectory("DYJetsToLL_M5to50_HT400to600"    , "",         xSection=3.581) #LO without 1.23 k-factor
#DYJetsToLL_M5to50_HT600toInf     = Sample.fromDirectory("DYJetsToLL_M5to50_HT600toInf"    , "",         xSection=1.124) #LO without 1.23 k-factor

#DYJetsM5to50HT = [
#    DYJetsToLL_M5to50_HT70to100,
#    DYJetsToLL_M5to50_HT100to200,
#    DYJetsToLL_M5to50_HT200to400,
#    DYJetsToLL_M5to50_HT400to600,
#    DYJetsToLL_M5to50_HT600toInf,
#]

# x-secs using runXSecAnalyzer
DYJetsToNuNu_HT100to200       = Sample.fromDirectory("DYJetsToNuNu_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_140935/",         xSection=280.35*1.23)
DYJetsToNuNu_HT200to400       = Sample.fromDirectory("DYJetsToNuNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_140958/",         xSection=77.67*1.23)
#DYJetsToNuNu_HT400to600       = Sample.fromDirectory("DYJetsToNuNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/",         xSection=10.73*1.23)
#DYJetsToNuNu_HT600to800       = Sample.fromDirectory("DYJetsToNuNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/",         xSection=2.559*1.23)
#DYJetsToNuNu_HT800to1200      = Sample.fromDirectory("DYJetsToNuNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/",         xSection=1.1796*1.23)
DYJetsToNuNu_HT1200to2500     = Sample.fromDirectory("DYJetsToNuNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141150/",         xSection=0.28833*1.23)
DYJetsToNuNu_HT2500toInf      = Sample.fromDirectory("DYJetsToNuNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141218/",         xSection=0.006945*1.23)

DYJetsNuNuHT = [
   DYJetsToNuNu_HT100to200,
   DYJetsToNuNu_HT200to400,
   #DYJetsToNuNu_HT400to600,
   #DYJetsToNuNu_HT600to800,
   #DYJetsToNuNu_HT800to1200,
   DYJetsToNuNu_HT1200to2500,
   DYJetsToNuNu_HT2500toInf,
]


DY =  DYJetsNuNuHT + DYJetsM50HT #+ DYJetsM5to50HT 
## ttbar
#TTLep_pow_CP5       = Sample.fromDirectory("TTLep_pow_CP5",            "/eos/vbc/experiments/cms/store/user/prhussai/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/",            xSection=831.762*((3*0.108)**2))
#TTSingleLep_pow_CP5 = Sample.fromDirectory("TTSingleLep_pow_CP5",      "/eos/vbc/experiments/cms/store/user/prhussai/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/",            xSection=831.762*(3*0.108)*(1-3*0.108)*2)
#TTbar               = Sample.fromDirectory("TTbar",                	"",        xSection=831.762)
#TTJets_amcatnlo     = Sample.fromDirectory("TTJets_amcatnlo",          "",        xSection=831.762)

## single top
#
#T_tch_pow           = Sample.fromDirectory("T_tch_pow",        "/ST_t-channel_top_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1",         xSection=136.02) # inclusive sample
#TBar_tch_pow        = Sample.fromDirectory("TBar_tch_pow",     "/ST_t-channel_antitop_4f_inclusiveDecays_13TeV-powhegV2-madspin-pythia8_TuneCUETP8M1/",     xSection=80.95) # inclusive sample
#
T_tWch_ext          = Sample.fromDirectory("T_tWch_ext",       "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141731/",         xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext       = Sample.fromDirectory("TBar_tWch_ext",    "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210903_080729/",     xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect

## ttV
#TTWToLNu_CP5        = Sample.fromDirectory("TTWToLNu_CP5" ,    "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/",   xSection=0.2043)
#TTWToQQ             = Sample.fromDirectory("TTWToQQ",          "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/",         xSection=0.40620)
#TTZ_LO              = Sample.fromDirectory("TTZ_LO",           "/ttZJets_13TeV_madgraphMLM-pythia8/",                                   xSection=0.5297/0.692)
#TTGJets             = Sample.fromDirectory("TTGJets",          "/eos/vbc/experiments/cms/store/user/prhussai/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/",             xSection=3.697)
#TTGJets_ext         = Sample.fromDirectory("TTGJets_ext",      "/TTGJets_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8/",        xSection=3.697)
TTV = []
#TTV = [TTWToLNu_CP5 , TTGJets]

top = [
    
#    #TTbar,
    #TTLep_pow_CP5,
    #TTSingleLep_pow_CP5,
#    #T_tch_pow,
#    #TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
    ] + TTV 

## di/multiboson
WWTo2L2Nu           = Sample.fromDirectory("WWTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2_privateUL18v1_nanov2/210830_141245/",   xSection=12.178)
#WWToLNuQQ           = Sample.fromDirectory("WWToLNuQQ",        "/WWToLNuQQ_13TeV-powheg/",         xSection=49.997)

ZZTo2L2Nu           = Sample.fromDirectory("ZZTo2L2Nu",            "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_141308/",                     xSection=0.564)
#ZZTo2L2Q            = Sample.fromDirectory("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_powheg_pythia8/",                           xSection=3.28)
#ZZTo2Q2Nu           = Sample.fromDirectory("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=4.04)
ZZTo4L              = Sample.fromDirectory("ZZTo4L",               "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v2_privateUL18v1_nanov2/210830_141331/",                             xSection=1.256*1.1)

#WZTo1L3Nu           = Sample.fromDirectory("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.fromDirectory("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/",          xSection=10.71)
#WZTo2L2Q            = Sample.fromDirectory("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/",             xSection=5.60)
#WZTo3LNu            = Sample.fromDirectory("WZTo3LNu",             "/WZTo3LNu",         xSection=4.42965)
#WZTo3LNu_amcatnlo   = Sample.fromDirectory("WZTo3LNu_amcatnlo",    "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/",        xSection=4.666)


boson = [
    WWTo2L2Nu,
#    #WWToLNuQQ,
    ZZTo2L2Nu,
#    #ZZTo2L2Q,
#    #ZZTo2Q2Nu,
    ZZTo4L,
#    #WZTo1L3Nu,
#    #WZTo1L1Nu2Q,
#    #WZTo2L2Q,
#    #WZTo3LNu,
#    WZTo3LNu_amcatnlo,
    ]


## HT-binned
#WJetsToLNu_HT70to100        = Sample.fromDirectory("WJetsToLNu_HT70to100",        "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/",        xSection=1637.13)
WJetsToLNu_HT100to200       = Sample.fromDirectory("WJetsToLNu_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL18MiniAOD-106X_upgrade2018_realistic_v11_L1v1-v1_privateUL18v1_nanov2/210830_125552/",       xSection=1627.45)
#WJetsToLNu_HT200to400       = Sample.fromDirectory("WJetsToLNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/",       xSection=435.237)
#WJetsToLNu_HT400to600       = Sample.fromDirectory("WJetsToLNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/",       xSection=59.1811)
#WJetsToLNu_HT600to800       = Sample.fromDirectory("WJetsToLNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/",       xSection=14.5805)
#WJetsToLNu_HT800to1200      = Sample.fromDirectory("WJetsToLNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/",      xSection=6.65621)
#WJetsToLNu_HT1200to2500     = Sample.fromDirectory("WJetsToLNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/", xSection=1.60809)
#WJetsToLNu_HT2500toInf      = Sample.fromDirectory("WJetsToLNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/",     xSection=0.0389136)


wjets_ht = [
    #WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    #WJetsToLNu_HT200to400,
    #WJetsToLNu_HT400to600,
    #WJetsToLNu_HT600to800,
    #WJetsToLNu_HT800to1200,
    #WJetsToLNu_HT1200to2500,
    #WJetsToLNu_HT2500toInf,
    ]

#wjets += wjets_ht


signals = [
    ]



### QCD

## QCD HT bins (cross sections from McM)
#QCD_HT50to100        = Sample.fromDirectory("QCD_HT50to100",        "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/",           xSection=246400000.0)
#QCD_HT100to200       = Sample.fromDirectory("QCD_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/",          xSection=27850000.0)
#QCD_HT200to300       = Sample.fromDirectory("QCD_HT200to300",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/",          xSection=1717000)
#QCD_HT300to500       = Sample.fromDirectory("QCD_HT300to500",       "",          xSection=351300)
#QCD_HT500to700       = Sample.fromDirectory("QCD_HT500to700",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/",          xSection=31630)
#QCD_HT700to1000      = Sample.fromDirectory("QCD_HT700to1000",      "",         xSection=6802)
#QCD_HT1000to1500     = Sample.fromDirectory("QCD_HT1000to1500",     "",        xSection=1206)
#QCD_HT1500to2000     = Sample.fromDirectory("QCD_HT1500to2000",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/",        xSection=120.4)
#QCD_HT2000toInf      = Sample.fromDirectory("QCD_HT2000toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/",         xSection=25.25)
QCD_HT = []
#QCD_HT = [
#    QCD_HT50to100,
#    QCD_HT100to200,
#    QCD_HT200to300,
#    QCD_HT300to500,
#    QCD_HT500to700,
#    QCD_HT700to1000,
#    QCD_HT1000to1500,
#    QCD_HT1500to2000,
#    QCD_HT2000toInf,
#    ]
allSamples = DY + top + boson + wjets_ht + signals + QCD_HT 
for s in allSamples:
    s.isData = False
    for i_f, f in enumerate(s.files):
	    if f.startswith('/eos/'):
		    s.files[i_f] = 'root://eos.grid.vbc.ac.at/'+f

