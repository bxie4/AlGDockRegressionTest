# The example is 1of6

import AlGDock.BindingPMF_plots
import os, shutil, glob

os.system('rm -rf cool dock')

import cProfile
import re
cProfile.run("self = AlGDock.BindingPMF_plots.BPMF_plots(\
  dir_dock='dock', dir_cool='cool',\
  ligand_tarball='prmtopcrd/ligand.tar.gz', \
  ligand_database='ligand.db', \
  forcefield='prmtopcrd/gaff.dat', \
  ligand_prmtop='ligand.prmtop', \
  ligand_inpcrd='ligand.trans.inpcrd', \
  receptor_tarball='prmtopcrd/receptor.tar.gz', \
  receptor_prmtop='receptor.prmtop', \
  receptor_inpcrd='receptor.trans.inpcrd', \
  receptor_fixed_atoms='receptor.pdb', \
  complex_tarball='prmtopcrd/complex.tar.gz', \
  complex_prmtop='complex.prmtop', \
  complex_inpcrd='complex.trans.inpcrd', \
  complex_fixed_atoms='complex.pdb', \
  score = 'prmtopcrd/anchor_and_grow_scored.mol2', \
  dir_grid='grids', \
  protocol='Adaptive', cool_therm_speed=1.5, dock_therm_speed=1.5,\
  sampler='NUTS', \
  MCMC_moves=1, \
  seeds_per_state=10, steps_per_seed=200, darts_per_seed=5, \
  sweeps_per_cycle=25, attempts_per_sweep=100, \
  steps_per_sweep=50, darts_per_sweep=5, \
  cool_repX_cycles=3, dock_repX_cycles=4, \
  site='Sphere', site_center=[1.74395, 1.74395, 1.74395], site_max_R=0.6, \
  site_density=10., \
  phases=['NAMD_Gas','NAMD_GBSA'], \
  cores=1, \
  rmsd=True, \
  run_type='cool', random_seed=50)","cool_stats")

import pstats
p = pstats.Stats("cool_stats")
p.strip_dirs().sort_stats('tottime').print_stats(100)

# NO DARTS:
#         3578894 function calls (3534894 primitive calls) in 12.659 seconds
#  calculated NAMD_GBSA solvation free energy of -77.055740 RT using cycles 0 to 0
#  calculated NAMD_GBSA solvation free energy of -73.947292 RT using cycles 1 to 1
#  calculated NAMD_GBSA solvation free energy of -75.163298 RT using cycles 1 to 2
#         3570175 function calls (3527205 primitive calls) in 13.055 seconds
#  calculated NAMD_GBSA solvation free energy of -77.055740 RT using cycles 0 to 0
#  calculated NAMD_GBSA solvation free energy of -73.947292 RT using cycles 1 to 1
#  calculated NAMD_GBSA solvation free energy of -75.163298 RT using cycles 1 to 2

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      370    3.495    0.009    5.157    0.014 BindingPMF.py:2309(_sim_one_state)
#   171080    1.516    0.000    2.103    0.000 ChemicalObjects.py:578(position)
#        1    1.280    1.280    8.457    8.457 BindingPMF.py:685(initial_cool)
#   239690    1.074    0.000    1.074    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#        6    0.773    0.129    0.773    0.129 {posix.waitpid}
#    85540    0.596    0.000    2.998    0.000 Universe.py:868(distanceVector)
#   427858    0.551    0.000    0.551    0.000 {numpy.core.multiarray.array}
#        2    0.350    0.175    0.358    0.179 IO.py:204(read)
#1737/1736    0.305    0.000    0.503    0.000 {apply}
#        2    0.270    0.135    2.914    1.457 BindingPMF.py:1959(_replica_exchange)
#      810    0.212    0.000    0.212    0.000 {built-in method compress}
#   171080    0.150    0.000    2.348    0.000 Universe.py:389(position)

