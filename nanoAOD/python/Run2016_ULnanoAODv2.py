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
            from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB
from Samples.Tools.config import dbDir
dbFile = dbDir+'/DB_Run2016_ULnanoAODv2.sql'
logger.info("Using db file: %s", dbFile)

# DoubleMuon
DoubleMuon_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_ver1_UL",   "/DoubleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("DoubleMuon_Run2016B_ver2_UL",   "/DoubleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016C_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016C_UL",        "/DoubleMuon/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016D_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016D_UL",        "/DoubleMuon/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016E_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016E_UL",        "/DoubleMuon/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_HIPM_UL",   "/DoubleMuon/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016F_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016F_UL",        "/DoubleMuon/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016G_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016G_UL",        "/DoubleMuon/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleMuon_Run2016H_UL       = Sample.nanoAODfromDAS("DoubleMuon_Run2016H_UL",        "/DoubleMuon/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD",      dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleMuon = [
    DoubleMuon_Run2016B_ver1_UL,
    DoubleMuon_Run2016B_ver2_UL,
    DoubleMuon_Run2016C_UL,
    DoubleMuon_Run2016D_UL,
    DoubleMuon_Run2016E_UL,
    DoubleMuon_Run2016F_HIPM_UL,
    DoubleMuon_Run2016F_UL,
    DoubleMuon_Run2016G_UL,
    DoubleMuon_Run2016H_UL,
]

