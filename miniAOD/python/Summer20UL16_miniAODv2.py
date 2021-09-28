'''
miniAOD samples of Summer20UL16 campaign, miniAODv2 (106X)
Get the full list of samples with
dasgoclient -query="dataset=/*/RunIISummer20UL16MiniAODv2*106X*/MINIAODSIM"
'''
                                                                                                                                                                                                            
import copy, os, sys
from RootTools.fwlite.FWLiteSample import FWLiteSample
import ROOT

def get_parser():
	import argparse
	argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
	argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
	return argParser

# Logging
if __name__=="__main__":
	import Samples.Tools.logger as logger
	logger = logger.get_logger("INFO", logFile = None )
	import RootTools.core.logger as logger_rt
	logger_rt = logger_rt.get_logger("INFO", logFile = None )
	options = get_parser().parse_args()
	ov = options.overwrite

else:
	import logging
	logger = logging.getLogger(__name__)
	ov = False

from Samples.Tools.config import dbDir, redirector, redirector_global
dbFile = dbDir+"Summer20UL16_miniAODv2.sql"

logger.info("Using db file: %s", dbFile)


##WJets_HT
WJetsToLNu_HT70To100             = FWLiteSample.fromDAS("WJetsToLNu_HT70To100", "/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT100To200            = FWLiteSample.fromDAS("WJetsToLNu_HT100To200", "/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT200To400            = FWLiteSample.fromDAS("WJetsToLNu_HT200To400", "/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT400To600            = FWLiteSample.fromDAS("WJetsToLNu_HT400To600", "/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT600To800            = FWLiteSample.fromDAS("WJetsToLNu_HT600To800", "/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT800To1200           = FWLiteSample.fromDAS("WJetsToLNu_HT800To1200", "/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT1200To2500          = FWLiteSample.fromDAS("WJetsToLNu_HT1200To2500", "/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WJetsToLNu_HT2500ToInf           = FWLiteSample.fromDAS("WJetsToLNu_HT2500ToInf", "/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

WJetsToLNu_HT = [
		WJetsToLNu_HT70To100,
		WJetsToLNu_HT100To200,
		WJetsToLNu_HT200To400,
		WJetsToLNu_HT400To600,
		WJetsToLNu_HT600To800,
		WJetsToLNu_HT800To1200,
		WJetsToLNu_HT1200To2500,
		WJetsToLNu_HT2500ToInf,
]
##TTJets
TTLep_pow			= FWLiteSample.fromDAS("TTLep_pow", "/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTSingleLep_pow			= FWLiteSample.fromDAS("TTSingleLep_pow", "/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
TTJets = [ TTLep_pow, TTSingleLep_pow ]

##ZInv
ZJetsToNuNu_HT-100To200		= FWLiteSample.fromDAS("ZJetsToNuNu_HT-100To200", "/ZJetsToNuNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT-200To400		= FWLiteSample.fromDAS("ZJetsToNuNu_HT-200To400", "/ZJetsToNuNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT-400To600		= FWLiteSample.fromDAS("ZJetsToNuNu_HT-400To600", "/ZJetsToNuNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT-600To800		= FWLiteSample.fromDAS("ZJetsToNuNu_HT-600To800", "/ZJetsToNuNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT-800To1200	= FWLiteSample.fromDAS("ZJetsToNuNu_HT-800To1200", "/ZJetsToNuNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZJetsToNuNu_HT-1200To2500	= FWLiteSample.fromDAS("ZJetsToNuNu_HT-1200To2500", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ZJetsToNuNu_HT-2500ToInf	= FWLiteSample.fromDAS("ZJetsToNuNu_HT-2500ToInf", "/ZJetsToNuNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v3/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZJetsToNuNu = [
		ZJetsToNuNu_HT-100To200,
		ZJetsToNuNu_HT-200To400,
		ZJetsToNuNu_HT-400To600,
		ZJetsToNuNu_HT-600To800,
		ZJetsToNuNu_HT-800To1200,
		#ZJetsToNuNu_HT-1200To2500,
		ZJetsToNuNu_HT-2500ToInf,
		]

##DiBoson
WWTo2L2Nu		= FWLiteSample.fromDAS("WWTo2L2Nu", "/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WWToLNuQQ		= FWLiteSample.fromDAS("WWToLNuQQ", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

#WZTo1LNu2Q_NLO		= FWLiteSample.fromDAS("WZTo1LNu2Q_NLO", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WZTo1L3Nu_NLO		= FWLiteSample.fromDAS("WZTo1L3Nu_NLO", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#WZTo2L2Q_NLO		= FWLiteSample.fromDAS("WZTo2L2Q_NLO", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
WZTo3LNu_NLO		= FWLiteSample.fromDAS("WZTo3LNu_NLO", "/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

ZZTo2L2Nu		= FWLiteSample.fromDAS("ZZTo2L2Nu", "/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo2L2Q		= FWLiteSample.fromDAS("ZZTo2L2Q", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo2Q2Nu		= FWLiteSample.fromDAS("ZZTo2Q2Nu", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ZZTo4L			= FWLiteSample.fromDAS("ZZTo4L", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

diBoson = [
	   WWTo2L2Nu,
	   #WWToLNuQQ,
	   #WZTo1LNu2Q_NLO,
	   #WZTo1L3Nu_NLO,
	   #WZTo2L2Q_NLO,
	   WZTo3LNu_NLO,
	   ZZTo2L2Nu,
	   #ZZTo2L2Q,
	   #ZZTo2Q2Nu,
	   #ZZTo4L,
	   ]

##DY
#DYJetsToLL_M5to50_HT100to200		= FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT100to200", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M5to50_HT200to400		= FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT200to400", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M5to50_HT400to600		= FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT400to600", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M5to50_HT600toInf		= FWLiteSample.fromDAS("DYJetsToLL_M5to50_HT600toInf", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)


DYJetsToLL_M50_HT70to100		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT70to100", "/DYJetsToLL_M-50_HT-70to100_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT100to200		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT100to200", "/DYJetsToLL_M-50_HT-100to200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M50_HT200to400		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT200to400", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT400to600		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT400to600", "/DYJetsToLL_M-50_HT-400to600_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M50_HT600to800		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT600to800", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
DYJetsToLL_M50_HT800to1200		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT800to1200", "/DYJetsToLL_M-50_HT-800to1200_TuneCP5_PSweights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M50_HT1200to2500		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT1200to2500", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#DYJetsToLL_M50_HT2500toInf		= FWLiteSample.fromDAS("DYJetsToLL_M50_HT2500toInf", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

DY_HT= [
	#DYJetsToLL_M5to50_HT100to200,
	#DYJetsToLL_M5to50_HT200to400,
	#DYJetsToLL_M5to50_HT400to600,
	#DYJetsToLL_M5to50_HT600toInf,

	DYJetsToLL_M50_HT70to100,
	DYJetsToLL_M50_HT100to200,
	#DYJetsToLL_M50_HT200to400,
	DYJetsToLL_M50_HT400to600,
	#DYJetsToLL_M50_HT600to800,
	DYJetsToLL_M50_HT800to1200,
	#DYJetsToLL_M50_HT1200to2500,
	#DYJetsToLL_M50_HT2500toInf,
	]

##singleTop
#ST_tchannel_top_4f_pow		= FWLiteSample.fromDAS("ST_tchannel_top_4f_pow", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ST_tchannel_antitop_4f_pow	= FWLiteSample.fromDAS("ST_tchannel_antitop_4f_pow", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_top_NoFullyHad_5f_pow 	= FWLiteSample.fromDAS("ST_tW_top_NoFullyHad_5f_pow", "/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ST_tW_antitop_NoFullyHad_5f_pow = FWLiteSample.fromDAS("ST_tW_antitop_NoFullyHad_5f_pow", "/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

singleTop = [
	     #ST_tchannel_top_4f_pow,
	     #ST_tchannel_antitop_4f_pow,
	     ST_tW_top_NoFullyHad_5f_pow,
	     ST_tW_antitop_NoFullyHad_5f_pow,
		]

##ttX
TTGJets_NLO			= FWLiteSample.fromDAS("TTGJets_NLO", "/TTGJets_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttWJetsToLNu_NLO		= FWLiteSample.fromDAS("ttWJetsToLNu_NLO", "/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttWJetsToQQ_NLO			= FWLiteSample.fromDAS("ttWJetsToQQ_NLO", "/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v2/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ttWJets_LO			= FWLiteSample.fromDAS("ttWJets_LO", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
#ttZJets_LO			= FWLiteSample.fromDAS("ttZJets_LO", "", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
ttX = [TTGJets_NLO, ttWJetsToLNu_NLO, ttWJetsToQQ_NLO, #ttWJets_LO, #ttZJets_LO, ]

##QCD
QCD_HT50to100			= FWLiteSample.fromDAS("QCD_HT50to100", "/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT100to200			= FWLiteSample.fromDAS("QCD_HT100to200", "/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT200to300			= FWLiteSample.fromDAS("QCD_HT200to300", "/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT300to500			= FWLiteSample.fromDAS("QCD_HT300to500", "/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT500to700			= FWLiteSample.fromDAS("QCD_HT500to700", "/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT700to1000			= FWLiteSample.fromDAS("QCD_HT700to1000", "/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT1000to1500		= FWLiteSample.fromDAS("QCD_HT1000to1500", "/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT1500to2000		= FWLiteSample.fromDAS("QCD_HT1500to2000", "/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
QCD_HT2000toInf			= FWLiteSample.fromDAS("QCD_HT2000toInf", "/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

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

allSamples = WJetsToLNu_HT + TTJets + ZJetsToNuNu + diBoson + DY_HT + singleTop + ttX + QCD_HT   

for sample in allSamples:
	sample.isData = False

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )

