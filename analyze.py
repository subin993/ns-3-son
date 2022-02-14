from hashlib import new
from operator import ne
import string


file = open("/home/subin/son_test/DlRlcStats.txt", "r")
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

for i in range(1, 73):
    globals()['totalbytes_{}'.format(i)]=0
    
for i in strings:
    # print i.splitlines()
    line_list = i.splitlines()[0]
    new_data.append(line_list.split('\t'))
# print(new_data)
for i in range(len(new_data)):
    # print(new_data[i][2])
    # print(type(new_data[i][2]))
    if new_data[i][2]== str(2):
        if str(1) == new_data[i][1]:
            totalbytes_1 += int(new_data[i][7])
        if str(2) == new_data[i][1]:
            totalbytes_2 += int(new_data[i][7])
        if str(3) == new_data[i][1]:
            totalbytes_3 += int(new_data[i][7])
        if str(4) == new_data[i][1]:
            totalbytes_4 += int(new_data[i][7])
        if str(5) == new_data[i][1]:
            totalbytes_5 += int(new_data[i][7])
        if str(6) == new_data[i][1]:
            totalbytes_6 += int(new_data[i][7])
        if str(7) == new_data[i][1]:
            totalbytes_7 += int(new_data[i][7])
        if str(8) == new_data[i][1]:
            totalbytes_8 += int(new_data[i][7])
        if str(9) == new_data[i][1]:
            totalbytes_9 += int(new_data[i][7])
        if str(10) == new_data[i][1]:
            totalbytes_10 += int(new_data[i][7])
        if str(11) == new_data[i][1]:
            totalbytes_11 += int(new_data[i][7])
        if str(12) == new_data[i][1]:
            totalbytes_12 += int(new_data[i][7])
        if str(13) == new_data[i][1]:
            totalbytes_13 += int(new_data[i][7])
        if str(14) == new_data[i][1]:
            totalbytes_14 += int(new_data[i][7])
        if str(15) == new_data[i][1]:
            totalbytes_15 += int(new_data[i][7])
        if str(16) == new_data[i][1]:
            totalbytes_16 += int(new_data[i][7])
        if str(17) == new_data[i][1]:
            totalbytes_17 += int(new_data[i][7])
        if str(18) == new_data[i][1]:
            totalbytes_18 += int(new_data[i][7])
        if str(19) == new_data[i][1]:
            totalbytes_19 += int(new_data[i][7])
        if str(20) == new_data[i][1]:
            totalbytes_20 += int(new_data[i][7])
        if str(21) == new_data[i][1]:
            totalbytes_21 += int(new_data[i][7])
        if str(22) == new_data[i][1]:
            totalbytes_22 += int(new_data[i][7])
        if str(23) == new_data[i][1]:
            totalbytes_23 += int(new_data[i][7])
        if str(24) == new_data[i][1]:
            totalbytes_24 += int(new_data[i][7])
        if str(25) == new_data[i][1]:
            totalbytes_25 += int(new_data[i][7])
        if str(26) == new_data[i][1]:
            totalbytes_26 += int(new_data[i][7])
        if str(27) == new_data[i][1]:
            totalbytes_27 += int(new_data[i][7])
        if str(28) == new_data[i][1]:
            totalbytes_28 += int(new_data[i][7])
        if str(29) == new_data[i][1]:
            totalbytes_29 += int(new_data[i][7])
        if str(30) == new_data[i][1]:
            totalbytes_30 += int(new_data[i][7])
        if str(31) == new_data[i][1]:
            totalbytes_31 += int(new_data[i][7])
        if str(32) == new_data[i][1]:
            totalbytes_32 += int(new_data[i][7])
        if str(33) == new_data[i][1]:
            totalbytes_33 += int(new_data[i][7])
        if str(34) == new_data[i][1]:
            totalbytes_34 += int(new_data[i][7])
        if str(35) == new_data[i][1]:
            totalbytes_35 += int(new_data[i][7])
        if str(36) == new_data[i][1]:
            totalbytes_36 += int(new_data[i][7])
        if str(37) == new_data[i][1]:
            totalbytes_37 += int(new_data[i][7])
        if str(38) == new_data[i][1]:
            totalbytes_38 += int(new_data[i][7])
        if str(39) == new_data[i][1]:
            totalbytes_39 += int(new_data[i][7])
        if str(40) == new_data[i][1]:
            totalbytes_40 += int(new_data[i][7])
        if str(41) == new_data[i][1]:
            totalbytes_41 += int(new_data[i][7])
        if str(42) == new_data[i][1]:
            totalbytes_42 += int(new_data[i][7])
        if str(43) == new_data[i][1]:
            totalbytes_43 += int(new_data[i][7])
        if str(44) == new_data[i][1]:
            totalbytes_44 += int(new_data[i][7])
        if str(45) == new_data[i][1]:
            totalbytes_45 += int(new_data[i][7])
        if str(46) == new_data[i][1]:
            totalbytes_46 += int(new_data[i][7])
        if str(47) == new_data[i][1]:
            totalbytes_47 += int(new_data[i][7])
        if str(48) == new_data[i][1]:
            totalbytes_48 += int(new_data[i][7])
        if str(49) == new_data[i][1]:
            totalbytes_49 += int(new_data[i][7])
        if str(50) == new_data[i][1]:
            totalbytes_50 += int(new_data[i][7])
        if str(51) == new_data[i][1]:
            totalbytes_51 += int(new_data[i][7])
        if str(52) == new_data[i][1]:
            totalbytes_52 += int(new_data[i][7])
        if str(53) == new_data[i][1]:
            totalbytes_53 += int(new_data[i][7])
        if str(54) == new_data[i][1]:
            totalbytes_54 += int(new_data[i][7])
        if str(55) == new_data[i][1]:
            totalbytes_55 += int(new_data[i][7])
        if str(56) == new_data[i][1]:
            totalbytes_56 += int(new_data[i][7])
        if str(57) == new_data[i][1]:
            totalbytes_57 += int(new_data[i][7])
        if str(58) == new_data[i][1]:
            totalbytes_58 += int(new_data[i][7])
        if str(59) == new_data[i][1]:
            totalbytes_59 += int(new_data[i][7])
        if str(60) == new_data[i][1]:
            totalbytes_60 += int(new_data[i][7])
        if str(61) == new_data[i][1]:
            totalbytes_61 += int(new_data[i][7])
        if str(62) == new_data[i][1]:
            totalbytes_62 += int(new_data[i][7])
        if str(63) == new_data[i][1]:
            totalbytes_63 += int(new_data[i][7])
        if str(64) == new_data[i][1]:
            totalbytes_64 += int(new_data[i][7])
        if str(65) == new_data[i][1]:
            totalbytes_65 += int(new_data[i][7])
        if str(66) == new_data[i][1]:
            totalbytes_66 += int(new_data[i][7])