# >>> With DARTS
#  calculated NAMD_GBSA solvation free energy of -75.796975 RT using cycles 0 to 0
#  calculated NAMD_GBSA solvation free energy of -73.347731 RT using cycles 1 to 1
#  calculated NAMD_GBSA solvation free energy of -78.163444 RT using cycles 1 to 2
#
#           6560764 function calls (6479732 primitive calls) in 20.062 seconds
#
#     Ordered by: internal time
#     List reduced from 1173 to 100 due to restriction <100>
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     588460    4.411    0.000    5.951    0.000 ChemicalObjects.py:578(position)
#        310    2.232    0.007   13.960    0.045 BindingPMF.py:2309(_sim_one_state)
#     654382    2.118    0.000    2.118    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#          1    1.145    1.145    7.203    7.203 BindingPMF.py:685(initial_cool)
#      34100    0.814    0.000    1.913    0.000 Objects3D.py:313(_intersectCirclePlane)
#          5    0.769    0.154    0.769    0.154 {posix.waitpid}
#      32550    0.717    0.000    0.863    0.000 Objects3D.py:338(rotateDirection)
#       1550    0.601    0.000    8.420    0.005 BAT.py:113(Cartesian)
#      98930    0.562    0.000    2.877    0.000 Universe.py:868(distanceVector)
#     343695    0.424    0.000    0.424    0.000 {numpy.core.multiarray.array}
#      34100    0.420    0.000    0.482    0.000 Objects3D.py:285(_intersectSphereCone)
#     100750    0.370    0.000    0.409    0.000 Objects3D.py:120(__init__)
#          2    0.362    0.181    0.368    0.184 IO.py:204(read)
#     637361    0.348    0.000    0.348    0.000 {hasattr}
#      34100    0.344    0.000    0.446    0.000 Objects3D.py:296(_intersectPlanePlane)
#  3342/3341    0.321    0.000    0.520    0.000 {apply}
#      68200    0.308    0.000    0.380    0.000 Objects3D.py:238(distanceFrom)
#          2    0.235    0.118   11.161    5.581 BindingPMF.py:1959(_replica_exchange)
#        792    0.235    0.000    0.235    0.000 {built-in method compress}
#     197860    0.167    0.000    2.259    0.000 Universe.py:389(position)
#

# >>> Calculating BAT directly operating on numpy arrays
#  calculated NAMD_GBSA solvation free energy of -75.796975 RT using cycles 0 to 0
#  calculated NAMD_GBSA solvation free energy of -73.347731 RT using cycles 1 to 1
#  calculated NAMD_GBSA solvation free energy of -78.163444 RT using cycles 1 to 2
#
#           6716013 function calls (6634981 primitive calls) in 18.511 seconds
#
#     Ordered by: internal time
#     List reduced from 1176 to 100 due to restriction <100>
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     390600    2.848    0.000    3.830    0.000 ChemicalObjects.py:578(position)
#        310    2.214    0.007   13.148    0.042 BindingPMF.py:2309(_sim_one_state)
#     460327    1.574    0.000    1.574    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#          1    1.151    1.151    6.687    6.687 BindingPMF.py:685(initial_cool)
#      34100    0.802    0.000    1.882    0.000 Objects3D.py:313(_intersectCirclePlane)
#          6    0.776    0.129    0.776    0.129 {posix.waitpid}
#      32550    0.696    0.000    0.837    0.000 Objects3D.py:338(rotateDirection)
#       1550    0.591    0.000    8.220    0.005 BAT.py:162(Cartesian)
#     823045    0.538    0.000    0.538    0.000 {hasattr}
#      95886    0.528    0.000    1.457    0.000 Universe.py:868(distanceVector)
#     343695    0.430    0.000    0.430    0.000 {numpy.core.multiarray.array}
#      34100    0.418    0.000    0.480    0.000 Objects3D.py:285(_intersectSphereCone)
#          2    0.376    0.188    0.382    0.191 IO.py:204(read)
#     100750    0.368    0.000    0.407    0.000 Objects3D.py:120(__init__)
#     191772    0.357    0.000    0.876    0.000 Universe.py:389(position)
#      34100    0.330    0.000    0.431    0.000 Objects3D.py:296(_intersectPlanePlane)
#  3342/3341    0.326    0.000    0.523    0.000 {apply}
#      68200    0.307    0.000    0.378    0.000 Objects3D.py:238(distanceFrom)
#          2    0.238    0.119   10.104    5.052 BindingPMF.py:1959(_replica_exchange)
#        792    0.231    0.000    0.231    0.000 {built-in method compress}
#     191772    0.169    0.000    0.169    0.000 {Scientific._vector.isVector}


