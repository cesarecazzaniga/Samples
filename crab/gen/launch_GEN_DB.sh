
dir="/eos/vbc/user/robert.schoefbeck/gridpacks/"

#gridpack="WW_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WW-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WZ_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WZ-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ZZ_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ZZ-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 50000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ZZZ_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ZZZ-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 20000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WZZ_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WZZ-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WWZ_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WWZ-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WWW_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WWW-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish


#gridpack="WA_LO_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WA_LO-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5  --production_label ${label} --unitsPerJob 50000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#gridpack="WA_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WA-v4"
#python launch_GEN.py $@ --config gen_LO_012j_mc_93X_CP5  --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WWjj_OS_ewk_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WWjj_OS-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WWjj_SS_ewk_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WWjj_SS-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WZjj_ewk_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WZjj-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

gridpack="ZA_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
label="ZA-v4"
python launch_GEN.py $@ --config gen_LO_012j_mc_93X_CP5  --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ZAjj_ewk_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ZAjj-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ZZjj_ewk_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ZZjj-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="WAjj_ewk_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="WAjj-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish
#
#gridpack="ttg_noFullyHad_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ttg_noFullyHad-v4"
#python launch_GEN.py $@ --config gen_LO_0j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#gridpack="ttW01j_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ttW01j-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

#gridpack="ttZ_slc7_amd64_gcc700_CMSSW_10_6_0_tarball.tar.xz"
#label="ttZ01j-v4"
#python launch_GEN.py $@ --config gen_LO_01j_mc_93X_CP5 --production_label ${label} --unitsPerJob 5000 --totalUnits 10000000  --gridpackDir ${dir} --gridpack ${gridpack} --publish