# MuonEG
MuonEG_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("MuonEG_Run2016B_ver1_UL",   "/MuonEG/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("MuonEG_Run2016B_ver2_UL",   "/MuonEG/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016C_UL       = Sample.nanoAODfromDAS("MuonEG_Run2016C_UL",        "/MuonEG/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016D_UL       = Sample.nanoAODfromDAS("MuonEG_Run2016D_UL",        "/MuonEG/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016E_UL       = Sample.nanoAODfromDAS("MuonEG_Run2016E_UL",        "/MuonEG/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("MuonEG_Run2016F_HIPM_UL",   "/MuonEG/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016F_UL       = Sample.nanoAODfromDAS("MuonEG_Run2016F_UL",        "/MuonEG/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016G_UL       = Sample.nanoAODfromDAS("MuonEG_Run2016G_UL",        "/MuonEG/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MuonEG_Run2016H_UL       = Sample.nanoAODfromDAS("MuonEG_Run2016H_UL",        "/MuonEG/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MuonEG = [
    MuonEG_Run2016Bver1_UL,
    MuonEG_Run2016B_ver2_UL,
    MuonEG_Run2016C_UL,
    MuonEG_Run2016D_UL,
    MuonEG_Run2016E_UL,
    MuonEG_Run2016F_HIPM_UL,
    MuonEG_Run2016F_UL,
    MuonEG_Run2016G_UL,
    MuonEG_Run2016H_UL,
]

# DoubleEG
DoubleEG_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_ver1_UL",   "/DoubleEG/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("DoubleEG_Run2016B_ver2_UL ",  "/DoubleEG/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016C_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016C_UL",        "/DoubleEG/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016D_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016D_UL",        "/DoubleEG/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016E_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016E_UL",        "/DoubleEG/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("DoubleEG_Run2016F_HIPM_UL",   "/DoubleEG/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016F_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016F_UL",        "/DoubleEG/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016G_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016G_UL",        "/DoubleEG/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
DoubleEG_Run2016H_UL       = Sample.nanoAODfromDAS("DoubleEG_Run2016H_UL",        "/DoubleEG/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

DoubleEG = [
    DoubleEG_Run2016B_ver1_UL,
    DoubleEG_Run2016B_ver2_UL,
    DoubleEG_Run2016C_UL,
    DoubleEG_Run2016D_UL,
    DoubleEG_Run2016E_UL,
    DoubleEG_Run2016F_HIPM_UL,
    DoubleEG_Run2016F_UL,
    DoubleEG_Run2016G_UL,
    DoubleEG_Run2016H_UL,
]

# SingleMuon
SingleMuon_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("SingleMuon_Run2016B_ver1_UL",   "/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("SingleMuon_Run2016B_ver2_UL",   "/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016C_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2016C_UL",        "/SingleMuon/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016D_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2016D_UL",        "/SingleMuon/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016E_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2016E_UL",        "/SingleMuon/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("SingleMuon_Run2016F_HIPM_UL",   "/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016F_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2016F_UL",        "/SingleMuon/Run2016F-UL2016_MiniAODv1_NanoAODv2-v4/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016G_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2016G_UL",        "/SingleMuon/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleMuon_Run2016H_UL       = Sample.nanoAODfromDAS("SingleMuon_Run2016H_UL",        "/SingleMuon/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleMuon = [
    SingleMuon_Run2016B_ver1_UL,
    SingleMuon_Run2016B_ver2_UL,
    SingleMuon_Run2016C_UL,
    SingleMuon_Run2016D_UL,
    SingleMuon_Run2016E_UL,
    SingleMuon_Run2016F_HIPM_UL,
    SingleMuon_Run2016F_UL,
    SingleMuon_Run2016G_UL,
    SingleMuon_Run2016H_UL,
]

# SingleElectron
SingleElectron_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_ver1_UL",   "/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("SingleElectron_Run2016B_ver2_UL",   "/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016C_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016C_UL",        "/SingleElectron/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016D_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016D_UL",        "/SingleElectron/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016E_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016E_UL",        "/SingleElectron/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("SingleElectron_Run2016F_HIPM_UL",   "/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016F_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016F_UL",        "/SingleElectron/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016G_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016G_UL",        "/SingleElectron/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
SingleElectron_Run2016H_UL       = Sample.nanoAODfromDAS("SingleElectron_Run2016H_UL",        "/SingleElectron/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

SingleElectron = [
    SingleElectron_Run2016B_ver1_UL,
    SingleElectron_Run2016B_ver2_UL,
    SingleElectron_Run2016C_UL,
    SingleElectron_Run2016D_UL,
    SingleElectron_Run2016E_UL,
    SingleElectron_Run2016F_HIPM_UL,
    SingleElectron_Run2016F_UL,
    SingleElectron_Run2016G_UL,
    SingleElectron_Run2016H_UL,
]

# JetHT
JetHT_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("JetHT_Run2016B_ver2_UL",   "/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("JetHT_Run2016B_ver2_UL",   "/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016C_UL       = Sample.nanoAODfromDAS("JetHT_Run2016C_UL",        "/JetHT/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016D_UL       = Sample.nanoAODfromDAS("JetHT_Run2016D_UL",        "/JetHT/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016E_UL       = Sample.nanoAODfromDAS("JetHT_Run2016E_UL",        "/JetHT/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("JetHT_Run2016F_HIPM_UL",   "/JetHT/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016F_UL       = Sample.nanoAODfromDAS("JetHT_Run2016F_UL",        "/JetHT/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016G_UL       = Sample.nanoAODfromDAS("JetHT_Run2016G_UL",        "/JetHT/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
JetHT_Run2016H_UL       = Sample.nanoAODfromDAS("JetHT_Run2016H_UL",        "/JetHT/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

JetHT = [
    JetHT_Run201BC_ver1_UL,
    JetHT_Run2016B_ver2_UL,
    JetHT_Run2016C_UL,
    JetHT_Run2016D_UL,
    JetHT_Run2016E_UL,
    JetHT_Run2016F_HIPM_UL,
    JetHT_Run2016F_UL,
    JetHT_Run2016G_UL,
    JetHT_Run2016H_UL,
]

# MET
MET_Run2016B_ver1_UL  = Sample.nanoAODfromDAS("MET_Run2016B_ver2_UL",   "/MET/Run2016B-ver1_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016B_ver2_UL  = Sample.nanoAODfromDAS("MET_Run2016B_ver2_UL",   "/MET/Run2016B-ver2_HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016C_UL       = Sample.nanoAODfromDAS("MET_Run2016C_UL",        "/MET/Run2016C-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016D_UL       = Sample.nanoAODfromDAS("MET_Run2016D_UL",        "/MET/Run2016D-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016E_UL       = Sample.nanoAODfromDAS("MET_Run2016E_UL",        "/MET/Run2016E-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016F_HIPM_UL  = Sample.nanoAODfromDAS("MET_Run2016F_HIPM_UL",   "/MET/Run2016F-HIPM_UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016F_UL       = Sample.nanoAODfromDAS("MET_Run2016F_UL",        "/MET/Run2016F-UL2016_MiniAODv1_NanoAODv2-v2/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016G_UL       = Sample.nanoAODfromDAS("MET_Run2016G_UL",        "/MET/Run2016G-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)
MET_Run2016H_UL       = Sample.nanoAODfromDAS("MET_Run2016H_UL",        "/MET/Run2016H-UL2016_MiniAODv1_NanoAODv2-v1/NANOAOD", dbFile=dbFile, redirector=redirector, overwrite=ov)

MET = [
    MET_Run2016B_ver1_UL,
    MET_Run2016B_ver2_UL,
    MET_Run2016C_UL,
    MET_Run2016D_UL,
    MET_Run2016E_UL,
    MET_Run2016F_HIPM_UL,
    MET_Run2016F_UL,
    MET_Run2016G_UL,
    MET_Run2016H_UL,
]

allSamples = DoubleMuon + MuonEG + DoubleEG + SingleMuon + SingleElectron + JetHT + MET

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 ) 
