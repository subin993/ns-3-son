from hashlib import new
from operator import ne
from re import X
import string
import numpy as numpy
from matplotlib import pyplot as plt

cell1 = [27.85,37.1429,35]
cell2 = [20,50,30]
cell3 = []
cell4 = []
cell5 = []
cell6 = []


x = numpy.arange(70)
indexmat = ['cell1_mlb', 'cell2_mlb', 'cell3_mlb', 'cell1_non', 'cell2_non', 'cell3_non']
indexmat_alg = x
plt.bar(indexmat[:3], cell1)
plt.bar(indexmat[3:6], cell2)
# plt.bar(indexmat[:3], cell2[:3])
# plt.xlabel("Time")
plt.ylabel("Average PrbUsage")
plt.savefig('PRB_compare_temp.png')