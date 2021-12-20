 #!/bin/sh

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_3LinePatched/"
#gridpack="TTGamma_SingleLeptFromT_3LinePatched_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromT_3LinePatched_SM_GENSIM"

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/TTGamma_SingleLeptFromT_1Line/"
#gridpack="TTGamma_SingleLeptFromT_1Line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromT_1Line_SM_GENSIM_v2"

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/EFT/TTGamma_DiLept_1Line_EFT/"
#gridpack="TTGamma_DiLept_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_DiLept_1Line_EFT_GENSIM_v3"

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_SingleLeptFromT_1line_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromT_1line_5f_ckm_LO_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_SingleLeptFromT_1line_5f_ckm_LO_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_SingleLeptFromTbar_1line_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromTbar_1line_5f_ckm_LO_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_SingleLeptFromTbar_1line_5f_ckm_LO_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_SingleLeptFromT_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromT_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_SingleLeptFromT_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_SingleLeptFromTbar_5f_ckm_LO/"
#gridpack="ttGamma_SingleLeptFromTbar_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_SingleLeptFromTbar_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_Dilept_5f_ckm_LO/"
#gridpack="ttGamma_Dilept_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_Dilept_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/central/ttGamma_Hadronic_5f_ckm_LO/"
#gridpack="ttGammaHadronic_5f_ckm_LO_tarball.tar.xz"
#label="ttGamma_Hadronic_5f_ckm_LO_central_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/newEFT/TTGamma_SingleLeptFromT_1Line_EFT/"
#gridpack="TTGamma_SingleLeptFromT_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromT_1Line_EFT_GENSIM_v3"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/newEFT/TTGamma_SingleLeptFromTbar_1Line_EFT/"
#gridpack="TTGamma_SingleLeptFromTbar_1Line_EFT_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="TTGamma_SingleLeptFromTbar_1Line_EFT_GENSIM_v3"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTXPheno/gridpacks/WJetsToLNu3Jets"
#gridpack="WJetsToLNu_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz"
#label="WJetsToLNu"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTXPheno/gridpacks/WJetsToLNu"
#gridpack="WJetsToLNu_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="WJetsToLNu4Jets"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard"
#gridpack="ttGamma_CMS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_ATLASrunCard"
#gridpack="ttGamma_ATLAS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_ATLASrunCard"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard"
#gridpack="ttGamma_CMS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_small"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_ATLASrunCard"
#gridpack="ttGamma_ATLAS_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_ATLASrunCard_small"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 100000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTZRun2EFT/gridpacks/EFT/ttZ_ll_LO_order4_6weights_ref/"
#gridpack="ttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttZ_order4_6weights_EFT"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR/"
#gridpack="ttGamma_CMS_deltaR_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut/"
#gridpack="ttGamma_CMS_jetPt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_xqcut/"
#gridpack="ttGamma_CMS_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_xqcut/"
#gridpack="ttGamma_CMS_deltaR_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut/"
#gridpack="ttGamma_CMS_deltaR_jetPt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut/"
#gridpack="ttGamma_CMS_deltaR_jetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut_xqcut/"
#gridpack="ttGamma_CMS_jetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noJetPtCut_xqcut_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut/"
#gridpack="ttGamma_CMS_deltaR_jetPt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta/"
#gridpack="ttGamma_CMS_dR_ptj_xq_etal_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_noDeltaR_noJetPtCut_xqcut_wideLepEta"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_largeBJetPt_xqcut/"
#gridpack="ttGamma_CMS_largeBJetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_largeBJetPt_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_CMSrunCard_largeJetPt_xqcut/"
#gridpack="ttGamma_CMS_largeJetPt_xqcut_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_CMSrunCard_largeJetPt_xqcut"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_TTBarrunCard/"
#gridpack="ttGamma_ttbar_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_TTBarrunCard_v2"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_TTBarrunCard_modified/"
#gridpack="ttGamma_ttbarMod_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_TTBarrunCard_modified"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/SM/ttGamma_1Line_noFullyHad_TTBarrunCard_mllOnly/"
#gridpack="ttGamma_ttbarModmllOnly_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_noFullyHad_TTBarrunCard_mllOnly"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish


