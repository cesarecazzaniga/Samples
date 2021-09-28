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
dbFile = dbDir+"DB_Run2017UL_miniAOD.sql"

logger.info("Using db file: %s", dbFile)

# MET
MET_Run2017A_UL  =   FWLiteSample.fromDAS("MET_Run2017A_UL",  "/MET/Run2017A-09Aug2019_UL2017_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017B_UL  =   FWLiteSample.fromDAS("MET_Run2017B_UL",  "/MET/Run2017B-09Aug2019_UL2017_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017C_UL  =   FWLiteSample.fromDAS("MET_Run2017C_UL",  "/MET/Run2017C-09Aug2019_UL2017_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017D_UL  =   FWLiteSample.fromDAS("MET_Run2017D_UL",  "/MET/Run2017D-09Aug2019_UL2017_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017E_UL  =   FWLiteSample.fromDAS("MET_Run2017E_UL",  "/MET/Run2017E-09Aug2019_UL2017_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)
MET_Run2017F_UL  =   FWLiteSample.fromDAS("MET_Run2017F_UL",  "/MET/Run2017F-09Aug2019_UL2017_rsb-v1/MINIAOD", dbFile=dbFile, overwrite=ov, prefix=redirector_global, skipCheck=True)

MET = [\
    MET_Run2017A_UL,
    MET_Run2017B_UL,
    MET_Run2017C_UL,
    MET_Run2017D_UL,
    MET_Run2017E_UL,
    MET_Run2017F_UL,
]
## add up all samples
allSamples = MET

for sample in allSamples:
    sample.isData = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