cell1.append(totalbytes_1)
cell1.append(totalbytes_2)
cell1.append(totalbytes_3)
cell1.append(totalbytes_4)
cell1.append(totalbytes_5)
cell1.append(totalbytes_6)
cell1.append(totalbytes_7)
cell1.append(totalbytes_8)
cell1.append(totalbytes_9)
cell1.append(totalbytes_10)
cell1.append(totalbytes_11)
cell1.append(totalbytes_12)
cell1.append(totalbytes_13)
cell1.append(totalbytes_14)
cell1.append(totalbytes_15)
cell1.append(totalbytes_16)
cell1.append(totalbytes_17)
cell1.append(totalbytes_18)
cell1.append(totalbytes_19)
cell1.append(totalbytes_20)
cell1.append(totalbytes_21)
cell1.append(totalbytes_22)
cell1.append(totalbytes_23)
cell1.append(totalbytes_24)
cell1.append(totalbytes_25)
cell1.append(totalbytes_26)
cell1.append(totalbytes_27)
cell1.append(totalbytes_28)
cell1.append(totalbytes_29)
cell1.append(totalbytes_30)
cell1.append(totalbytes_31)
cell1.append(totalbytes_32)
cell1.append(totalbytes_33)
cell1.append(totalbytes_34)
cell1.append(totalbytes_35)
cell1.append(totalbytes_36)
cell1.append(totalbytes_37)
cell1.append(totalbytes_38)
cell1.append(totalbytes_39)
cell1.append(totalbytes_40)
cell1.append(totalbytes_41)
cell1.append(totalbytes_42)
cell1.append(totalbytes_43)
cell1.append(totalbytes_44)
cell1.append(totalbytes_45)
cell1.append(totalbytes_46)
cell1.append(totalbytes_47)
cell1.append(totalbytes_48)
cell1.append(totalbytes_49)
cell1.append(totalbytes_50)
cell1.append(totalbytes_51)
cell1.append(totalbytes_52)
cell1.append(totalbytes_53)
cell1.append(totalbytes_54)
cell1.append(totalbytes_55)
cell1.append(totalbytes_56)
cell1.append(totalbytes_57)
cell1.append(totalbytes_58)
cell1.append(totalbytes_59)
cell1.append(totalbytes_60)
cell1.append(totalbytes_61)
cell1.append(totalbytes_62)
cell1.append(totalbytes_63)
cell1.append(totalbytes_64)
cell1.append(totalbytes_65)

print(cell1)
