from cProfile import label
from hashlib import new
from operator import ne
from re import X
import string
import numpy as numpy
from matplotlib import pyplot as plt


file = open("/home/subin/son_test/DlRlcStats_analyze_result.txt", "r")
# file_write = open("/home/subin/son_test/DlRlcStats_analyze_result.txt", "w")
strings = file.readlines()

# print(strings)
# print(len(strings))

line = []
new_data = []
cell1 = []
cell2 = []
cell3 = []
cell4 = []
cell5 = []
cell6 = []
cell_total = []
cell_total_alg = []

for i in strings:
    # print i.splitlines()
    line_list = i.splitlines()[0]
    new_data.append(line_list.split('\t'))

for i in range(len(new_data)):
    # print(new_data[i][1])
    cell1.append(new_data[i][1])
    cell2.append(new_data[i][2])
    cell3.append(new_data[i][3])
    # cell4.append(new_data[i][4])
    # cell5.append(new_data[i][5])
    # cell6.append(new_data[i][6])
    cell_total_alg.append(new_data[i][6])
    cell_total.append(new_data[i][7])

cell1_list = list(map(int, cell1))
cell2_list = list(map(int, cell2))
cell3_list = list(map(int, cell3))
cell4_list = list(map(int, cell4))
cell5_list = list(map(int, cell5))
cell6_list = list(map(int, cell6))
cell_total_list = list(map(float, cell_total))
cell_total_list_alg = list(map(float, cell_total_alg))

print(cell1_list)
print(cell2_list)
print(cell3_list)
print(cell4_list)
print(cell5_list)
print(cell6_list)
print(cell_total_list)
print(cell_total_list_alg)

x = numpy.arange(70)
indexmat = x
indexmat_alg = x
plt.plot(indexmat[1:65], cell_total_list_alg[1:65], label='MLB')
plt.plot(indexmat[1:65], cell_total_list[1:65], label='Non-MLB')
plt.legend()
plt.xlabel("Time")
plt.ylabel("Throughput(Mbps)")
# plt.show
plt.savefig('Total_graph_compare_temp.png')