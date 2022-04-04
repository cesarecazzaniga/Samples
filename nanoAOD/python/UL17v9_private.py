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

DYJetsToLL_M50_HT70to100      =   Sample.fromDirectory("DYJetsToLL_M50_HT70to100",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203012/",	 xSection=169.9*1.23)
DYJetsToLL_M50_HT70to100.normalization = 12205958.0 
DYJetsToLL_M50_HT100to200     =   Sample.fromDirectory("DYJetsToLL_M50_HT100to200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203032/",	 xSection=147.4*1.23)
DYJetsToLL_M50_HT100to200.normalization = 18955253.0
DYJetsToLL_M50_HT200to400     =   Sample.fromDirectory("DYJetsToLL_M50_HT200to400",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203052/",	xSection=40.99*1.23)
DYJetsToLL_M50_HT200to400.normalization = 12513057.0
DYJetsToLL_M50_HT400to600     =   Sample.fromDirectory("DYJetsToLL_M50_HT400to600",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203111/",	xSection=5.678*1.23)
DYJetsToLL_M50_HT400to600.normalization = 5543804.0
DYJetsToLL_M50_HT600to800     =   Sample.fromDirectory("DYJetsToLL_M50_HT600to800",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203130/",	xSection=1.367*1.23 )
DYJetsToLL_M50_HT600to800.normalization = 5278417.0
DYJetsToLL_M50_HT800to1200    =   Sample.fromDirectory("DYJetsToLL_M50_HT800to1200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203149/",	xSection=0.6304*1.23 )
DYJetsToLL_M50_HT800to1200.normalization = 4506887.0
DYJetsToLL_M50_HT1200to2500   =   Sample.fromDirectory("DYJetsToLL_M50_HT1200to2500",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203209/",xSection=0.1514*1.23 )
DYJetsToLL_M50_HT1200to2500.normalization = 4802716.0
DYJetsToLL_M50_HT2500toInf    =   Sample.fromDirectory("DYJetsToLL_M50_HT2500toInf",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203230/",	xSection=0.003565*1.23 )
DYJetsToLL_M50_HT2500toInf.normalization = 1480047.0
DYJetsM50HT = [
		DYJetsToLL_M50_HT70to100,
		DYJetsToLL_M50_HT100to200,
		DYJetsToLL_M50_HT200to400,
		DYJetsToLL_M50_HT400to600,
		DYJetsToLL_M50_HT600to800,
		DYJetsToLL_M50_HT800to1200,
		DYJetsToLL_M50_HT1200to2500,
		DYJetsToLL_M50_HT2500toInf,
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
DYJetsToNuNu_HT100to200       = Sample.fromDirectory("DYJetsToNuNu_HT100to200",	      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202619/",	       xSection=280.35*1.23)
DYJetsToNuNu_HT100to200.normalization = 18983897.0 
DYJetsToNuNu_HT200to400       = Sample.fromDirectory("DYJetsToNuNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202637/",         xSection=77.67*1.23)
DYJetsToNuNu_HT200to400.normalization =  17349597.0
DYJetsToNuNu_HT400to600       = Sample.fromDirectory("DYJetsToNuNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202656/",         xSection=10.73*1.23)
DYJetsToNuNu_HT400to600.normalization = 13963690.0
DYJetsToNuNu_HT600to800       = Sample.fromDirectory("DYJetsToNuNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202716/",         xSection=2.559*1.23)
DYJetsToNuNu_HT600to800.normalization = 4418971.0
DYJetsToNuNu_HT800to1200      = Sample.fromDirectory("DYJetsToNuNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202736/",         xSection=1.1796*1.23)
DYJetsToNuNu_HT800to1200.normalization = 1513585.0
DYJetsToNuNu_HT1200to2500     = Sample.fromDirectory("DYJetsToNuNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202755/",         xSection=0.28833*1.23)
DYJetsToNuNu_HT1200to2500.normalization = 267125.0
DYJetsToNuNu_HT2500toInf      = Sample.fromDirectory("DYJetsToNuNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202833/",         xSection=0.006945*1.23)
DYJetsToNuNu_HT2500toInf.normalization = 176201.0

DYJetsNuNuHT = [
   DYJetsToNuNu_HT100to200,
   DYJetsToNuNu_HT200to400,
   DYJetsToNuNu_HT400to600,
   DYJetsToNuNu_HT600to800,
   DYJetsToNuNu_HT800to1200,
   DYJetsToNuNu_HT1200to2500,
   DYJetsToNuNu_HT2500toInf,
]


DY = DYJetsM50HT  + DYJetsNuNuHT  #+ DYJetsM5to50HT

## ttbar
TTLep_pow_CP5       = Sample.fromDirectory("TTLep_pow_CP5",            "/eos/vbc/experiments/cms/store/user/prhussai/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202117/",            xSection=831.762*((3*0.108)**2))
TTLep_pow_CP5.normalization = 7695841652.17 
TTSingleLep_pow_CP5 = Sample.fromDirectory("TTSingleLep_pow_CP5",      "/eos/vbc/experiments/cms/store/user/prhussai/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202331/",            xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTSingleLep_pow_CP5.normalization =  106922359721.0
#TTbar               = Sample.fromDirectory("TTbar",                "",        xSection=831.762)
#TTJets_amcatnlo     = Sample.fromDirectory("TTJets_amcatnlo",                "",        xSection=831.762)

## single top
#
T_tch_pow           = Sample.fromDirectory("T_tch_pow",        "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/220323_084011/",         xSection=136.02) 
T_tch_pow.normalization = 13434789518.9 
TBar_tch_pow        = Sample.fromDirectory("TBar_tch_pow",     "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203248/",     xSection=80.95)
TBar_tch_pow.normalization = 4471058680.0

T_tWch_ext          = Sample.fromDirectory("T_tWch_ext",       "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203327/",         xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
T_tWch_ext.normalization = 276021555.621
TBar_tWch_ext       = Sample.fromDirectory("TBar_tWch_ext",    "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203306/",     xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext.normalization = 274168362.624

## ttV
TTWToLNu_CP5        = Sample.fromDirectory("TTWToLNu_CP5" ,    "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203405/",   xSection=0.2043)
TTWToLNu_CP5.normalization = 2500272.10683
TTWToQQ             = Sample.fromDirectory("TTWToQQ",          "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203424/",         xSection=0.40620)
TTWToQQ.normalization = 444333.974766
TTZ_LO              = Sample.fromDirectory("TTZ_LO",           "/eos/vbc/experiments/cms/store/user/prhussai/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/211124_203503/",                                   xSection=0.5297/0.692)
TTZ_LO.normalization = 32503711.0
TTW_LO		    = Sample.fromDirectory("TTW_LO",		"/eos/vbc/experiments/cms/store/user/prhussai/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/211124_203444/",	xSection=0.6105)	
TTW_LO.normalization = 27662138.0
TTGJets             = Sample.fromDirectory("TTGJets",          "/eos/vbc/experiments/cms/store/user/prhussai/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_203347/",             xSection=3.697)
TTGJets.normalization = 22157556.6335

TTV = [TTWToLNu_CP5, TTWToQQ , TTGJets , TTZ_LO, TTW_LO]

top = [
    
#    #TTbar,
    TTLep_pow_CP5,
    TTSingleLep_pow_CP5,
    T_tch_pow,
    TBar_tch_pow,
    T_tWch_ext,
    TBar_tWch_ext,
    ] + TTV 

## di/multiboson
WWTo2L2Nu           = Sample.fromDirectory("WWTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161629/",   xSection=12.178)
WWTo2L2Nu.normalization = 32147079.1672 
#WWToLNuQQ           = Sample.fromDirectory("WWToLNuQQ",        "/WWToLNuQQ_13TeV-powheg/",         xSection=49.997)
WW           	    = Sample.fromDirectory("WW",        "/eos/vbc/experiments/cms/store/user/prhussai/WW_TuneCP5_13TeV-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/220323_083948/",         xSection=63.21 * 1.82)
WW.normalization    = 15634116.1995

ZZTo2L2Nu           = Sample.fromDirectory("ZZTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202934/",                     xSection=0.564)
ZZTo2L2Nu.normalization = 39767479.5829

#ZZTo2L2Q            = Sample.fromDirectory("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_powheg_pythia8/",                           xSection=3.28)
#ZZTo2Q2Nu           = Sample.fromDirectory("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=4.04)
ZZTo4L              = Sample.fromDirectory("ZZTo4L",               "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/211124_202953/",                             xSection=1.256*1.1)
ZZTo4L.normalization = 131669255.013

#WZTo1L3Nu           = Sample.fromDirectory("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.fromDirectory("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/",          xSection=10.71)
#WZTo2L2Q            = Sample.fromDirectory("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/",             xSection=5.60)
#WZTo3LNu            = Sample.fromDirectory("WZTo3LNu",             "/WZTo3LNu",         xSection=4.42965)
WZTo3LNu_amcatnlo   = Sample.fromDirectory("WZTo3LNu_amcatnlo",    "/eos/vbc/experiments/cms/store/user/prhussai/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/211124_202914/",        xSection=4.666)
WZTo3LNu_amcatnlo.normalization = 87559047.7174 


boson = [
    WWTo2L2Nu,
#    #WWToLNuQQ,
    WW,
    ZZTo2L2Nu,
#    #ZZTo2L2Q,
#    #ZZTo2Q2Nu,
    ZZTo4L,
#    #WZTo1L3Nu,
#    #WZTo1L1Nu2Q,
#    #WZTo2L2Q,
#    #WZTo3LNu,
    WZTo3LNu_amcatnlo,
    ]


## HT-binned
WJetsToLNu_HT70to100        = Sample.fromDirectory("WJetsToLNu_HT70to100",        "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202352/",        xSection=1637.13)
WJetsToLNu_HT70to100.normalization = 44736228.0 
WJetsToLNu_HT100to200       = Sample.fromDirectory("WJetsToLNu_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202411/",       xSection=1627.45)
WJetsToLNu_HT100to200.normalization = 47424468.0
WJetsToLNu_HT200to400       = Sample.fromDirectory("WJetsToLNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202443/",       xSection=435.237)
WJetsToLNu_HT200to400.normalization = 42602407.0
WJetsToLNu_HT400to600       = Sample.fromDirectory("WJetsToLNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202502/",       xSection=59.1811)
WJetsToLNu_HT400to600.normalization = 5468473.0
WJetsToLNu_HT600to800       = Sample.fromDirectory("WJetsToLNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202521/",       xSection=14.5805)
WJetsToLNu_HT600to800.normalization = 5545298.0
WJetsToLNu_HT800to1200      = Sample.fromDirectory("WJetsToLNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220323_083111/",      xSection=6.65621)
WJetsToLNu_HT800to1200.normalization = 5088483.0 
WJetsToLNu_HT1200to2500     = Sample.fromDirectory("WJetsToLNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211124_202540/", 	xSection=1.60809)
WJetsToLNu_HT1200to2500.normalization = 4955636.0
WJetsToLNu_HT2500toInf      = Sample.fromDirectory("WJetsToLNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/211124_202600/",     xSection=0.0389136)
WJetsToLNu_HT2500toInf.normalization = 1185699.0


wjets_ht = [
    WJetsToLNu_HT70to100,
    WJetsToLNu_HT100to200,
    WJetsToLNu_HT200to400,
    WJetsToLNu_HT400to600,
    WJetsToLNu_HT600to800,
    WJetsToLNu_HT800to1200,
    WJetsToLNu_HT1200to2500,
    WJetsToLNu_HT2500toInf,
    ]

#wjets += wjets_ht


signals = [
    ]



### QCD

## QCD HT bins (cross sections from McM)
QCD_HT50to100        = Sample.fromDirectory("QCD_HT50to100",        "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211126_145550/",           xSection=246400000.0)
QCD_HT50to100.normalization = 26243010.0 
QCD_HT100to200       = Sample.fromDirectory("QCD_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/220323_084033/",          xSection=27850000.0)
QCD_HT100to200.normalization = 54760426.0 
QCD_HT200to300       = Sample.fromDirectory("QCD_HT200to300",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211126_150355/",          xSection=1717000)
QCD_HT200to300.normalization = 42714435.0
QCD_HT300to500       = Sample.fromDirectory("QCD_HT300to500",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211126_150751/",          xSection=351300)
QCD_HT300to500.normalization = 43589739.0 
QCD_HT500to700       = Sample.fromDirectory("QCD_HT500to700",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211126_150810/",          xSection=31630)
QCD_HT500to700.normalization = 36194860.0 
QCD_HT700to1000      = Sample.fromDirectory("QCD_HT700to1000",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211126_150836/",         xSection=6802)
QCD_HT700to1000.normalization = 34051754.0
QCD_HT1000to1500     = Sample.fromDirectory("QCD_HT1000to1500",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/220323_084429/",        xSection=1206)
QCD_HT1000to1500.normalization = 10111772.0 
QCD_HT1500to2000     = Sample.fromDirectory("QCD_HT1500to2000",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/211126_145631/",        xSection=120.4)
QCD_HT1500to2000.normalization = 7701876.0
QCD_HT2000toInf      = Sample.fromDirectory("QCD_HT2000toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1_privateUL17nanov9/220323_084104/",         xSection=25.25)
QCD_HT2000toInf.normalization = 3914281.0 

QCD_HT = [
    QCD_HT50to100,
    QCD_HT100to200,
    QCD_HT200to300,
    QCD_HT300to500,
    QCD_HT500to700,
    QCD_HT700to1000,
    QCD_HT1000to1500,
    QCD_HT1500to2000,
    QCD_HT2000toInf,
    ]

SMS_T2tt_mStop_500_mLSP_420      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_420",	"/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220323_084123/",	xSection=1.)
SMS_T2tt_mStop_500_mLSP_420.normalization = 1001819.0 
SMS_T2tt_mStop_500_mLSP_450      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_450",	"/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-450_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220323_084143/",	xSection=1.)
SMS_T2tt_mStop_500_mLSP_450.normalization = 992089.0
SMS_T2tt_mStop_500_mLSP_470      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_470",	"/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220323_084207/",	xSection=1.)
SMS_T2tt_mStop_500_mLSP_470.normalization = 816993.0

SMS_T2tt_LL_mStop_400_mLSP_380      = Sample.fromDirectory("SMS_T2tt_LL_mStop_400_mLSP_380",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220325_103840/",		xSection=1.)
SMS_T2tt_LL_mStop_400_mLSP_380.normalization = 939925.0
SMS_T2tt_LL_mStop_350_mLSP_335      = Sample.fromDirectory("SMS_T2tt_LL_mStop_350_mLSP_335",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-350_mLSP-335_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220325_103812/",		xSection=1.)
SMS_T2tt_LL_mStop_350_mLSP_335.normalization = 984468.0
SMS_T2tt_LL_mStop_300_mLSP_290      = Sample.fromDirectory("SMS_T2tt_LL_mStop_300_mLSP_290",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-300_mLSP-290_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v2_privateUL17nanov9/220325_101251/",		xSection=1.)
SMS_T2tt_LL_mStop_300_mLSP_290.normalization = 971258.0

compSUSY = [
		SMS_T2tt_mStop_500_mLSP_420,
		SMS_T2tt_mStop_500_mLSP_450,
		SMS_T2tt_mStop_500_mLSP_470,
		SMS_T2tt_LL_mStop_400_mLSP_380,
		SMS_T2tt_LL_mStop_350_mLSP_335,
		SMS_T2tt_LL_mStop_300_mLSP_290,
	]



allSamples = DY + top + boson + wjets_ht + signals + QCD_HT + compSUSY 

for s in allSamples:
    
    s.isData = False
    for i_f, f in enumerate(s.files):
	    if f.startswith('/eos/'):
		    s.files[i_f] = 'root://eos.grid.vbc.ac.at/'+f

