#!/bin/sh

python launch.py $@ --config ULRun2018nanoAODv2_NANO  --production_label privateULRun2018v1_nanov2 --remoteDir privateULRun2018v1_nanov2 --unitsPerJob 25 --publish --isData --Run UL2018 --module Run2018UL_miniAOD --sample MET_Run2018A_UL
python launch.py $@ --config ULRun2018nanoAODv2_NANO  --production_label privateULRun2018v1_nanov2 --remoteDir privateULRun2018v1_nanov2 --unitsPerJob 25 --publish --isData --Run UL2018 --module Run2018UL_miniAOD --sample MET_Run2018B_UL
python launch.py $@ --config ULRun2018nanoAODv2_NANO  --production_label privateULRun2018v1_nanov2 --remoteDir privateULRun2018v1_nanov2 --unitsPerJob 25 --publish --isData --Run UL2018 --module Run2018UL_miniAOD --sample MET_Run2018C_UL 
python launch.py $@ --config ULRun2018nanoAODv2_NANO  --production_label privateULRun2018v1_nanov2 --remoteDir privateULRun2018v1_nanov2 --unitsPerJob 25 --publish --isData --Run UL2018 --module Run2018UL_miniAOD --sample MET_Run2018D_UL