#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_Dilept/"
#gridpack="ttGamma_Dilept_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_Dilept"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_SemiLept/"
#gridpack="ttGamma_SemiLept_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_SemiLept"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_Had/"
#gridpack="ttGamma_Had_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_Had"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_NoFullyHad/"
#gridpack="ttGamma_NoFullyHad_5f_ckm_LO_1line_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_NoFullyHad"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/ttgamma/cmssw930/ttGamma_NoFullyHad_noAuto/"
#gridpack="ttGamma_NoFullyHad_5f_ckm_LO_1line_noAuto_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz"
#label="ttGamma_1Line_NoFullyHad_noAuto"
#python launch_GEN.py $@ --config gen_LO_0j_mc_931 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/"
#gridpack="ttW01j_rwgt_mg265_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz"
#label="ttW01j_rwgt_mg265_v1"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="reduced_tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 200 --totalUnits 10000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="reduced_tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt_v1"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="tZZ1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tZZ1j_rwgt_v1"
#python launch_GEN.py $@ --config gensim_LO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="tWW1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWW1j_rwgt_v1"
#python launch_GEN.py $@ --config gensim_LO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="reduced_tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt_v2"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="reduced_tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt_test"
#python launch_GEN.py $@ --config gen_LO_01j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 200 --totalUnits 10000  --gridpackDir ${dir} --gridpack ${gridpack} --publish


###############################################################################

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="tZZ1j_4l_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tZZ1j_4l_rwgt"
#python launch_GEN.py $@ --config gensim_LO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/cms04/ttschida/gridpacks/Yt/"
#gridpack="tWW1j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWW1j_rwgt"
#python launch_GEN.py $@ --config gensim_LO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/cms04/ttschida/gridpacks/Yt/"
#gridpack="tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/cms04/ttschida/gridpacks/dim6top/"
#gridpack="ttW01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="ttW01j_rwgt_dim6top"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="ttWW_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="ttWW_rwgt"
#python launch_GEN.py $@ --config gensim_LO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/Yt/"
#gridpack="tttt_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tttt_rwgt"
#python launch_GEN.py $@ --config gensim_LO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 1000 --totalUnits 1000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/cms04/ttschida/gridpacks/"
#gridpack="tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt_filter"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1_twz_filter --production_label ${label} --unitsPerJob 50000 --totalUnits 500000000 --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/cms04/ttschida/gridpacks/"
#gridpack="tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt_filter_2"
#python launch_GEN.py $@ --config gensim_LO_01j_mc_71X_CUEP8M1_twz_filter --production_label ${label} --unitsPerJob 3000 --totalUnits 30000000 --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/dim6top/"
#gridpack="tWZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ0j_rwgt_filter_dim6top"
#python launch_GEN.py $@ --config gen_LO_0j_mc_71X_CUEP8M1_twz_filter --production_label ${label} --unitsPerJob 3000 --totalUnits 30000000 --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/rschoefbeck01/gridpacks/dim6top/"
#gridpack="tWZ01j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ01j_rwgt_filter_dim6top"
#python launch_GEN.py $@ --config gen_LO_01j_mc_71X_CUEP8M1_twz_filter --production_label ${label} --unitsPerJob 3000 --totalUnits 30000000 --gridpackDir ${dir} --gridpack ${gridpack} --publish

#dir="/afs/hephy.at/data/llechner03/tWZ/"
#gridpack="tWZ_NLO_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz"
#label="tWZ_NLO_v16_2"
#python launch_GEN.py $@ --config gen_NLO_0j_mc_71X_CUEP8M1 --production_label ${label} --unitsPerJob 100 --totalUnits 100 --gridpackDir ${dir} --gridpack ${gridpack} --publish


