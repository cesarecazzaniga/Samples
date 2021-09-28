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
#            from Samples.Tools.config import redirector_clip as redirector
#    else:
#        from Samples.Tools.config import redirector as redirector
#
## DB
#from Samples.Tools.config import dbDir
#dbFile = dbDir+'/DB_Run2016_ULnanoAODv2.sql'
#logger.info("Using db file: %s", dbFile)


# MET
MET_Run2016B_ver1_UL  = Sample.fromDirectory("MET_Run2016B_ver1_UL",   "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016B-21Feb2020_ver1_UL2016_HIPM-v1_privateULRun2017v1_nanov2/210911_184617/")
MET_Run2016B_ver2_UL  = Sample.fromDirectory("MET_Run2016B_ver2_UL",   "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016B-21Feb2020_ver2_UL2016_HIPM-v1_privateULRun2017v1_nanov2/210911_190732/"  )
MET_Run2016C_UL       = Sample.fromDirectory("MET_Run2016C_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016C-21Feb2020_UL2016_HIPM-v1_privateULRun2017v1_nanov2/210912_165916/"  )
MET_Run2016D_UL       = Sample.fromDirectory("MET_Run2016D_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016D-21Feb2020_UL2016_HIPM-v1_privateULRun2017v1_nanov2/210912_165937/"  )
MET_Run2016E_UL       = Sample.fromDirectory("MET_Run2016E_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016E-21Feb2020_UL2016_HIPM-v1_privateULRun2017v1_nanov2/210912_170008/"  )
MET_Run2016F_HIPM_UL  = Sample.fromDirectory("MET_Run2016F_HIPM_UL",   "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016F-21Feb2020_UL2016_HIPM-v1_privateULRun2017v1_nanov2/210912_170058/"  )
MET_Run2016F_UL       = Sample.fromDirectory("MET_Run2016F_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016F-21Feb2020_UL2016-v1_privateULRun2017v1_nanov2/210912_170038/"  )
MET_Run2016G_UL       = Sample.fromDirectory("MET_Run2016G_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016G-21Feb2020_UL2016-v1_privateULRun2017v1_nanov2/210912_170119/"  )
MET_Run2016H_UL       = Sample.fromDirectory("MET_Run2016H_UL",        "/eos/vbc/experiments/cms/store/user/prhussai/MET/crab_Run2016H-21Feb2020_UL2016-v2_privateULRun2017v1_nanov2/210912_170147/"  )

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

allSamples =  MET

for s in allSamples:
    s.json      = os.path.expandvars("$CMSSW_BASE/src/Samples/Tools/data/json/Cert_271036-284044_13TeV_Legacy2016_Collisions16_JSON.txt")
    s.isData    = True

from Samples.Tools.AutoClass import AutoClass
samples = AutoClass( allSamples )
if __name__=="__main__":
    if options.check_completeness:
        samples.check_completeness( cores=20 ) 