# >>> Calculating bonds, angles, and torsions together in BAT routine
# Somehow the numbers are slightly different
#  calculated NAMD_GBSA solvation free energy of -76.827563 RT using cycles 0 to 0
#  calculated NAMD_GBSA solvation free energy of -75.392861 RT using cycles 1 to 1
#  calculated NAMD_GBSA solvation free energy of -76.801582 RT using cycles 1 to 2
#
#           5997853 function calls (5914668 primitive calls) in 17.658 seconds
#
#     Ordered by: internal time
#     List reduced from 1169 to 100 due to restriction <100>
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     403200    2.743    0.000    3.691    0.000 ChemicalObjects.py:578(position)
#        320    2.157    0.007   12.538    0.039 BindingPMF.py:2309(_sim_one_state)
#     594374    1.831    0.000    1.831    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#          1    1.152    1.152    6.557    6.557 BindingPMF.py:685(initial_cool)
#      35200    0.767    0.000    1.810    0.000 Objects3D.py:313(_intersectCirclePlane)
#          5    0.687    0.137    0.687    0.137 {posix.waitpid}
#      33600    0.668    0.000    0.805    0.000 Objects3D.py:338(rotateDirection)
#       1600    0.532    0.000    7.835    0.005 BAT.py:175(Cartesian)
#     411652    0.479    0.000    0.479    0.000 {numpy.core.multiarray.array}
#      16842    0.468    0.000    1.599    0.000 BAT.py:38(BAT4)
#      35200    0.387    0.000    0.443    0.000 Objects3D.py:285(_intersectSphereCone)
#          2    0.370    0.185    0.376    0.188 IO.py:204(read)
#     104000    0.343    0.000    0.379    0.000 Objects3D.py:120(__init__)
#  3437/3436    0.325    0.000    0.522    0.000 {apply}
#      35200    0.316    0.000    0.412    0.000 Objects3D.py:296(_intersectPlanePlane)
#      70400    0.297    0.000    0.367    0.000 Objects3D.py:238(distanceFrom)
#     453616    0.293    0.000    0.293    0.000 {hasattr}
#      50526    0.278    0.000    0.345    0.000 BAT.py:13(cross)
#          2    0.220    0.110    9.509    4.755 BindingPMF.py:1959(_replica_exchange)
#      33684    0.210    0.000    0.384    0.000 BAT.py:10(normalize)
#     167440    0.177    0.000    0.934    0.000 fromnumeric.py:1621(sum)
#        665    0.168    0.000    0.168    0.000 {built-in method compress}

# >>> Direct access to positions when calculating Cartesian coordinates
#  calculated NAMD_GBSA solvation free energy of -76.827563 RT using cycles 0 to 0
#  calculated NAMD_GBSA solvation free energy of -75.392861 RT using cycles 1 to 1
#  calculated NAMD_GBSA solvation free energy of -76.801582 RT using cycles 1 to 2
#
#           5668253 function calls (5585068 primitive calls) in 15.920 seconds
#
#     Ordered by: internal time
#     List reduced from 1168 to 100 due to restriction <100>
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        320    2.271    0.007   10.382    0.032 BindingPMF.py:2309(_sim_one_state)
#       1600    1.204    0.001    5.376    0.003 BAT.py:168(Cartesian)
#          1    1.182    1.182    6.319    6.319 BindingPMF.py:685(initial_cool)
#     191174    0.976    0.000    0.976    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#          5    0.794    0.159    0.794    0.159 {posix.waitpid}
#      35200    0.787    0.000    1.833    0.000 Objects3D.py:313(_intersectCirclePlane)
#      33600    0.679    0.000    0.815    0.000 Objects3D.py:338(rotateDirection)
#      68800    0.624    0.000    0.812    0.000 Objects3D.py:296(_intersectPlanePlane)
#      16842    0.526    0.000    1.810    0.000 BAT.py:38(BAT4)
#     411652    0.513    0.000    0.513    0.000 {numpy.core.multiarray.array}
#     137600    0.412    0.000    0.454    0.000 Objects3D.py:120(__init__)
#      35200    0.392    0.000    0.452    0.000 Objects3D.py:285(_intersectSphereCone)
#          2    0.363    0.181    0.369    0.185 IO.py:204(read)
#     520816    0.341    0.000    0.341    0.000 {hasattr}
#  3437/3436    0.334    0.000    0.533    0.000 {apply}
#      50526    0.309    0.000    0.387    0.000 BAT.py:13(cross)
#      70400    0.306    0.000    0.379    0.000 Objects3D.py:238(distanceFrom)
#      33684    0.247    0.000    0.448    0.000 BAT.py:10(normalize)
#          2    0.234    0.117    7.873    3.936 BindingPMF.py:1959(_replica_exchange)
#     167440    0.193    0.000    1.035    0.000 fromnumeric.py:1621(sum)
#        665    0.173    0.000    0.173    0.000 {built-in method compress}
#  139200/104000    0.163    0.000    2.823    0.000 Objects3D.py:29(intersectWith)
#     518400    0.156    0.000    0.496    0.000 TensorModule.py:229(isTensor)

