import numpy as np
import pyEXP
import sys
sys.path.append('../scf_coefficients/')
import scf_utils
#import matplotlib.pyplot as plt


sys.path.append("../../../../projects/cosmo_wakes/pyEXP_ex/")
import makemodel




coefs = pyEXP.coefs.Coefs.factory('m12i_test.dat')



config2 = """
---
id: sphereSL
parameters:
  numr: 2000
  rmin: -2
  rmax: 4
  Lmax: 1
  nmax: 10
  scale: 40
  modelname: hernquist_table.txt
...
"""

basis = pyEXP.basis.Basis.factory(config2)

basis.set_coefs(coefs.getCoefStruct(0.0))