#dir="/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/WAToLNuA0123j_5f_LO_MLM/"
#gridpack="WAToLNuA0123j_5f_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz"
#label="WGToLNuG_MLM_A18_test"
#echo "python launch_GEN.py $@ --config gensim_WG_LO_Autumn18 --production_label ${label} --unitsPerJob 200 --totalUnits 1000  --gridpackDir ${dir} --gridpack ${gridpack} --publish"

#dir="/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/WAToLNuA0123j_5f_LO_MLM/"
#gridpack="WAToLNuA0123j_5f_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz"
#label="WGToLNuG_MLM_Fall17"
#python launch_GEN.py $@ --config gensim_WG_LO_Fall17 --production_label ${label} --unitsPerJob 3000 --totalUnits 30000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish


#dir="/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.2.2/WAToLNuA0123j_5f_LO_MLM/v1/"
#gridpack="WAToLNuA0123j_5f_LO_MLM_tarball.tar.xz"
#label="WGToLNuG_MLM_S16_test"
#echo "python launch_GEN.py $@ --config gensim_WG_LO_Summer16 --production_label ${label} --unitsPerJob 200 --totalUnits 1000  --gridpackDir ${dir} --gridpack ${gridpack} --publish"
#

#/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/vec/ttZ01j-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/vec/WZTo3L1Nu-vec-rw_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/vec/WZTo3L1Nu-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/vec/ZZ-vec-rw_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#/eos/vbc/user/robert.schoefbeck/gridpacks/flavor/vec/ZZ-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz

#dir="/eos/vbc/user/robert.schoefbeck/gridpacks/v7/"

#label="WGjj_VBF"
#python launch_GEN.py $@ --config gen_LO_0j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WGjj_VBF_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="WGToLNu"
#python launch_GEN.py $@ --config gen_LO_012j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WGToLNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="ZZjj_VBF"
#python launch_GEN.py $@ --config gen_LO_0j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack ZZjj_VBF_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="ZZ"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack ZZ_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 

#label="WG20To130ToLNu"
#python launch_GEN.py $@ --config gen_LO_012j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WG20To130ToLNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="WG130To300ToLNu"
#python launch_GEN.py $@ --config gen_LO_012j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WG130To300ToLNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="WG300To500ToLNu"
#python launch_GEN.py $@ --config gen_LO_012j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WG300To500ToLNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="WG500ToLNu"
#python launch_GEN.py $@ --config gen_LO_012j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WG500ToLNu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#dir="/eos/vbc/user/robert.schoefbeck/gridpacks/VH/"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label WH --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WH_WToLNu_1j_SMEFTsim_topU3l_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ZH --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack ZH_ZToLL_1j_SMEFTsim_topU3l_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz

#python launch_GEN.py $@ --config gen_LO_0123j_mc_102X_CP5_semiLepFilter --production_label TTJets_LO_semiLepFilter --unitsPerJob 30000 --totalUnits 30000000 --publish --gridpackDir /cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/tt0123j_5f_ckm_LO_MLM/v1/ --gridpack tt0123j_5f_ckm_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz

#dir="/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/tt0123j_5f_ckm_HT_LO_MLM/v2/"
#python launch_GEN.py $@ --config gen_LO_0123j_mc_102X_CP5_semiLepFilter --production_label TTJets_LO_semiLepFilter_HT-600to800 --unitsPerJob 30000 --totalUnits 10000000 --publish --gridpackDir ${dir} --gridpack tt0123j_5f_ckm_HT-600to800_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_0123j_mc_102X_CP5_semiLepFilter --production_label TTJets_LO_semiLepFilter_HT-800to1200 --unitsPerJob 30000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack tt0123j_5f_ckm_HT-800to1200_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_0123j_mc_102X_CP5_semiLepFilter --production_label TTJets_LO_semiLepFilter_HT-1200to2500 --unitsPerJob 30000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack tt0123j_5f_ckm_HT-1200to2500_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz                   
#python launch_GEN.py $@ --config gen_LO_0123j_mc_102X_CP5_semiLepFilter --production_label TTJets_LO_semiLepFilter_HT-2500toInf --unitsPerJob 30000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack tt0123j_5f_ckm_HT-2500toInf_LO_MLM_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz

