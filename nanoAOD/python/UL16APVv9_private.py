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

DYJetsToLL_M50_HT70to100      =   Sample.fromDirectory("DYJetsToLL_M50_HT70to100",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194357/",	 xSection=169.9*1.23)
DYJetsToLL_M50_HT70to100.normalization    = 6724232.0 
DYJetsToLL_M50_HT100to200     =   Sample.fromDirectory("DYJetsToLL_M50_HT100to200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194432/",	 xSection=147.4*1.23)
DYJetsToLL_M50_HT100to200.normalization   = 9570042.0
DYJetsToLL_M50_HT200to400     =   Sample.fromDirectory("DYJetsToLL_M50_HT200to400",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-200to400_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194457/",	xSection=40.99*1.23)
DYJetsToLL_M50_HT200to400.normalization   = 5862631.0
DYJetsToLL_M50_HT400to600     =   Sample.fromDirectory("DYJetsToLL_M50_HT400to600",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161824/",	xSection=5.678*1.23)
DYJetsToLL_M50_HT400to600.normalization   = 2491416.0 
DYJetsToLL_M50_HT600to800     =   Sample.fromDirectory("DYJetsToLL_M50_HT600to800",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-600to800_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194519/",	xSection=1.367*1.23 )
DYJetsToLL_M50_HT600to800.normalization   = 2681650.0
DYJetsToLL_M50_HT800to1200    =   Sample.fromDirectory("DYJetsToLL_M50_HT800to1200",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194543/",	xSection=0.6304*1.23 )
DYJetsToLL_M50_HT800to1200.normalization  = 2411091.0
DYJetsToLL_M50_HT1200to2500   =   Sample.fromDirectory("DYJetsToLL_M50_HT1200to2500",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-1200to2500_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODv2-106X_mcRun2_asymptotic_v17-v2_privateUL16nanov9/211124_161919/",	xSection=0.1514*1.23 )
DYJetsToLL_M50_HT1200to2500.normalization = 1970857.0 
DYJetsToLL_M50_HT2500toInf    =   Sample.fromDirectory("DYJetsToLL_M50_HT2500toInf",	"/eos/vbc/experiments/cms/store/user/prhussai/DYJetsToLL_M-50_HT-2500toInf_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194609/",	xSection=0.003565*1.23 )
DYJetsToLL_M50_HT2500toInf.normalization  = 721404.0
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
DYJetsToNuNu_HT100to200       = Sample.fromDirectory("DYJetsToNuNu_HT100to200",	      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194033/",	       xSection=280.35*1.23)
DYJetsToNuNu_HT100to200.normalization   = 7784090.0 
DYJetsToNuNu_HT200to400       = Sample.fromDirectory("DYJetsToNuNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194055/",         xSection=77.67*1.23)
DYJetsToNuNu_HT200to400.normalization   =  7531529.0
DYJetsToNuNu_HT400to600       = Sample.fromDirectory("DYJetsToNuNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194119/0000/",         xSection=10.73*1.23)
DYJetsToNuNu_HT400to600.normalization   = 6632524.0
DYJetsToNuNu_HT600to800       = Sample.fromDirectory("DYJetsToNuNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194141/",         xSection=2.559*1.23)
DYJetsToNuNu_HT600to800.normalization   = 2030858.0
DYJetsToNuNu_HT800to1200      = Sample.fromDirectory("DYJetsToNuNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194203/",         xSection=1.1796*1.23)
DYJetsToNuNu_HT800to1200.normalization  = 703970.0
DYJetsToNuNu_HT1200to2500     = Sample.fromDirectory("DYJetsToNuNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194228/",         xSection=0.28833*1.23)
DYJetsToNuNu_HT1200to2500.normalization = 136393.0
DYJetsToNuNu_HT2500toInf      = Sample.fromDirectory("DYJetsToNuNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194249/",         xSection=0.006945*1.23)
DYJetsToNuNu_HT2500toInf.normalization  = 111838.0

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

# ttbar
TTLep_pow_CP5       = Sample.fromDirectory("TTLep_pow_CP5",            "/eos/vbc/experiments/cms/store/user/prhussai/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193642/",            xSection=831.762*((3*0.108)**2))
TTLep_pow_CP5.normalization = 2704527656.16 
TTSingleLep_pow_CP5 = Sample.fromDirectory("TTSingleLep_pow_CP5",      "/eos/vbc/experiments/cms/store/user/prhussai/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193732/",            xSection=831.762*(3*0.108)*(1-3*0.108)*2)
TTSingleLep_pow_CP5.normalization =  39645902747.0
#TTbar               = Sample.fromDirectory("TTbar",                "",        xSection=831.762)
#TTJets_amcatnlo     = Sample.fromDirectory("TTJets_amcatnlo",                "",        xSection=831.762)

# single top
T_tch_pow           = Sample.fromDirectory("T_tch_pow",        "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3_privateUL16nanoAPVv9/211124_194631/",         xSection=136.02) 
T_tch_pow.normalization     = 5948135153.64 
TBar_tch_pow        = Sample.fromDirectory("TBar_tch_pow",     "/eos/vbc/experiments/cms/store/user/prhussai/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v3_privateUL16nanoAPVv9/211124_194653/",     xSection=80.95)
TBar_tch_pow.normalization  = 1983864432.8

T_tWch_ext          = Sample.fromDirectory("T_tWch_ext",       "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194739/",         xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
T_tWch_ext.normalization    = 106897143.0
TBar_tWch_ext       = Sample.fromDirectory("TBar_tWch_ext",    "/eos/vbc/experiments/cms/store/user/prhussai/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194717/",     xSection=35.85*(1.-(1.-0.108*3)*(1.-0.108*3)) ) #xsec analyzer is wrong and does not take decay modes into account https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec#Single_top_Wt_channel_cross_sect
TBar_tWch_ext.normalization = 103260113.117

# ttV
TTWToLNu_CP5        = Sample.fromDirectory("TTWToLNu_CP5" ,    "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194828/",   xSection=0.2043)
TTWToLNu_CP5.normalization = 953960.42239 
TTWToQQ             = Sample.fromDirectory("TTWToQQ",          "/eos/vbc/experiments/cms/store/user/prhussai/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_213902/",         xSection=0.40620)
TTWToQQ.normalization	= 176057.27827 
TTZ_LO              = Sample.fromDirectory("TTZ_LO",           "/eos/vbc/experiments/cms/store/user/prhussai/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_214154/",                                   xSection=0.5297/0.692)
TTZ_LO.normalization  = 14435482.0 
TTW_LO              = Sample.fromDirectory("TTW_LO",            "/eos/vbc/experiments/cms/store/user/prhussai/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_214131/",  xSection=0.6105)
TTW_LO.normalization = 14118554.0  

TTGJets             = Sample.fromDirectory("TTGJets",          "/eos/vbc/experiments/cms/store/user/prhussai/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194801/",             xSection=3.697)
TTGJets.normalization  = 9472781.7663

TTV = [TTWToLNu_CP5, TTWToQQ, TTZ_LO, TTW_LO, TTGJets]

top = [
   
    #TTbar,
   TTLep_pow_CP5,
   TTSingleLep_pow_CP5,
   T_tch_pow,
   TBar_tch_pow,
   T_tWch_ext,
   TBar_tWch_ext,
   ] + TTV 

# di/multiboson
WWTo2L2Nu           = Sample.fromDirectory("WWTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194311/",   xSection=12.178)
WWTo2L2Nu.normalization = 33456497.8642 
#WWToLNuQQ           = Sample.fromDirectory("WWToLNuQQ",        "/WWToLNuQQ_13TeV-powheg/",         xSection=49.997)
WW                  = Sample.fromDirectory("WW",               "/eos/vbc/experiments/cms/store/user/prhussai/WW_TuneCP5_13TeV-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_211401/",                  xSection=63.21 * 1.82)
WW.normalization = 13938114.1561 


ZZTo2L2Nu           = Sample.fromDirectory("ZZTo2L2Nu",        "/eos/vbc/experiments/cms/store/user/prhussai/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194335/",                     xSection=0.564)
ZZTo2L2Nu.normalization = 16317441.3612

#ZZTo2L2Q            = Sample.fromDirectory("ZZTo2L2Q",             "/ZZTo2L2Q_13TeV_powheg_pythia8/",                           xSection=3.28)
#ZZTo2Q2Nu           = Sample.fromDirectory("ZZTo2Q2Nu",            "/ZZTo2Q2Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=4.04)
#ZZTo4L              = Sample.fromDirectory("ZZTo4L",               "/ZZTo4L_13TeV_powheg_pythia8/",                             xSection=1.256*1.1)
#
#WZTo1L3Nu           = Sample.fromDirectory("WZTo1L3Nu"  ,          "/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/",            xSection=(47.13)*(3*0.108)*(0.2) )
#WZTo1L1Nu2Q         = Sample.fromDirectory("WZTo1L1Nu2Q",          "/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/",          xSection=10.71)
#WZTo2L2Q            = Sample.fromDirectory("WZTo2L2Q"   ,          "/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/",             xSection=5.60)
#WZTo3LNu            = Sample.fromDirectory("WZTo3LNu",             "/WZTo3LNu",         xSection=4.42965)
#WZTo3LNu_amcatnlo   = Sample.fromDirectory("WZTo3LNu_amcatnlo",    "/eos/vbc/experiments/cms/store/user/prhussai/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/",        xSection=4.666)
#WZTo3LNu_amcatnlo.normalization = 88368496.8435


boson = [
   WWTo2L2Nu,
    #WWToLNuQQ,
    WW,
   ZZTo2L2Nu,
    #ZZTo2L2Q,
    #ZZTo2Q2Nu,
    #ZZTo4L,
    #WZTo1L3Nu,
    #WZTo1L1Nu2Q,
    #WZTo2L2Q,
    #WZTo3LNu,
#    WZTo3LNu_amcatnlo,
   ]


# HT-binned
#WJetsToLNu_HT70to100        = Sample.fromDirectory("WJetsToLNu_HT70to100",        "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/",        xSection=1637.13)
#WJetsToLNu_HT70to100.normalization    =  
WJetsToLNu_HT100to200       = Sample.fromDirectory("WJetsToLNu_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193757/",       xSection=1627.45)
WJetsToLNu_HT100to200.normalization   = 21734530.0
WJetsToLNu_HT200to400       = Sample.fromDirectory("WJetsToLNu_HT200to400",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193819/",       xSection=435.237)
WJetsToLNu_HT200to400.normalization   = 17870845.0 
WJetsToLNu_HT400to600       = Sample.fromDirectory("WJetsToLNu_HT400to600",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193841/",       xSection=59.1811)
WJetsToLNu_HT400to600.normalization   = 2467498.0
WJetsToLNu_HT600to800       = Sample.fromDirectory("WJetsToLNu_HT600to800",       "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193905/",       xSection=14.5805)
WJetsToLNu_HT600to800.normalization   = 2344130.0 
WJetsToLNu_HT800to1200      = Sample.fromDirectory("WJetsToLNu_HT800to1200",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193925/",      xSection=6.65621)
WJetsToLNu_HT800to1200.normalization  = 2510487.0
WJetsToLNu_HT1200to2500     = Sample.fromDirectory("WJetsToLNu_HT1200to2500",     "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_193948/", xSection=1.60809)
WJetsToLNu_HT1200to2500.normalization = 2119975.0
WJetsToLNu_HT2500toInf      = Sample.fromDirectory("WJetsToLNu_HT2500toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/211124_194012/",     xSection=0.0389136)
WJetsToLNu_HT2500toInf.normalization  = 808649.0


wjets_ht = [
   #WJetsToLNu_HT70to100,
   WJetsToLNu_HT100to200,
   WJetsToLNu_HT200to400,
   WJetsToLNu_HT400to600,
   WJetsToLNu_HT600to800,
   WJetsToLNu_HT800to1200,
   WJetsToLNu_HT1200to2500,
   WJetsToLNu_HT2500toInf,
   ]

#wjets += wjets_ht


# QCD

# QCD HT bins (cross sections from McM)
QCD_HT50to100		       = Sample.fromDirectory("QCD_HT50to100",        "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214212/",           xSection=246400000.0)
QCD_HT50to100.normalization = 35648181.0 
QCD_HT50to100_madgraph        = Sample.fromDirectory("QCD_HT50to100_madgraph",        "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214230/",           xSection=246400000.0)
QCD_HT50to100_madgraph.normalization = 11207944.0 
QCD_HT100to200       = Sample.fromDirectory("QCD_HT100to200",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194912/",          xSection=27850000.0)
QCD_HT100to200.normalization = 67431856.0 
QCD_HT100to200_madgraph       = Sample.fromDirectory("QCD_HT100to200_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214250/",          xSection=27850000.0)
QCD_HT100to200_madgraph.normalization = 27998051.0 
#QCD_HT200to300       = Sample.fromDirectory("QCD_HT200to300",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/",          xSection=1717000)
#QCD_HT200to300.normalization = 
QCD_HT200to300_madgraph       = Sample.fromDirectory("QCD_HT200to300_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214310/",          xSection=1717000)
QCD_HT200to300_madgraph.normalization = 18273591.0 
QCD_HT300to500       = Sample.fromDirectory("QCD_HT300to500",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_214328/",          xSection=351300)
QCD_HT300to500.normalization = 45351614.8303 
QCD_HT300to500_madgraph       = Sample.fromDirectory("QCD_HT300to500_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214347/",          xSection=351300)
QCD_HT300to500_madgraph.normalization = 15341307.0 
QCD_HT500to700       = Sample.fromDirectory("QCD_HT500to700",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194850/",          xSection=31630)
QCD_HT500to700.normalization = 56610815.0 
QCD_HT500to700_madgraph       = Sample.fromDirectory("QCD_HT500to700_madgraph",       "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214407/",          xSection=31630)
QCD_HT500to700_madgraph.normalization = 13515126.0 
QCD_HT700to1000      = Sample.fromDirectory("QCD_HT700to1000",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_214427/",         xSection=6802)
QCD_HT700to1000.normalization = 40442876.0 
QCD_HT700to1000_madgraph      = Sample.fromDirectory("QCD_HT700to1000_madgraph",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211126_144534/",         xSection=6802)
QCD_HT700to1000_madgraph.normalization = 15808790.0 
QCD_HT1000to1500_madgraph     = Sample.fromDirectory("QCD_HT1000to1500_madgraph",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211126_144553/",        xSection=1206)
QCD_HT1000to1500_madgraph.normalization = 4773503.0 
QCD_HT1000to1500     = Sample.fromDirectory("QCD_HT1000to1500",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_194939/0000/",        xSection=1206)
QCD_HT1000to1500.normalization = 13705620.0 
QCD_HT1500to2000     = Sample.fromDirectory("QCD_HT1500to2000",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_195001/",        xSection=120.4)
QCD_HT1500to2000.normalization = 10031077.0 
QCD_HT1500to2000_madgraph     = Sample.fromDirectory("QCD_HT1500to2000_madgraph",     "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211126_144612/",        xSection=120.4)
QCD_HT1500to2000_madgraph.normalization = 3503675.0 
QCD_HT2000toInf      = Sample.fromDirectory("QCD_HT2000toInf",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/211124_195023/",         xSection=25.25)
QCD_HT2000toInf.normalization = 4996082.0 
QCD_HT2000toInf_madgraph      = Sample.fromDirectory("QCD_HT2000toInf_madgraph",      "/eos/vbc/experiments/cms/store/user/prhussai/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1_privateUL16nanoAPVv9/220302_215207/",         xSection=25.25)
QCD_HT2000toInf_madgraph.normalization = 1629000.0 

QCD_HT = [
   QCD_HT50to100,
   QCD_HT50to100_madgraph,
   QCD_HT100to200,
   QCD_HT100to200_madgraph,
   #QCD_HT200to300,
   QCD_HT200to300_madgraph,
   QCD_HT300to500,
   QCD_HT300to500_madgraph,
   QCD_HT500to700,
   QCD_HT500to700_madgraph,
   QCD_HT700to1000,
   QCD_HT700to1000_madgraph,
   QCD_HT1000to1500,
   QCD_HT1000to1500_madgraph,
   QCD_HT1500to2000,
   QCD_HT1500to2000_madgraph,
   QCD_HT2000toInf,
   QCD_HT2000toInf_madgraph,
   ]

SMS_T2tt_mStop_500_mLSP_420      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_420",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-420_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_215225/",         xSection=1.)
SMS_T2tt_mStop_500_mLSP_420.normalization = 498791.0
SMS_T2tt_mStop_500_mLSP_450      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_450",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-450_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_215245/",         xSection=1.)
SMS_T2tt_mStop_500_mLSP_450.normalization = 458074.0
SMS_T2tt_mStop_500_mLSP_470      = Sample.fromDirectory("SMS_T2tt_mStop_500_mLSP_470",      "/eos/vbc/experiments/cms/store/user/prhussai/SMS-T2tt_genMET-100_genHT200_mStop-500_mLSP-470_TuneCP5_13TeV-madgraphMLM-pythia8/crab_RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2_privateUL16nanoAPVv9/220302_215308/",         xSection=1.)
SMS_T2tt_mStop_500_mLSP_470.normalization = 496407.0

compSUSY = [
		SMS_T2tt_mStop_500_mLSP_420,
		SMS_T2tt_mStop_500_mLSP_450,
		SMS_T2tt_mStop_500_mLSP_470,
		]

allSamples = DY + top + boson + wjets_ht + QCD_HT + compSUSY 

for s in allSamples:
    
    s.isData = False
    for i_f, f in enumerate(s.files):
	    if f.startswith('/eos/'):
		    s.files[i_f] = 'root://eos.grid.vbc.ac.at/'+f

