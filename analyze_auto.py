from hashlib import new
from operator import ne
import string
import numpy as numpy
from matplotlib import pyplot as plt


file_alg = open("/home/subin/son_test/DlRlcStats_random_alg.txt", "r")
# file_write = open("/home/subin/son_test/DlRlcStats_analyze_result.txt", "w")
strings = file_alg.readlines()
file_non_alg = open("/home/subin/son_test/DlRlcStats_random_non_alg.txt", "r")
# file_write = open("/home/subin/son_test/DlRlcStats_analyze_result.txt", "w")
strings_non_alg = file_non_alg.readlines()

# print(strings)
# print(len(strings))

line = []
new_data = []
new_data_non = []

for i in range(1, 10):
    globals()['cell_{}'.format(i)]= []

for i in range(1, 1000):
    globals()['totalbytes_1_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_2_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_3_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_4_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_5_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_6_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_7_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_8_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_9_{}'.format(i)]=0
    
for i in strings:
    # print i.splitlines()
    line_list = i.splitlines()[0]
    new_data.append(line_list.split('\t'))
# print(new_data)
for i in range(len(new_data)):
    # print(new_data[i][2])
    # print(type(new_data[i][2]))
    for j in range(1,1000):
        if new_data[i][2] == str(1):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_1_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(2):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_2_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(3):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_3_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(4):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_4_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(5):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_5_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(6):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_6_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(7):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_7_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(8):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_8_{}'.format(j)] += int(new_data[i][7])
    for j in range(1,1000):
        if new_data[i][2] == str(9):
            if str(j) == new_data[i][1]:
                globals()['totalbytes_9_{}'.format(j)] += int(new_data[i][7])
    
for i in range(1,558):
    cell_1.append(globals()['totalbytes_1_{}'.format(i)])
    cell_2.append(globals()['totalbytes_2_{}'.format(i)])
    cell_3.append(globals()['totalbytes_3_{}'.format(i)])
    cell_4.append(globals()['totalbytes_4_{}'.format(i)])
    cell_5.append(globals()['totalbytes_5_{}'.format(i)])
    cell_6.append(globals()['totalbytes_6_{}'.format(i)])
    cell_7.append(globals()['totalbytes_7_{}'.format(i)])
    cell_8.append(globals()['totalbytes_8_{}'.format(i)])
    cell_9.append(globals()['totalbytes_9_{}'.format(i)])

total_throughput = [cell_1 +cell_2 +cell_3 +cell_4 +cell_5 +cell_6 +cell_7 +cell_8 +cell_9 for cell_1,cell_2,cell_3,cell_4,cell_5,cell_6,cell_7,cell_8,cell_9 in zip (cell_1,cell_2,cell_3,cell_4,cell_5,cell_6,cell_7,cell_8,cell_9)]
# print(total_throughput)


for i in range(1, 10):
    globals()['cell_{}'.format(i)]= []

for i in range(1, 1000):
    globals()['totalbytes_1_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_2_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_3_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_4_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_5_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_6_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_7_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_8_{}'.format(i)]=0
for i in range(1, 1000):
    globals()['totalbytes_9_{}'.format(i)]=0

for i in strings_non_alg:
    # print i.splitlines()
    line_list = i.splitlines()[0]
    new_data_non.append(line_list.split('\t'))
# print(new_data)
for i in range(len(new_data_non)):
    # print(new_data[i][2])
    # print(type(new_data[i][2]))
    for j in range(1,1000):
        if new_data_non[i][2] == str(1):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_1_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(2):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_2_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(3):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_3_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(4):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_4_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(5):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_5_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(6):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_6_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(7):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_7_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(8):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_8_{}'.format(j)] += int(new_data_non[i][7])
    for j in range(1,1000):
        if new_data_non[i][2] == str(9):
            if str(j) == new_data_non[i][1]:
                globals()['totalbytes_9_{}'.format(j)] += int(new_data_non[i][7])
    
for i in range(1,558):
    cell_1.append(globals()['totalbytes_1_{}'.format(i)])
    cell_2.append(globals()['totalbytes_2_{}'.format(i)])
    cell_3.append(globals()['totalbytes_3_{}'.format(i)])
    cell_4.append(globals()['totalbytes_4_{}'.format(i)])
    cell_5.append(globals()['totalbytes_5_{}'.format(i)])
    cell_6.append(globals()['totalbytes_6_{}'.format(i)])
    cell_7.append(globals()['totalbytes_7_{}'.format(i)])
    cell_8.append(globals()['totalbytes_8_{}'.format(i)])
    cell_9.append(globals()['totalbytes_9_{}'.format(i)])

total_throughput_non_alg = [cell_1 +cell_2 +cell_3 +cell_4 +cell_5 +cell_6 +cell_7 +cell_8 +cell_9 for cell_1,cell_2,cell_3,cell_4,cell_5,cell_6,cell_7,cell_8,cell_9 in zip (cell_1,cell_2,cell_3,cell_4,cell_5,cell_6,cell_7,cell_8,cell_9)]

for i in range (556):
    total_throughput[i] = total_throughput[i] * 8 / 1000000
    total_throughput_non_alg[i] = total_throughput_non_alg[i] * 8 / 1000000
    
x = numpy.arange(1000)
indexmat = x
indexmat_alg = x
plt.plot(indexmat[0:50], total_throughput[0:50], label='MLB')
plt.plot(indexmat[0:50], total_throughput_non_alg[0:50], label='Non-MLB')
# plt.ylim(15,30)
plt.legend()
plt.xlabel("Time")
plt.ylabel("Throughput(Mbps)")
# plt.show
plt.savefig('total_test.png')