#WJets
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir /cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/WJetsToLNu-madgraphMLM/  --gridpack WJetsToLNu_13TeV-madgraphMLM-pythia8_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#dir="/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.6.5/WJetsToLNu_HT/WJetsToLNu_HT"
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-70to100    --unitsPerJob 10000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-70to100_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-100to200   --unitsPerJob 10000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-100to200_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz    
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-200to400   --unitsPerJob 10000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-200to400_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz    
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-400to600   --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-400to600_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-600to800   --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-600to800_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-800to1200  --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-800to1200_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-1200to2500 --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-1200to2500_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz  
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label WJetsToLNu_HT-2500toInf  --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack WJetsToLNu_HT-2500toInf_slc6_amd64_gcc630_CMSSW_9_3_8_tarball.tar.xz   

#DY
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label DYJets --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir /cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/DYJets_HT_mll50/DYJets_HT-incl/  --gridpack DYJets_HT-incl_slc6_amd64_gcc481_CMSSW_7_1_30_tarball_v1.tar.xz
#dir="/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/DYJets_HT_mll50"
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-70to100 --unitsPerJob 10000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-70to100_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-100to200 --unitsPerJob 10000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-100to200_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz                  
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-200to400 --unitsPerJob 10000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-200to400_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz                  
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-400to600 --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-400to600_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-600to800 --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-600to800_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-800to1200 --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-800to1200_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-1200to2500 --unitsPerJob 5000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-1200to2500_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz                
#python launch_GEN.py $@ --config gen_LO_01234j_mc_102X_CP5 --production_label  DYJets_HT-2500toInf-ext --unitsPerJob 2000 --totalUnits 1000000 --publish --gridpackDir ${dir} --gridpack DYJets_HT-2500toInf_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz                 


#label="flavor_vec_gen_ttZ01j"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack ttZ01j-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="flavor_vec_gen_WZTo3L1Nu"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WZTo3L1Nu-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="flavor_vec_gen_ZZ"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack ZZ-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="flavor_vec-cw_gen_WZTo3L1Nu"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 30000000 --publish --gridpackDir ${dir} --gridpack WZTo3L1Nu-vec-cw_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 

#dir="/mnt/hephy/cms/robert.schoefbeck/gridpacks/SMEFTsim_general/flavor_v1/"
#
#label="SMEFTsim_general_flavor_v1_ttZ01j"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack ttZ01j_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz
#label="SMEFTsim_general_flavor_v1_WZTo3L1Nu"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack WZTo3L1Nu_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
#label="SMEFTsim_general_flavor_v1_ZZ"
#python launch_GEN.py $@ --config gen_LO_01j_mc_102X_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 5000000 --publish --gridpackDir ${dir} --gridpack ZZ_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 


python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5_filter1LepW --production_label tWZtoLL01j_lepWFilter --unitsPerJob 5000 --totalUnits 5000000 --publish --gridpackDir /eos/vbc/user/robert.schoefbeck/gridpacks/dennis/ --gridpack tWZtoLL01j-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5_filter1LepW --production_label ttZ01j_lepWFilter --unitsPerJob 5000 --totalUnits 10000000 --publish --gridpackDir /eos/vbc/user/robert.schoefbeck/gridpacks/dennis/ --gridpack ttZtoLL01j-vec_slc7_amd64_gcc700_CMSSW_10_6_19_tarball.tar.xz 
