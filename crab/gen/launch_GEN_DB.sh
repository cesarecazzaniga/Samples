
dir="/eos/vbc/user/robert.schoefbeck/gridpacks/v6/"

#gridpack="WW_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WW-v6"
#python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 4000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WZTo3L1Nu_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WZTo3L1Nu-v6"
#python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 4000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WZTojj2L_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WZTojj2L-v6"
#python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 4000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WZToLNujj_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WZToLNujj-v6"
#python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5 --production_label ${label} --unitsPerJob 2000 --totalUnits 4000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ZGTo2L_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ZGTo2L-v6"
#python launch_GEN.py $@ --config genToReco_LO_012j_mc_fast_10_2_22_CP5 --production_label ${label} --unitsPerJob 3000 --totalUnits 20000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WGToLNu_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WGToLNu-v6"
#python launch_GEN.py $@ --config genToReco_LO_012j_mc_fast_10_2_22_CP5  --production_label ${label} --unitsPerJob 3000 --totalUnits 20000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ttG_noFullyHad_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ttG_noFullyHad-v6"
#python launch_GEN.py $@ --config genToReco_LO_0j_mc_fast_10_2_22_CP5  --production_label ${label} --unitsPerJob 3000 --totalUnits 20000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#gridpack="ttW01j_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ttW01j-v6"
#python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5  --production_label ${label} --unitsPerJob 2000 --totalUnits 4000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#gridpack="ttZ01j_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ttZ01j-v6"
#python launch_GEN.py $@ --config genToReco_LO_01j_mc_fast_10_2_22_CP5  --production_label ${label} --unitsPerJob 2000 --totalUnits 4000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

dir="/mnt/hephy/cms/lukas.lechner/TTGammaEFT/gridpacks/SM/SMEFTatNLO/ttg_NoFullyHad/"


gridpack="ttG_noFullyHad_SM_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
label="ttG_noFullyHad_SM-v6"
python launch_GEN.py $@ --config genToReco_LO_0j_mc_fast_10_2_22_CP5  --production_label ${label} --unitsPerJob 3000 --totalUnits 20000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