# >>> Cython BAT.pyx
#    calculated NAMD_GBSA solvation free energy of -76.803688 RT using cycles 0 to 0
#    calculated NAMD_GBSA solvation free energy of -76.932018 RT using cycles 1 to 1
#    calculated NAMD_GBSA solvation free energy of -70.874913 RT using cycles 2 to 2
#
#           3498364 function calls (3459134 primitive calls) in 13.323 seconds
#
#     Ordered by: internal time
#     List reduced from 1130 to 100 due to restriction <100>
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        240    4.412    0.018    6.704    0.028 SmartDarting.py:136(__call__)
#     460147    1.533    0.000    1.533    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#        240    1.525    0.006    8.965    0.037 BindingPMF.py:2309(_sim_one_state)
#          1    1.137    1.137    4.401    4.401 BindingPMF.py:685(initial_cool)
#          6    0.741    0.123    0.741    0.123 {posix.waitpid}
#     439150    0.443    0.000    2.288    0.000 fromnumeric.py:1621(sum)
#          2    0.356    0.178    0.362    0.181 IO.py:204(read)
#          6    0.354    0.059    0.565    0.094 SmartDarting.py:40(set_confs)
#  2638/2637    0.302    0.000    0.507    0.000 {apply}
#     441448    0.287    0.000    1.703    0.000 _methods.py:23(_sum)
#     289404    0.285    0.000    0.285    0.000 {numpy.core.multiarray.array}
#     477172    0.161    0.000    0.161    0.000 {isinstance}
#        515    0.151    0.000    0.151    0.000 {built-in method compress}

# >>> Extension type
#    calculated NAMD_GBSA solvation free energy of -76.803688 RT using cycles 0 to 0
#    calculated NAMD_GBSA solvation free energy of -76.932018 RT using cycles 1 to 1
#    calculated NAMD_GBSA solvation free energy of -70.874913 RT using cycles 2 to 2
#
#           3481075 function calls (3441845 primitive calls) in 13.049 seconds
#
#     Ordered by: internal time
#     List reduced from 1132 to 100 due to restriction <100>
#
#     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1200    3.870    0.003    5.530    0.005 {method 'Cartesian' of 'BAT.converter' objects}
#     460147    1.573    0.000    1.573    0.000 {method 'reduce' of 'numpy.ufunc' objects}
#        240    1.484    0.006    8.749    0.036 BindingPMF.py:2309(_sim_one_state)
#          1    1.129    1.129    4.367    4.367 BindingPMF.py:685(initial_cool)
#          5    0.713    0.143    0.713    0.143 {posix.waitpid}
#        496    0.672    0.001    1.052    0.002 {method 'BAT' of 'BAT.converter' objects}
#     439150    0.430    0.000    2.315    0.000 fromnumeric.py:1621(sum)
#          2    0.360    0.180    0.367    0.183 IO.py:204(read)
#  2638/2637    0.304    0.000    0.501    0.000 {apply}
#     441448    0.284    0.000    1.741    0.000 _methods.py:23(_sum)
#     289404    0.281    0.000    0.281    0.000 {numpy.core.multiarray.array}
#     477172    0.161    0.000    0.161    0.000 {isinstance}
#        515    0.153    0.000    0.153    0.000 {built-in method compress}