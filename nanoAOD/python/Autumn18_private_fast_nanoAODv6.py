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

ttG_noFullyHad_fast =  Sample.fromDirectory("ttG_noFullyHad_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v6/ttG_noFullyHad/", xSection=3.470e+00) 
ttG_noFullyHad_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v6/ttG_noFullyHad_reweight_card.pkl"
ttG_noFullyHad_fast.normalization = 16777216.0

ttG_noFullyHad_SM_fast =  Sample.fromDirectory("ttG_noFullyHad_SM_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/v5/ttG_noFullyHad_SM", xSection=3.470e+00) 
ttG_noFullyHad_SM_fast.normalization = 6042*3000.

WGToLNu_fast =  Sample.fromDirectory("WGToLNu_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v6/WGToLNu/", xSection=6.307e+01) 
WGToLNu_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v6/WGToLNu_reweight_card.pkl"
WGToLNu_fast.normalization = 5687653.0

ZGTo2L_fast =  Sample.fromDirectory("ZGTo2L_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v6/ZGTo2L/", xSection=1.109e+01) 
ZGTo2L_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v6/ZGTo2L_reweight_card.pkl"
ZGTo2L_fast.normalization = 6776987.0

ttZ01j_fast         =  Sample.fromDirectory("ttZ01j_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/flavor/ttZ01j", xSection=6.563e-02)
ttZ01j_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/order_2/ttZ01j_reweight_card.pkl"
ttZ01j_fast.normalization =  1488765.0

WZTo3L1Nu_fast         =  Sample.fromDirectory("WZTo3L1Nu_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/flavor/WZTo3L1Nu", xSection=1.036e+00)
WZTo3L1Nu_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/order_2/WZTo3L1Nu_reweight_card.pkl"
WZTo3L1Nu_fast.normalization =  2049842.0

ZZ_fast         =  Sample.fromDirectory("ZZ_fast", "/eos/vbc/user/robert.schoefbeck/nanoAODSim_fast_private/flavor/ZZ", xSection=1.134e-01)
ZZ_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/order_2/ZZ_reweight_card.pkl"
ZZ_fast.normalization =  2607863.0

#ttG_noFullyHad_fast =  Sample.fromDirectory("ttG_noFullyHad_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/ttG_noFullyHad", xSection=4.168e+00) 
#ttG_noFullyHad_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/top_boson_reweight_card.pkl"
#ttG_noFullyHad_fast.normalization = 2614389.0
#ttZ01j_fast         =  Sample.fromDirectory("ttZ01j_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/ttZ01j", xSection=1.166e-01)
#ttZ01j_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/top_boson_reweight_card.pkl"
#ttZ01j_fast.normalization =  1170285.0
#ttW01j_fast         =  Sample.fromDirectory("ttW01j_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/ttW01j", xSection=1.458e+00)
#ttW01j_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/top_boson_reweight_card.pkl"
#ttW01j_fast.normalization = 1081772.0
#
#WZTo3L1Nu_fast      =  Sample.fromDirectory("WZTo3L1Nu_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/WZTo3L1Nu", xSection=1.729e+00)
#WZTo3L1Nu_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
#WZTo3L1Nu_fast.normalization = 1766697.0
#WZTojj2L_fast       =  Sample.fromDirectory("WZTojj2L_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/WZTojj2L", xSection=3.568e+00)
#WZTojj2L_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
#WZTojj2L_fast.normalization = 1771616.0
#WZToLNujj_fast      =  Sample.fromDirectory("WZToLNujj_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/WZToLNujj", xSection=1.163e+01)
#WZToLNujj_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
#WZToLNujj_fast.normalization = 1725969.0
#WGToLNu_fast        =  Sample.fromDirectory("WGToLNu_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/WGToLNu", xSection=5.453e+01)
#WGToLNu_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
#WGToLNu_fast.normalization = 1269847.0
#ZGTo2L_fast         =  Sample.fromDirectory("ZGTo2L_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/ZGTo2L", xSection=9.087e+00)
#ZGTo2L_fast.reweight_pkl = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
#ZGTo2L_fast.normalization = 1461428.0
#WW_fast             =  Sample.fromDirectory("WW_fast", "/eos/vbc/user/robert.schoefbeck/topNanoAODSim_fast_private/v5/WW", xSection=1.194e+01)
#WW_fast.reweight_pkl     = "/eos/vbc/user/robert.schoefbeck/gridpacks/v5/boson_reweight_card.pkl"
#WW_fast.normalization = 1737656.0

allSamples = [
    ttG_noFullyHad_fast,
    ttG_noFullyHad_SM_fast,
    WGToLNu_fast,
    ZGTo2L_fast,

#    ttW01j_fast,
#
    ttZ01j_fast,
    WZTo3L1Nu_fast,
    ZZ_fast,
#    WZTojj2L_fast,
#    WZToLNujj_fast,
#    WGToLNu_fast,
#    ZGTo2L_fast,
#    WW_fast,
]

for s in allSamples:
    s.isData    = False
    s.isFastSim = True
    for i_f, f in enumerate(s.files):
        if f.startswith('/eos/'):
            s.files[i_f] = 'root://eos.grid.vbc.ac.at/'+f
