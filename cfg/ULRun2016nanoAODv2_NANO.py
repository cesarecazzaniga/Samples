# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: ULRun2016nanoAODv2 -s NANO --data --conditions 106X_dataRun2_v32 --era Run2_2016,run2_nanoAOD_106Xv1 --eventcontent NANOAOD --datatier NANOAOD --fileout file:UL_Run2016_nanoAODv2.root --filein dbs:/MET/Run2016C-21Feb2020_UL2016_HIPM-v1/MINIAOD --customise_commands=process.add_(cms.Service('InitRootHandlers', EnableIMT = cms.untracked.bool(False)));process.MessageLogger.cerr.FwkReport.reportEvery=100 -n -1 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2016_cff import Run2_2016
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv1_cff import run2_nanoAOD_106Xv1
from PhysicsTools.NanoAOD.common_cff import *
process = cms.Process('NANO',Run2_2016,run2_nanoAOD_106Xv1)

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
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/07AE9484-4BDC-BF4B-9838-6A2EE6C4AEF8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/0D9E4F57-6E3F-3643-9F2C-56678C9E1E12.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/133BC016-2563-6240-815D-B66DB15716A0.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/170BFE66-41D5-A44E-ACE9-F36FB5FD2912.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/26224B13-71F4-054B-BD2F-7EE4BDF5656A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/2F90B3E4-B387-0547-AADE-C645076F13C3.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/3372F01B-D2A2-5840-95F8-3A510C0648BC.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/3A0E1EF0-ED5D-864F-B627-F7B6ADA28687.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/41B34DEB-9052-954B-9533-0A1D835FEF30.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/43707C6C-3115-E84D-AE67-FB2574F9ACCA.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/45667495-3C38-8D47-84CE-4E3B3366CF80.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/45C34029-7F46-D64B-91E3-EA985A239B53.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/467D7D67-00E3-5C4F-85BC-7C30A1BCA11B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/4AA79023-9657-A94F-9C6E-29501F073420.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/51EA6C2D-5BC3-D549-B3CD-67F2E324643E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/56D3BFF3-2D5B-CD47-9405-96F2F754CF29.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/5A9B48C6-2CD7-804E-9B28-D51C8358F12D.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/60F92B36-6F73-7B40-8BEF-065829DAC61A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/6227A57B-2045-064F-BCEB-C7C6AAA0D95B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/625D1CB0-B15B-9A47-BECE-54834007C73E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/6FB20C5F-26BF-7646-9AA2-E2644171E7E1.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/70AEEB56-2594-9F43-834A-AF057F6D9F33.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/728662D7-8119-F64A-B4DD-39645FE715E1.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/74445941-C5B0-7C4B-A2DD-1588342B03B5.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/7518D3B2-4108-B94A-845E-6A09FED1A2B1.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/759EA508-2FFB-2346-8CFD-443E0FB7D4CF.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/788EFBF1-F42C-5A47-9F6B-3C4B3B48968D.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/7F5C60E0-9342-A644-AB62-6C3E91AB168E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/8F6DB785-E6C8-1A40-8006-A9FF218137F8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/921A4234-1E8F-6F41-B24A-F8FB65EB046B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/99A2EED6-4BFB-0247-8ADC-1A06BEE7BD18.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/9B80A8AF-3B29-7B49-8065-C377DEE6DE64.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/A14D43F0-56E9-5B42-8AD0-6282EAB53964.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/A2315DE8-8E1D-A54F-82EE-F4378F08B9E8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/A5CE8C6B-135E-764C-8039-905E13BE65FF.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/ACDC7AAA-C50D-0946-8059-1343ADCE1193.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/B6F3EB8C-4D33-9D4E-9AE1-CF224B67F678.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/B7B9F46F-EDB3-BA4D-9EF3-E7E6E5C17E5B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/BAEDC3B2-2321-F84E-8D93-1A4619ADBD93.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/BCF91EAA-A20F-344A-8AD7-2DE424FED92B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/C8245C6F-04D0-8747-AEC5-DAF033DB2EAC.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/CB752964-5B3B-224D-899D-4E2365B1B668.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/D2D1C560-D725-964C-A397-5D8834405258.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/D8A6204C-9D02-4846-BD90-D4CAC676BB22.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/EEBFD500-E69C-6E4D-A13C-964D69479FCC.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/F15818EE-39A4-7749-9409-9EE98320E1CA.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/F53E6460-09E6-5041-841E-6DB9966484AD.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/F578A54D-B299-B446-9948-74B1206C6B71.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/10000/F5DDC2AC-DAEB-6940-89CA-FB3930BDDDA9.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/30000/A89B8C76-E43E-E14D-BCB1-C538DEE9D4CD.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/00E8913F-2280-6440-8746-D65D7D0EC486.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/012F50C6-3969-FF46-AEC3-5E464D05A099.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/03A73252-CB14-1B4A-B408-FFD13F502634.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/03C40AF8-5E8C-E240-9883-695D897C6732.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/054AC84F-F588-184D-B6A3-93DF8AEBE39A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/078BF4BB-890D-5747-8926-3F7A9416F402.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/08404AB7-E25A-5143-9D47-C57541182D70.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/0A30F9F4-83BD-6545-BCAA-17764495054E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/0B044D24-D3BA-6540-8B2B-A7C135846215.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/0CD49E4E-5768-1642-9550-736F71A55181.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/0DFB88D7-8A2F-1A40-838F-B38BF19E7DF8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/0E1FF578-B81C-3A47-91EB-0CF972326AB8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/0FDEB2FE-6A7C-9042-91BB-0AFE9604CD59.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1038A8CE-40EE-FB47-800D-2C28649BAAE9.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/116A0F55-C579-D94C-A6C2-76D17EFB4B1E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/145EF694-6EDC-C34D-B70E-785BC95D7504.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/15897491-4B66-8142-BCED-BEA6B7F61C4E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1664A724-59E5-144A-BCC8-FE00F5D62677.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/173638A4-74FE-2F46-B6E2-89D89C4FEDCB.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/187F4607-DC35-C942-8832-33510093B3AF.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1AB007BB-D6B3-714E-8B95-4D93AA6B4EAD.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1B1EB618-52A5-5943-96D0-E6D25E2EC25A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1BD8ECDA-2955-BB45-A2F5-F71612FDA95B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1D283396-2002-CB41-B9D3-803A9FD01D84.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/1D6827E9-FE9A-F34D-9984-5957537C904A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/219EA126-C12E-D848-83AB-14662947B26C.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/274A33D3-C3A4-2343-83BE-083C771C504B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/274DD8ED-D015-2445-96D7-78720556F7BC.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/2835B92F-36FA-E148-AAE7-A0C4EBD91A72.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/28706F83-B8DA-F740-A722-3A86F3A0D9AE.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/28FF8552-A88E-6647-B166-CC3A7128CC85.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/2DB992D3-9AED-8345-9838-C7964499A1FE.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/332E4E61-DD36-2643-9CB9-968E4384C4A5.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/3588E43B-64E9-AC42-A8F2-ED1C8058FC74.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/36365522-46D0-2245-9283-3F463BA0555E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/36E6B154-65DB-9F49-A241-71C421BD1BE5.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/3AC4C0F1-730B-A548-9FA0-D16946D5A12B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/45A1EF0F-6488-1649-B5A3-9FBB4EB91DF7.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/498312D0-8490-9D41-8F81-567EAF1C26B0.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/4B2CBFD5-889B-4E4E-9D8C-012940AEF7BB.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/4E14CCF1-7582-F24A-94E8-7C456A924709.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/530E8AA6-3973-C546-83B7-E1F893C47F33.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/53C17004-A179-DB44-B687-76848DF2EF06.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/5D0122EA-9478-2D48-B3DF-21ECB72EBD49.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/5DCCE126-0163-7140-BBB8-86226B407D05.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/5E201ADD-CBFA-4349-96A0-26B2966B7AAE.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/6277C4C6-515A-5647-907E-E8FF441CE083.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/63746A71-045B-2445-B8ED-A402E29FAE49.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/66DCE00B-933B-1D4A-A749-AF1B770826B0.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/69E47ACB-DAAA-974D-956D-3CB30AF02D7B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/6B9F05A2-FFEE-A143-BC12-747E4AE114FB.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/6BB95A72-F180-264E-A123-82C86131C636.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/6D57267F-1A9D-B640-BF9C-23E19DE07B7C.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/71C695BF-3F0F-CB4B-8604-741860AC5CB5.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/71F2892E-7110-1840-9B98-6AEA1158CB63.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/7504C06A-C057-C647-B12B-427AB9248A93.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/78E765CA-4481-9C41-820F-BEAA86D21ADD.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/7CAD53E1-E921-C043-B63B-A7AA3248577D.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/7D6F4FBC-E095-8B4B-A34E-B746FD94471C.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/7E199A6C-11AA-1B47-B5CE-772E8782BAE4.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/7ECE9BF9-4B40-1A4C-964D-5AD63B3EC06D.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/862FB9A8-B200-2C46-9017-6C1FCFD32D9A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/87EC9954-6124-8449-8ADE-49DF040FA832.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/8B24AD65-D247-C74B-B00B-CE48A5374B29.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/8C2ED755-759F-BE4C-983F-2DD14968B411.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/8D992062-C765-1E44-A845-E2AC17EBF589.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/92C5DE3C-78F4-4642-9ABF-FBD946469E9E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/9485826A-F653-1E4F-95F4-6D86A63FE9BC.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/958E0252-D71D-2D47-8925-6EB364676A30.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/96456AF2-A084-0442-94FE-BEEA84FDC7CC.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/99801F95-0776-0045-9D41-FBF04D274D5E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/9EF321C3-F9B4-7043-9206-F685B5EBB673.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/A15B7661-0632-FD43-B34F-72C3FD0CF5C0.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/A22A41BE-62E1-7140-8AC0-38A34030AB6C.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/A345FCC6-30E8-2F4F-8927-CD1839DAAD1A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/A7926DD7-B698-3C41-AB83-45EEE83ECD02.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/AC9BBE53-08AA-9D44-900D-21E7898A608B.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/AE10813F-DE18-7941-8DCD-7E9A2D58DDB2.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/AE484BB4-CDE6-2B4A-8EDB-6A69117E5897.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/AF754B27-67D5-CD40-B4E6-5B61DC07D9AA.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/BAE13A84-9AE0-414F-A341-48C341F39BE3.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/BC2CD9AF-50AB-0E4D-8455-CBD17C2A65B9.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/BE8FE479-04C6-0A43-A603-C3C01F31F9F5.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/BED0EE6D-61A3-574C-8C87-B2B0489BADE6.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/C08CCB34-285C-8F46-8F27-D2E83EFB4BB8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/C7BA89BE-92E9-3D46-AF47-CA937581B46E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/CB9BA8BB-F56B-D045-A6B2-62A0F72C353D.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/CE4D624B-0D43-EB43-91BB-ECB0CC1A270C.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/D01086EC-E5EB-4F4A-B50C-9D9059935B01.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/D32A551E-268D-374E-836A-4758C439C83F.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/D692D2EE-52ED-AB48-AE0F-AFF2ED26BCBD.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/D757455D-EAB2-A44D-BED4-B4B91111CBE3.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/DEC90E6C-850B-4D4A-ABCC-2D1FA7EA8DB8.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/E1BD6AB6-EF93-8C46-ABF7-7FFF9C24454E.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/E5389FE1-20CB-EF47-A109-A9D806C10C59.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/EA567A14-6FBD-4544-BB7E-0C877D2FF64A.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/F11DFD24-E853-1B45-8007-1A6329482894.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/F1A07C9D-0437-2F4B-8409-7DAD9A154041.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/F2F18F76-C4C0-D246-886C-A7EBF1C5E00C.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/FB5D3552-61E8-F44A-8E43-796EF92D9A2F.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/FE2EC061-479B-534E-B661-FAAA2C64A7F2.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/40000/FF494A00-1040-B341-A9AA-109CD3FE7200.root', 
        '/store/data/Run2016C/MET/MINIAOD/21Feb2020_UL2016_HIPM-v1/410000/51E66554-09B6-4042-A594-62962884357A.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('ULRun2016nanoAODv2 nevts:-1'),
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
    #fileName = cms.untracked.string('file:UL_Run2016_nanoAODv2.root'),
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
