#!/bin/sh

python launch.py $@ --config ULRun2017nanoAODv2_NANO  --production_label privateULRun2017v1_nanov2 --remoteDir privateULRun2017v1_nanov2 --unitsPerJob 20 --publish --isData --Run UL2017 --module Run2017UL_miniAOD --sample MET_Run2017A_UL
python launch.py $@ --config ULRun2017nanoAODv2_NANO  --production_label privateULRun2017v1_nanov2 --remoteDir privateULRun2017v1_nanov2 --unitsPerJob 20 --publish --isData --Run UL2017 --module Run2017UL_miniAOD --sample MET_Run2017B_UL
python launch.py $@ --config ULRun2017nanoAODv2_NANO  --production_label privateULRun2017v1_nanov2 --remoteDir privateULRun2017v1_nanov2 --unitsPerJob 20 --publish --isData --Run UL2017 --module Run2017UL_miniAOD --sample MET_Run2017C_UL 
python launch.py $@ --config ULRun2017nanoAODv2_NANO  --production_label privateULRun2017v1_nanov2 --remoteDir privateULRun2017v1_nanov2 --unitsPerJob 20 --publish --isData --Run UL2017 --module Run2017UL_miniAOD --sample MET_Run2017D_UL
python launch.py $@ --config ULRun2017nanoAODv2_NANO  --production_label privateULRun2017v1_nanov2 --remoteDir privateULRun2017v1_nanov2 --unitsPerJob 20 --publish --isData --Run UL2017 --module Run2017UL_miniAOD --sample MET_Run2017E_UL
python launch.py $@ --config ULRun2017nanoAODv2_NANO  --production_label privateULRun2017v1_nanov2 --remoteDir privateULRun2017v1_nanov2 --unitsPerJob 20 --publish --isData --Run UL2017 --module Run2017UL_miniAOD --sample MET_Run2017F_UL 
