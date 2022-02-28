from hashlib import new
from operator import ne
import string


file = open("/home/subin/son_test/DlRlcStats_random.txt", "r")
# file_write = open("/home/subin/son_test/DlRlcStats_analyze_result.txt", "w")
strings = file.readlines()

# print(strings)
# print(len(strings))

line = []
new_data = []

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
    
for i in range(1,61):
    cell_1.append(globals()['totalbytes_1_{}'.format(i)])
    cell_2.append(globals()['totalbytes_2_{}'.format(i)])
    cell_3.append(globals()['totalbytes_3_{}'.format(i)])
    cell_4.append(globals()['totalbytes_4_{}'.format(i)])
    cell_5.append(globals()['totalbytes_5_{}'.format(i)])
    cell_6.append(globals()['totalbytes_6_{}'.format(i)])

print(cell_1)
print(cell_2)
print(cell_3)
print(cell_4)
print(cell_5)
print(cell_6)

total_throughput = [cell_1 +cell_2 +cell_3 +cell_4 +cell_5 +cell_6 for cell_1,cell_2,cell_3,cell_4,cell_5,cell_6 in zip (cell_1,cell_2,cell_3,cell_4,cell_5,cell_6)]

# total_throughput_1 = cell_1 +cell_2 +cell_3 +cell_4 +cell_5 +cell_6
# total_throughput_1.append(cell_1[1])
# total_throughput_1.append(cell_2[1])
# total_throughput_1.append(cell_3[1])
# total_throughput_1.append(cell_4[1])
# total_throughput_1.append(cell_5[1])
# total_throughput_1.append(cell_6[1])
print(total_throughput)