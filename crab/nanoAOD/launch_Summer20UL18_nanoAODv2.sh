#Summer20UL18nanoAODv2
#python launch.py --config nano_v2_mc_106X_Summer20UL18_NANO --dryrun --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT100To200
##Run already
#python launch.py --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT100To200
##Run them now
python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT70To100 
#python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT200To400
#python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT400To600
#python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT600To800
#python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT800To1200
#python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT1200To2500
#python launch.py $@  --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WJetsToLNu_HT2500ToInf

python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample TTLep_pow
python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample TTSingleLep_pow
#
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT100To200 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT200To400 
python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT400To600 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT600To800 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT800To1200 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT1200To2500 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZJetsToNuNu_HT2500ToInf 

#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WWTo2L2Nu 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample WZTo3LNu_NLO 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZZTo2L2Nu 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ZZTo4L 
#
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT70to100 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT100to200 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT200to400 
python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT400to600 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT600to800 
python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT800to1200 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT1200to2500 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample DYJetsToLL_M50_HT2500toInf 

#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ST_tW_top_NoFullyHad_5f_pow 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ST_tW_antitop_NoFullyHad_5f_pow 
#
python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample TTGJets_NLO 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample ttWJetsToLNu_NLO 
python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 10 --publish --module Summer20UL18_miniAOD --sample ttWJetsToQQ_NLO

#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT50to100 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT100to200 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT200to300 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT300to500 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT500to700 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT700to1000 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT1000to1500 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT1500to2000 
#python launch.py $@ --config SUS_RunIISummer20UL18NanoAODv2_NANO --production_label privateUL18v1_nanov2 --remoteDir privateUL18v1_nanov2 --unitsPerJob 2 --publish --module Summer20UL18_miniAOD --sample QCD_HT2000toInf 

