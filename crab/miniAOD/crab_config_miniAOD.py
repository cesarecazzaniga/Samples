#run in CMSSW_9_4_7
tag = 'Autumn18-mAODv1-10222'

from CRABAPI.RawCommand import crabCommand
from WMCore.Configuration import Configuration
config = Configuration()

config.section_("General")
config.General.requestName = "fastMAOD" 
config.General.workArea = 'crab_miniAOD_%s' % tag
config.General.transferLogs = True

config.section_("JobType")
config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = '../../cfg/miniAOD_mc_fast_102X_Autumn18.py'
config.JobType.psetName = '../../cfg/miniAODv1_Autumn18_fast_10_2_22.py'
config.JobType.disableAutomaticOutputCollection = False
config.JobType.allowUndistributedCMSSW = True

config.section_("Data")
#config.Data.splitting = 'FileBased'
#config.Data.splitting = 'EventBased'
config.Data.splitting = 'EventAwareLumiBased'
#config.Data.totalUnits  = 500000 
config.Data.unitsPerJob = 2000
#config.Data.totalUnits  = 50000 
config.Data.publication = True
config.Data.inputDBS = 'phys03'
config.Data.publishDBS = 'phys03'

#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.ignoreLocality = False

config.section_("Site")
config.Site.storageSite = 'T2_AT_Vienna'
#config.Site.whitelist = ['T2_CERN_CH', 'T1_US_FNAL_Disk'] #Run where the PU dataset is, not where the sample is
config.section_("User")

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand

    for input_dataset in [
        '/ttG_noFullyHad-v5/schoef-ttG_noFullyHad-v5-fa75f6d0d64d97494f28d49b68b6ba8c/USER',
        '/ttW01j-v5/schoef-ttW01j-v5-d30966c9709b9416b921be2ac111acc6/USER',
        '/ttZ01j-v5/schoef-ttZ01j-v5-5941b9a9132a067bf58859850614a6bf/USER',
        '/WGToLNu/schoef-WGToLNu-888b7a86c2f3c15fead55bb8986384d5/USER',
        '/WW-v5/schoef-WW-v5-448bcad3b0404ce78bc7375a23091706/USER',
        '/WZTo3L1Nu-v5/schoef-WZTo3L1Nu-v5-151ec2871e2ed107def2a3aa630d2b24/USER',
        '/WZTojj2L-v5/schoef-WZTojj2L-v5-51f23f9fff638dfa36bf796f0c0fdb5e/USER',
        '/WZToLNujj-v5/schoef-WZToLNujj-v5-dfc272e117ae7be94858714bc60ae844/USER',
        '/ZGTo2L-v5/schoef-ZGTo2L-v5-84bab5a634a89234423bfe901d2c77f0/USER',
    ]:
        config.Data.inputDataset = input_dataset
        config.General.requestName = input_dataset.split('/')[1] 
        config.Data.outputDatasetTag = tag 
        
        #crabCommand('submit', '--dryrun', config = config)
        crabCommand('submit', config = config)
