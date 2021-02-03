import copy, os, sys
from RootTools.core.Sample import Sample
import ROOT

def get_parser():
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for samples file")
    argParser.add_argument('--overwrite',   action='store_true',    help="Overwrite current entry in db?")
    argParser.add_argument('--update',      action='store_true',    help="Update current entry in db?")
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
        from Samples.Tools.config import redirector_clip as redirector
    else:
        from Samples.Tools.config import redirector as redirector

# DB

ttG_noFullyHad_fast =  Sample.fromDirectory("ttG_noFullyHad_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/ttG_noFullyHad", xSection=4.168e+00) 
ttG_noFullyHad_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/top_boson_reweight_card.pkl"
ttZ01j_fast         =  Sample.fromDirectory("ttZ01j_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/ttZ01j", xSection=1.166e-01)
ttZ01j_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/top_boson_reweight_card.pkl"
ttW01j_fast         =  Sample.fromDirectory("ttW01j_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/ttW01j", xSection=1.458e+00)
ttW01j_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/top_boson_reweight_card.pkl"

WZTo3L1Nu_fast      =  Sample.fromDirectory("WZTo3L1Nu_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/WZTo3L1Nu", xSection=1.729e+00)
WZTo3L1Nu_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
WZTojj2L_fast       =  Sample.fromDirectory("WZTojj2L_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/WZTojj2L", xSection=3.568e+00)
WZTojj2L_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
WZToLNujj_fast      =  Sample.fromDirectory("WZToLNujj_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/WZToLNujj", xSection=1.163e+01)
WZToLNujj_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
WGToLNu_fast        =  Sample.fromDirectory("WGToLNu_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/WGToLNu", xSection=5.453e+01)
WGToLNu_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
ZGTo2L_fast         =  Sample.fromDirectory("ZGTo2L_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/ZGTo2L", xSection=9.087e+00)
ZGTo2L_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
WW_fast             =  Sample.fromDirectory("WW_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/WW", xSection=1.194e+01)
WW_fast.reweight_pkl     = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"

allSamples = [
    ttG_noFullyHad_fast,
    ttZ01j_fast,
    ttW01j_fast,
    WZTo3L1Nu_fast,
    WZTojj2L_fast,
    WZToLNujj_fast,
    WGToLNu_fast,
    ZGTo2L_fast,
    WW_fast,
]

for s in allSamples:
    s.isData = False
