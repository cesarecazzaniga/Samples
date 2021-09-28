cmsDriver.py  SUS_RunIISummer20UL16NanoAODv2 -s NANO --eventcontent NANOAODSIM --customise_commands="process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)))" --datatier NANOAODSIM --fileout file:SUS-RunIISummer20UL16NanoAODv2-00003.root --conditions 106X_mcRun2_asymptotic_v15 --filein "dbs:/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16MiniAOD-106X_mcRun2_asymptotic_v13-v1/MINIAODSIM" --era Run2_2016,run2_nanoAOD_106Xv1 --no_exec --mc -n 100
## cmsRun before submitting to crab
# cmsRun SUS_RunIISummer20UL16NanoAODv2_NANO.py 

