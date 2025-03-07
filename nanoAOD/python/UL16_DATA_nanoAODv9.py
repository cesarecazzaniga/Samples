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
try:
    redirector = sys.modules['__main__'].redirector
except:
    if "clip" in os.getenv("HOSTNAME").lower():
        if __name__ == "__main__" and not options.check_completeness:
            from Samples.Tools.config import redirector_global as redirector
        else:
            #from Samples.Tools.config import redirector_clip_local as redirector
            from Samples.Tools.config import redirector_global as redirector
    else:
        from Samples.Tools.config import redirector as redirector
# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_UL16_DATA_nanoAODv9.sql'

logger.info("Using db file: %s", dbFile)

################################################################################
# Single Muon
SingleMuon_Run2016F             = Sample.nanoAODfromDAS("SingleMuon_Run2016F",            "/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016G             = Sample.nanoAODfromDAS("SingleMuon_Run2016G",            "/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016H             = Sample.nanoAODfromDAS("SingleMuon_Run2016H",            "/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleMuon_Run2016 = [SingleMuon_Run2016F, SingleMuon_Run2016G, SingleMuon_Run2016H]

################################################################################
# SingleElectron
SingleElectron_Run2016F             = Sample.nanoAODfromDAS("SingleElectron_Run2016F",            "/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016G             = Sample.nanoAODfromDAS("SingleElectron_Run2016G",            "/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016H             = Sample.nanoAODfromDAS("SingleElectron_Run2016H",            "/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
SingleElectron_Run2016 = [SingleElectron_Run2016F, SingleElectron_Run2016G, SingleElectron_Run2016H]

################################################################################
# Double Muon
DoubleMuon_Run2016F             = Sample.nanoAODfromDAS("DoubleMuon_Run2016F",            "/DoubleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016G             = Sample.nanoAODfromDAS("DoubleMuon_Run2016G",            "/DoubleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016H             = Sample.nanoAODfromDAS("DoubleMuon_Run2016H",            "/DoubleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleMuon_Run2016 = [DoubleMuon_Run2016F, DoubleMuon_Run2016G, DoubleMuon_Run2016H]

################################################################################
# Double EG
DoubleEG_Run2016F             = Sample.nanoAODfromDAS("DoubleEG_Run2016F",            "/DoubleEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016G             = Sample.nanoAODfromDAS("DoubleEG_Run2016G",            "/DoubleEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016H             = Sample.nanoAODfromDAS("DoubleEG_Run2016H",            "/DoubleEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
DoubleEG_Run2016 = [DoubleEG_Run2016F, DoubleEG_Run2016G, DoubleEG_Run2016H]

################################################################################
# MuonEG
MuonEG_Run2016F             = Sample.nanoAODfromDAS("MuonEG_Run2016F",            "/MuonEG/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016G             = Sample.nanoAODfromDAS("MuonEG_Run2016G",            "/MuonEG/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016H             = Sample.nanoAODfromDAS("MuonEG_Run2016H",            "/MuonEG/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD", dbFile=dbFile, overwrite=ov, redirector=redirector)
MuonEG_Run2016 = [MuonEG_Run2016F, MuonEG_Run2016G, MuonEG_Run2016H]

################################################################################

allSamples = SingleMuon_Run2016 + SingleElectron_Run2016 + DoubleMuon_Run2016 + DoubleEG_Run2016 + MuonEG_Run2016

for s in allSamples:
    s.isData = True
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 )
