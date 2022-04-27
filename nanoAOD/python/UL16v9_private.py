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

from Samples.Tools.config import  redirector

from Samples.Tools.config import dbDir
dbFile = dbDir+"/DB_Summer16_private_legacy.sql"

logger.info("Using db file: %s", dbFile)

DYJetsToLL_M50_LO	      =	  Sample.fromDirectory("DYJetsToLL_M50_LO",		"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220415_110107/", xSection=2075.14*3)
DYJetsToLL_M50_LO.normalization = 82448537.0
DYJetsToLL_M10to50_LO	      =	  Sample.fromDirectory("DYJetsToLL_M10to50_LO",		"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220415_110130/", xSection=18610)
DYJetsToLL_M10to50_LO.normalization = 23706672.0


DYJetsToLL_M50_HT70to100      =   Sample.fromDirectory("DYJetsToLL_M50_HT70to100",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161728/",	 xSection=169.9*1.23)
DYJetsToLL_M50_HT70to100.normalization = 5893910.0
DYJetsToLL_M50_HT100to200     =   Sample.fromDirectory("DYJetsToLL_M50_HT100to200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161746/",	 xSection=147.4*1.23)
DYJetsToLL_M50_HT100to200.normalization = 8316351.0
DYJetsToLL_M50_HT200to400     =   Sample.fromDirectory("DYJetsToLL_M50_HT200to400",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161805/",	xSection=40.99*1.23)
DYJetsToLL_M50_HT200to400.normalization = 5653782.0
DYJetsToLL_M50_HT400to600     =   Sample.fromDirectory("DYJetsToLL_M50_HT400to600",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161824/",	xSection=5.678*1.23)
DYJetsToLL_M50_HT400to600.normalization = 2491416.0
DYJetsToLL_M50_HT600to800     =   Sample.fromDirectory("DYJetsToLL_M50_HT600to800",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161843/",	xSection=1.367*1.23 )
DYJetsToLL_M50_HT600to800.normalization = 2299853.0
DYJetsToLL_M50_HT800to1200    =   Sample.fromDirectory("DYJetsToLL_M50_HT800to1200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161900/",	xSection=0.6304*1.23 )
DYJetsToLL_M50_HT800to1200.normalization = 2393976.0
DYJetsToLL_M50_HT1200to2500   =   Sample.fromDirectory("DYJetsToLL_M50_HT1200to2500",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161919/",xSection=0.1514*1.23 )
DYJetsToLL_M50_HT1200to2500.normalization = 1970857.0
DYJetsToLL_M50_HT2500toInf    =   Sample.fromDirectory("DYJetsToLL_M50_HT2500toInf",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161939",	xSection=0.003565*1.23 )
DYJetsToLL_M50_HT2500toInf.normalization = 696811.0

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
##DYJetsToLL_M5to50_HT70to100      = Sample.fromDirectory("DYJetsToLL_M5to50_HT70to100"     , "",         xSection=303.4) #LO without 1.23 k-factor
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

##x-secs using runXSecAnalyzer
DYJetsToNuNu_HT100to200       = Sample.fromDirectory("DYJetsToNuNu_HT100to200",	      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161437/",	       xSection=280.35*1.23)
DYJetsToNuNu_HT100to200.normalization = 7083216.0
DYJetsToNuNu_HT200to400       = Sample.fromDirectory("DYJetsToNuNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161456/",         xSection=77.67*1.23)
DYJetsToNuNu_HT200to400.normalization = 6814106.0 
DYJetsToNuNu_HT400to600       = Sample.fromDirectory("DYJetsToNuNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_215757/",         xSection=10.73*1.23)
DYJetsToNuNu_HT400to600.normalization = 5854171.0 
DYJetsToNuNu_HT600to800       = Sample.fromDirectory("DYJetsToNuNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161516/",         xSection=2.559*1.23)
DYJetsToNuNu_HT600to800.normalization = 1881671.0
DYJetsToNuNu_HT800to1200      = Sample.fromDirectory("DYJetsToNuNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_220637/",         xSection=1.1796*1.23)
DYJetsToNuNu_HT800to1200.normalization = 633500.0
DYJetsToNuNu_HT1200to2500     = Sample.fromDirectory("DYJetsToNuNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161536/",         xSection=0.28833*1.23)
DYJetsToNuNu_HT1200to2500.normalization = 115609.0
DYJetsToNuNu_HT2500toInf      = Sample.fromDirectory("DYJetsToNuNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161555/",         xSection=0.006945*1.23)
DYJetsToNuNu_HT2500toInf.normalization = 110461.0

DYJetsNuNuHT = [
   DYJetsToNuNu_HT100to200,
   DYJetsToNuNu_HT200to400,
   DYJetsToNuNu_HT400to600,
   DYJetsToNuNu_HT600to800,
   DYJetsToNuNu_HT800to1200,
   DYJetsToNuNu_HT1200to2500,
   DYJetsToNuNu_HT2500toInf,
]


DY = [
	DYJetsToLL_M50_LO,
	DYJetsToLL_M10to50_LO,
	] + DYJetsM50HT  + DYJetsNuNuHT  #+ DYJetsM5to50HT

## ttbar
TTLep_pow_CP5       = Sample.fromDirectory("TTLep_pow_CP5",            "/eos/vbc/experiments/cms/store/user/prhussai/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211010_110921/",            xSection=831.762*((3*0.108)**2))
TTLep_pow_CP5.normalization = 2780625477.44 
TTSingleLep_pow_CP5 = Sample.fromDirectory("TTSingleLep_pow_CP5",      "/eos/vbc/experiments/cms/store/user/prhussai/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211010_120526/",            xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTSingleLep_pow_CP5.normalization = 38575657537.2 
#TTbar               = Sample.fromDirectory("TTbar",                "",        xSection=831.762)
#TTJets_amcatnlo     = Sample.fromDirectory("TTJets_amcatnlo",                "",        xSection=831.762)

## single top

T_tch_pow           = Sample.fromDirectory("T_tch_pow",        "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3_privateUL16nanov9/211124_161958/",         xSection=136.02) 
T_tch_pow.normalization = 6703801969.77 

TBar_tch_pow        = Sample.fromDirectory("TBar_tch_pow",     "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v3_privateUL16nanov9/211124_162042/",     xSection=80.95)
TBar_tch_pow.normalization = 1957283183.15

T_tWch_ext          = Sample.fromDirectory("T_tWch_ext",       "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162119/",         xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
T_tWch_ext.normalization = 109290196.266
TBar_tWch_ext       = Sample.fromDirectory("TBar_tWch_ext",    "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162101/",     xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext.normalization = 118799348.672

## ttV
TTWToLNu_CP5        = Sample.fromDirectory("TTWToLNu_CP5" ,    "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162400/",   xSection=0.2043)
TTWToLNu_CP5.normalization = 1113150.39282
TTWToQQ             = Sample.fromDirectory("TTWToQQ",          "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162431/",         xSection=0.40620)
TTWToQQ.normalization = 209107.004815
TTW_LO              = Sample.fromDirectory("TTW_LO",            "/eos/vbc/experiments/cms/store/user/prhussai/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v4_privateUL16nanov9/220415_110022/",  xSection=0.6105)
TTW_LO.normalization = 14396003.0 
TTZ_LO              = Sample.fromDirectory("TTZ_LO",            "/eos/vbc/experiments/cms/store/user/prhussai/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v4_privateUL16nanov9/220415_110043/",                                   xSection=0.5297/0.692)
TTZ_LO.normalization = 14329456.0
TTGJets             = Sample.fromDirectory("TTGJets",          "/eos/vbc/experiments/cms/store/user/prhussai/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162341/",             xSection=3.697)
TTGJets.normalization = 8868805.09113

TTV = [TTWToLNu_CP5, TTWToQQ , TTW_LO, TTZ_LO, TTGJets,]

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
WW                  = Sample.fromDirectory("WW",               "/eos/vbc/experiments/cms/store/user/prhussai/WW_TuneCP5_13TeV-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220302_220700/", 			xSection=63.21 * 1.82)
WW.normalization = 15170130.6853 

ZZTo2L2Nu           = Sample.fromDirectory("ZZTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161709/",                     xSection=0.564)
ZZTo2L2Nu.normalization = 15509971.4162

#ZZTo2L2Q            = Sample.fromDirectory("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_powheg_pythia8/",                           xSection=3.28)
#ZZTo2Q2Nu           = Sample.fromDirectory("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=4.04)
ZZTo4L              = Sample.fromDirectory("ZZTo4L",               "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo4L_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220415_105959/",                             xSection=1.256*1.1)
ZZTo4L.normalization = 69074570.0288 

#WZTo1L3Nu           = Sample.fromDirectory("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.fromDirectory("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/",          xSection=10.71)
#WZTo2L2Q            = Sample.fromDirectory("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/",             xSection=5.60)
#WZTo3LNu            = Sample.fromDirectory("WZTo3LNu",             "/WZTo3LNu",         xSection=4.42965)
WZTo3LNu_amcatnlo   = Sample.fromDirectory("WZTo3LNu_amcatnlo",    "/eos/vbc/experiments/cms/store/user/prhussai/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161649/",        xSection=4.666)
WZTo3LNu_amcatnlo.normalization = 88368496.8435


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

WJetsToLNu        = Sample.fromDirectory("WJetsToLNu",        "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211215_222823/",        xSection=3* 20508.9)
WJetsToLNu.normalization = 9.91323628305e+12 

## HT-binned
WJetsToLNu_HT70to100        = Sample.fromDirectory("WJetsToLNu_HT70to100",        "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_154006/",        xSection=1637.13)
WJetsToLNu_HT70to100.normalization = 19439931.0 
WJetsToLNu_HT100to200       = Sample.fromDirectory("WJetsToLNu_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161210/",       xSection=1627.45)
WJetsToLNu_HT100to200.normalization = 19753958.0
WJetsToLNu_HT200to400       = Sample.fromDirectory("WJetsToLNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161240/",       xSection=435.237)
WJetsToLNu_HT200to400.normalization = 15067621.0
WJetsToLNu_HT400to600       = Sample.fromDirectory("WJetsToLNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161258/",       xSection=59.1811)
WJetsToLNu_HT400to600.normalization = 2115509.0
WJetsToLNu_HT600to800       = Sample.fromDirectory("WJetsToLNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161319/",       xSection=14.5805)
WJetsToLNu_HT600to800.normalization = 2251807.0
WJetsToLNu_HT800to1200      = Sample.fromDirectory("WJetsToLNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161338/",      xSection=6.65621)
WJetsToLNu_HT800to1200.normalization = 2132228.0
WJetsToLNu_HT1200to2500     = Sample.fromDirectory("WJetsToLNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_161357/", 	xSection=1.60809)
WJetsToLNu_HT1200to2500.normalization = 2090561.0
WJetsToLNu_HT2500toInf      = Sample.fromDirectory("WJetsToLNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161416/",     xSection=0.0389136)
WJetsToLNu_HT2500toInf.normalization = 709514.0


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

wjets = [ WJetsToLNu ] + wjets_ht


signals = [
    ]



### QCD

## QCD HT bins (cross sections from McM)
QCD_HT50to100        = Sample.fromDirectory("QCD_HT50to100",        "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211126_144127/",           xSection=246400000.0)
QCD_HT50to100.normalization = 11197186.0 
QCD_HT100to200       = Sample.fromDirectory("QCD_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162451/",          xSection=27850000.0)
QCD_HT100to200.normalization = 73506112.0
QCD_HT100to200_madgraph       = Sample.fromDirectory("QCD_HT100to200_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220302_220719/",          xSection=27850000.0)
QCD_HT100to200_madgraph.normalization = 18623294.0 
QCD_HT200to300       = Sample.fromDirectory("QCD_HT200to300",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162510/",          xSection=1717000)
QCD_HT200to300.normalization = 43280518.0
QCD_HT200to300_madgraph       = Sample.fromDirectory("QCD_HT200to300_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211126_144148/",          xSection=1717000)
QCD_HT200to300_madgraph.normalization = 17569141.0
QCD_HT300to500       = Sample.fromDirectory("QCD_HT300to500",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211126_144209/",          xSection=351300)
QCD_HT300to500.normalization = 16747056.0 
QCD_HT300to500_madgraph       = Sample.fromDirectory("QCD_HT300to500_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211126_144209/",          xSection=351300)
QCD_HT300to500_madgraph.normalization = 16747056.0
QCD_HT500to700_madgraph       = Sample.fromDirectory("QCD_HT500to700_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211126_144231/",          xSection=31630)
QCD_HT500to700_madgraph.normalization = 15222746.0
QCD_HT700to1000_madgraph      = Sample.fromDirectory("QCD_HT700to1000_madgraph",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220302_220801/",         xSection=6802)
QCD_HT700to1000_madgraph.normalization = 13398972.0 
QCD_HT1000to1500     = Sample.fromDirectory("QCD_HT1000to1500",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162529/",        xSection=1206)
QCD_HT1000to1500.normalization = 12675816.0
QCD_HT1000to1500_madgraph     = Sample.fromDirectory("QCD_HT1000to1500_madgraph",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220302_220821/",        xSection=1206)
QCD_HT1000to1500_madgraph.normalization = 4315050.0  
QCD_HT1500to2000     = Sample.fromDirectory("QCD_HT1500to2000",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162549/",        xSection=120.4)
QCD_HT1500to2000.normalization = 9376965.0
QCD_HT1500to2000_madgraph     = Sample.fromDirectory("QCD_HT1500to2000_madgraph",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/220302_220844/",        xSection=120.4)
QCD_HT1500to2000_madgraph.normalization = 3217830.0 
QCD_HT2000toInf      = Sample.fromDirectory("QCD_HT2000toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211124_162609/",         xSection=25.25)
QCD_HT2000toInf.normalization = 4867995.0
QCD_HT2000toInf_madgraph      = Sample.fromDirectory("QCD_HT2000toInf_madgraph",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v1_privateUL16nanov9/211126_144250/",         xSection=25.25)
QCD_HT2000toInf_madgraph.normalization = 1847781.0

QCD_HT = [
    QCD_HT50to100,
    QCD_HT100to200,
    QCD_HT100to200_madgraph,
    QCD_HT200to300,
    QCD_HT200to300_madgraph,
    QCD_HT300to500,
    QCD_HT300to500_madgraph,
    QCD_HT500to700_madgraph,
    QCD_HT700to1000_madgraph,
#    QCD_HT700to1000,
    QCD_HT1000to1500,
    QCD_HT1000to1500_madgraph,
    QCD_HT1500to2000,
    QCD_HT1500to2000_madgraph,
    QCD_HT2000toInf,
    QCD_HT2000toInf_madgraph,
    ]
SMS_T2tt_mStop_500_mLSP_420      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_420",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_223031/",         xSection=1.)
SMS_T2tt_mStop_500_mLSP_420.normalization = 484134.0 
SMS_T2tt_mStop_500_mLSP_450      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_450",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-450_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_221024/",         xSection=1.)
SMS_T2tt_mStop_500_mLSP_450.normalization = 493804.0 
SMS_T2tt_mStop_500_mLSP_470      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_470",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_221258/",         xSection=1.)
SMS_T2tt_mStop_500_mLSP_470.normalization = 482711.0 
SMS_T2tt_LL_mStop_400_mLSP_380      = Sample.fromDirectory("SMS_T2tt_LL_mStop_400_mLSP_380",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-400_mLSP-380_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_220945/",         xSection=1.)
SMS_T2tt_LL_mStop_400_mLSP_380.normalization = 259721.0
SMS_T2tt_LL_mStop_350_mLSP_335      = Sample.fromDirectory("SMS_T2tt_LL_mStop_350_mLSP_335",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-350_mLSP-335_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_220922/",         xSection=1.)
SMS_T2tt_LL_mStop_350_mLSP_335.normalization = 450603.0 
SMS_T2tt_LL_mStop_300_mLSP_290      = Sample.fromDirectory("SMS_T2tt_LL_mStop_300_mLSP_290",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt-4bd_genMET-100_genHT200_mStop-300_mLSP-290_TuneCP5_LLStop_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/220302_220903/",         xSection=1.)
SMS_T2tt_LL_mStop_300_mLSP_290.normalization = 415214.0 

#SMS_T2tt_dM_10to80          = Sample.nanoAODfromDAS("SMS_T2tt_dM_10to80", "/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/prhussai-crab_RunIISummer16MiniAODv3-PUSummer16v3Fast_94X_mcRun2_asymptotic_v3-v1_v0-23775f5a395d6e9cdb45e128e602f3b3/USER", dbFile=dbFile, redirector=redirector, instance="phys03", overwrite=ov, xSection=1.)
SMS_T2tt_dM_10to80          = Sample.fromDirectory("SMS_T2tt_dM_10to80", 	"/eos/vbc/experiments/cms/store/mc/RunIISummer16NanoAODv4/SMS-T2tt_dM-10to80_genHT-160_genMET-80_mWMin-0p1_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/NANOAODSIM/PUSummer16v3Fast_Nano14Dec2018_102X_mcRun2_asymptotic_v6-v1/120000/", 		 xSection=1.)
SMS_T2tt_dM_10to80.normalization = 42504047.0

compSUSY = [
		SMS_T2tt_mStop_500_mLSP_420,
		SMS_T2tt_mStop_500_mLSP_450,
		SMS_T2tt_mStop_500_mLSP_470,
		SMS_T2tt_LL_mStop_400_mLSP_380,
		SMS_T2tt_LL_mStop_350_mLSP_335,
		SMS_T2tt_LL_mStop_300_mLSP_290,
		SMS_T2tt_dM_10to80,
		]
allSamples = DY + top + boson + wjets + signals + QCD_HT + compSUSY 

for s in allSamples:
    
    s.isData = False
#    for i_f, f in enumerate(s.files):
#	    if f.startswith('/eos/'):
#		    s.files[i_f] = 'root://eos.grid.vbc.ac.at/'+f

