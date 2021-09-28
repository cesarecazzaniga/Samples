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
dbFile = dbDir+"DB_Run2016UL_miniAOD.sql"

logger.info("Using db file: %s", dbFile)

# MET
MET_Run2016B_ULHIPM_ver1  =   FWLiteSample.fromDAS("MET_Run2016B_ULHIPM_ver1",  "/MET/Run2016B-21Feb2020_ver1_UL2016_HIPM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016B_ULHIPM_ver2  =   FWLiteSample.fromDAS("MET_Run2016B_ULHIPM_ver2",  "/MET/Run2016B-21Feb2020_ver2_UL2016_HIPM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016C_ULHIPM       =   FWLiteSample.fromDAS("MET_Run2016C_ULHIPM",	"/MET/Run2016C-21Feb2020_UL2016_HIPM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016D_ULHIPM       =   FWLiteSample.fromDAS("MET_Run2016D_ULHIPM",   	"/MET/Run2016D-21Feb2020_UL2016_HIPM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016E_ULHIPM       =   FWLiteSample.fromDAS("MET_Run2016E_ULHIPM",   	"/MET/Run2016E-21Feb2020_UL2016_HIPM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016F_UL       	  =   FWLiteSample.fromDAS("MET_Run2016F_UL",	    	"/MET/Run2016F-21Feb2020_UL2016-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016F_ULHIPM  	  =   FWLiteSample.fromDAS("MET_Run2016F_ULHIPM",   	"/MET/Run2016F-21Feb2020_UL2016_HIPM-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016G_UL       	  =   FWLiteSample.fromDAS("MET_Run2016G_UL",	    	"/MET/Run2016G-21Feb2020_UL2016-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2016H_UL       	  =   FWLiteSample.fromDAS("MET_Run2016H_UL",	    	"/MET/Run2016H-21Feb2020_UL2016-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2016B_ULHIPM_ver1,
    MET_Run2016B_ULHIPM_ver2,
    MET_Run2016C_ULHIPM,
    MET_Run2016D_ULHIPM,
    MET_Run2016E_ULHIPM,
    MET_Run2016F_UL,
    MET_Run2016F_ULHIPM,
    MET_Run2016G_UL,
    MET_Run2016H_UL,
]
## add up all samples
allSamples = MET

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
