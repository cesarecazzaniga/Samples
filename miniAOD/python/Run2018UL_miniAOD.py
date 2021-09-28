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
dbFile = dbDir+"DB_Run2018UL_miniAOD.sql"

logger.info("Using db file: %s", dbFile)

# MET
MET_Run2018A_UL  =   FWLiteSample.fromDAS("MET_Run2018A_UL",  "/MET/Run2018A-12Nov2019_UL2018-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018B_UL  =   FWLiteSample.fromDAS("MET_Run2018B_UL",  "/MET/Run2018B-12Nov2019_UL2018-v3/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018C_UL  =   FWLiteSample.fromDAS("MET_Run2018C_UL",  "/MET/Run2018C-12Nov2019_UL2018_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2018D_UL  =   FWLiteSample.fromDAS("MET_Run2018D_UL",  "/MET/Run2018D-12Nov2019_UL2018_rsb-v2/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2018A_UL,
    MET_Run2018B_UL,
    MET_Run2018C_UL,
    MET_Run2018D_UL,
]
## add up all samples
allSamples = MET

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
