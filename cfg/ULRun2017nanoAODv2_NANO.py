# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: ULRun2017nanoAODv2 -s NANO --data --conditions 106X_dataRun2_v32 --era Run2_2017,run2_nanoAOD_106Xv1 --eventcontent NANOAOD --datatier NANOAOD --fileout file:UL_Run2017_nanoAOD.root --filein dbs:/MET/Run2017A-09Aug2019_UL2017_rsb-v1/MINIAOD --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=100 -n -1 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2017_cff import Run2_2017
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1
from PhysicsTools.NanoAOD.common_cff import *
process = cms.Process('NANO',Run2_2017,run2_nanoAOD_106Xv1)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/0E7F1B7B-E056-8D46-A646-C0B884C7F6E3.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/12BBB3B4-8C26-7541-8CBE-FD8234402CD4.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/1E9DD363-8673-CA4B-B1B2-098B8430D4FF.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/3A231FBE-BF87-FB45-91F7-7D0DD416B491.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/46922663-BFAA-9E4C-8DA3-B602FA8A27AC.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/478225CC-EA57-544C-B326-787B8C58E09F.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/49C03E78-D545-4B45-A429-12CAE8142138.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/4EFE9857-9825-6B46-8726-E42AD4244684.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/64FF5AFC-5070-5F43-8DF5-E6E08CD222ED.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/7B64F7AD-1F70-EE47-91CE-C6357B172AA6.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/819B598C-7501-CA45-AD3B-139346061371.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/89E4B018-9B47-0340-A30B-2210FFE710E2.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/96EC67BC-ED8D-7E47-8706-25128C6E7312.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/A981C604-8663-1D40-8722-4FE61D77F125.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/B221FA67-4337-9E45-BC77-0B3EEB2F6C4B.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/D18F6243-6DF6-AF45-9A96-13B2CEDF5D33.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/D25BFF9F-3E80-8541-BEF1-E8FDCBD99A75.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/DC7A83DB-A6FF-AF4E-81E0-5F1EDDEEE605.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/E2E9C0CC-8DEE-854D-BB26-741BC3221DFB.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/ED7945D3-6343-CD44-8A15-38F3C764185B.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/F2FCA5B0-C4C4-BC45-9BBA-254E9A6D45F3.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/120000/F980C023-14A3-3B4E-B12E-B91B47257D72.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/0E8158E4-C31D-EC47-A2E5-B7A99D0107B9.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/0F5C32FC-A75F-8949-986C-F54F2F3C4F4C.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/11371202-86C5-4349-828F-B55DDADDB0CC.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/15DB2CA5-A0DF-A94C-882B-CD9C41013EFD.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/286BF3AB-AB2A-C345-8F4B-37AA18C91B9F.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/29F84C2F-ACFD-E14A-808A-0639DB9C0582.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/2E3E50A2-2BB9-CA4E-9C05-946CC131F6F5.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/329DD7DE-5D04-D543-9158-8A060C8E8D9F.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/4586670F-B9AF-D748-A63B-AE9651E8006A.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/484558C9-98B3-624B-B5C4-8BFD1DD57D9B.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/4B21BFF3-149F-8B49-A938-88040B66A35C.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/5F379CA1-A098-2943-B223-BAA8B7977863.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/612F4DE5-8C6A-B542-851F-0C6550AD8435.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/75B4916C-FEEE-804E-802A-67F680D8EF57.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/89403ECD-76AD-CE43-B648-9C9B9F82FF4E.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/9139758B-DE9B-334F-9276-C2A172B09640.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/B445F9FA-6EC7-BE44-B548-3AB17ED60469.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/C0E6E4E4-DBF9-0C48-9050-72E8204400B9.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/D431EE29-CA06-7746-B1C5-7AC8AA177435.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/D45D3C90-5E8A-A843-8BCD-866568AD453B.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/D6470D09-0A53-0446-B864-A3187D02372B.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/DF333684-5B9F-E744-BB39-FC0A7FB7387B.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/E2BE516A-64C0-A742-884B-F407B534F12E.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/E30CC305-F96E-7D4A-AAC5-B022633A0F77.root', 
        '/store/data/Run2017A/MET/MINIAOD/09Aug2019_UL2017_rsb-v1/260000/E4764B7E-EA61-CC4C-B3E1-546C58E84665.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('ULRun2017nanoAODv2 nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAOD'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:nanoAOD.root'),
    #fileName = cms.untracked.string('file:UL_Run2017_nanoAOD.root'),
    outputCommands = process.NANOAODEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_dataRun2_v32', '')

# Path and EndPath definitions
process.nanoAOD_step = cms.Path(process.nanoSequence)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODoutput_step = cms.EndPath(process.NANOAODoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.
process.finalIsolatedTracks.cut = cms.string("((pt>0 && (abs(pdgId) == 11 || abs(pdgId) == 13)) || pt > 0) && (abs(pdgId) < 15 || abs(eta) < 2.5) && ((pfIsolationDR03().chargedHadronIso < 5 && pt < 25) || pfIsolationDR03().chargedHadronIso/pt < 0.2)")
process.isoTrackTable.doc = cms.string("isolated tracks after basic selection (" + process.finalIsolatedTracks.cut.value() + ") and lepton veto")
process.isoTrackTable.variables = cms.PSet(process.isoTrackTable.variables,deltaEta = Var("deltaEta",float,doc="difference in eta between initial track and intersection w/ ecal",precision=12),deltaPhi = Var("deltaPhi",float,doc="difference in phi between initial track and intersection w/ ecal",precision=12),)
process.genParticleTable.variables = cms.PSet(process.genParticleTable.variables, vx = Var("vx",  float,precision=10), vy = Var("vy",  float,precision=10),vz = Var("vz",  float,precision=10),)
# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeData 

#call to customisation function nanoAOD_customizeData imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeData(process)

# End of customisation functions

# Customisation from command line

process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=100
# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
