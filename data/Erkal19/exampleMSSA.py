#pyEXP on cuillin

srun -n8 --pty $SHELL
cd /disk01/mpetersen/Disk076

python

import os, sys
sys.path.append('/home/mpetersen/lib/python3.10/site-packages')
import pyEXP

os.chdir('/disk01/mpetersen/Disk076')


runtag = 'run9mlde'


mwconfig = """
id: sphereSL
parameters:
  numr: 4000
  rmin: 0.000001
  rmax: 5.0
  Lmax: 6
  nmax: 18
  scale: 1.
  modelname: ErkalMW.model
  #cachename: SLGridSph.mw.pyEXP
"""
mwbasis = pyEXP.basis.Basis.factory(mwconfig)

mwcoefs = pyEXP.coefs.Coefs.factory('outcoef.mw.run9mlde')

print("Got coefs for name=", mwcoefs.getName())

# get all keys for l=1 harmonic order
keylst = mwcoefs.makeKeys([1])
print("Keys=", keylst)

config = {"mw": (mwcoefs, keylst, [])}

config = {"mw": (mwcoefs, keylst[0:10], [])}

window = int(len(mwcoefs.Times())/2)
npc = 10

print("Window={} PC number={}".format(window, npc))

ssa = pyEXP.mssa.expMSSA(config, window, npc)
ev = ssa.eigenvalues()

times = mwcoefs.Times();
pc    = ssa.getPC();

# make a deepcopy of the original coefs
originalmwcoefs = deepcopy(mwcoefs)
originalmwcoefs = pyEXP.coefs.Coefs.factory('outcoef.mw.run9mlde')


# this needs arguments
ssa.reconstruct([*range(10)])

newdata = ssa.getReconstructed()
print('newdata is a', type(newdata))



lmcconfig = """
id: sphereSL
parameters:
  numr: 4000
  rmin: 0.000001
  rmax: 5.0
  Lmax: 6
  nmax: 24
  scale: 1.0
  modelname: ErkalLMC.model
  cachename: SLGridSph.lmc.pyEXP
"""
lmcbasis = pyEXP.basis.Basis.factory(lmcconfig)

lmccoefs = pyEXP.coefs.Coefs.factory('outcoef.lmc.run9mlde')


