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
cell1 = []
cell2 = []
cell3 = []
cell4 = []
cell5 = []
cell6 = []
cell7 = []
cell8 = []
cell9 = []

for i in range(1, 1000):
    globals()['totalbytes_{}'.format(i)]=0
    
for i in strings:
    # print i.splitlines()
    line_list = i.splitlines()[0]
    new_data.append(line_list.split('\t'))
# print(new_data)
for i in range(len(new_data)):
    # print(new_data[i][2])
    # print(type(new_data[i][2]))
    if new_data[i][2]== str(1):
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
        if str(67) == new_data[i][1]:
            totalbytes_67 += int(new_data[i][7])
        if str(68) == new_data[i][1]:
            totalbytes_68 += int(new_data[i][7])
        if str(69) == new_data[i][1]:
            totalbytes_69 += int(new_data[i][7])
        if str(70) == new_data[i][1]:
            totalbytes_70 += int(new_data[i][7])
        if str(71) == new_data[i][1]:
            totalbytes_71 += int(new_data[i][7])
        if str(72) == new_data[i][1]:
            totalbytes_72 += int(new_data[i][7])
        if str(73) == new_data[i][1]:
            totalbytes_73 += int(new_data[i][7])
        if str(74) == new_data[i][1]:
            totalbytes_74 += int(new_data[i][7])
        if str(75) == new_data[i][1]:
            totalbytes_75 += int(new_data[i][7])
        if str(76) == new_data[i][1]:
            totalbytes_76 += int(new_data[i][7])
        if str(77) == new_data[i][1]:
            totalbytes_77 += int(new_data[i][7])
        if str(78) == new_data[i][1]:
            totalbytes_78 += int(new_data[i][7])
        if str(79) == new_data[i][1]:
            totalbytes_79 += int(new_data[i][7])
        if str(80) == new_data[i][1]:
            totalbytes_80 += int(new_data[i][7])
        if str(81) == new_data[i][1]:
            totalbytes_81 += int(new_data[i][7])
        if str(82) == new_data[i][1]:
            totalbytes_82 += int(new_data[i][7])
        if str(83) == new_data[i][1]:
            totalbytes_83 += int(new_data[i][7])
        if str(84) == new_data[i][1]:
            totalbytes_84 += int(new_data[i][7])
        if str(85) == new_data[i][1]:
            totalbytes_85 += int(new_data[i][7])
        if str(86) == new_data[i][1]:
            totalbytes_86 += int(new_data[i][7])
        if str(87) == new_data[i][1]:
            totalbytes_87 += int(new_data[i][7])
        if str(88) == new_data[i][1]:
            totalbytes_88 += int(new_data[i][7])
        if str(89) == new_data[i][1]:
            totalbytes_89 += int(new_data[i][7])
        if str(90) == new_data[i][1]:
            totalbytes_90 += int(new_data[i][7])
        if str(91) == new_data[i][1]:
            totalbytes_91 += int(new_data[i][7])
        if str(92) == new_data[i][1]:
            totalbytes_92 += int(new_data[i][7])
        if str(93) == new_data[i][1]:
            totalbytes_93 += int(new_data[i][7])
        if str(94) == new_data[i][1]:
            totalbytes_94 += int(new_data[i][7])
        if str(95) == new_data[i][1]:
            totalbytes_95 += int(new_data[i][7])
        if str(96) == new_data[i][1]:
            totalbytes_96 += int(new_data[i][7])
        if str(97) == new_data[i][1]:
            totalbytes_97 += int(new_data[i][7])
        if str(98) == new_data[i][1]:
            totalbytes_98 += int(new_data[i][7])
        if str(99) == new_data[i][1]:
            totalbytes_99 += int(new_data[i][7])
        if str(100) == new_data[i][1]:
            totalbytes_100 += int(new_data[i][7])
        if str(101) == new_data[i][1]:
            totalbytes_101 += int(new_data[i][7])
        if str(102) == new_data[i][1]:
            totalbytes_102 += int(new_data[i][7])
        if str(103) == new_data[i][1]:
            totalbytes_103 += int(new_data[i][7])
        if str(104) == new_data[i][1]:
            totalbytes_104 += int(new_data[i][7])
        if str(105) == new_data[i][1]:
            totalbytes_105 += int(new_data[i][7])
        if str(106) == new_data[i][1]:
            totalbytes_106 += int(new_data[i][7])
        if str(107) == new_data[i][1]:
            totalbytes_107 += int(new_data[i][7])
        if str(108) == new_data[i][1]:
            totalbytes_108 += int(new_data[i][7])
        if str(109) == new_data[i][1]:
            totalbytes_109 += int(new_data[i][7])
        if str(110) == new_data[i][1]:
            totalbytes_110 += int(new_data[i][7])
        if str(111) == new_data[i][1]:
            totalbytes_111 += int(new_data[i][7])
        if str(112) == new_data[i][1]:
            totalbytes_112 += int(new_data[i][7])
        if str(113) == new_data[i][1]:
            totalbytes_113 += int(new_data[i][7])
        if str(114) == new_data[i][1]:
            totalbytes_114 += int(new_data[i][7])
        if str(115) == new_data[i][1]:
            totalbytes_115 += int(new_data[i][7])
        if str(116) == new_data[i][1]:
            totalbytes_116 += int(new_data[i][7])
        if str(117) == new_data[i][1]:
            totalbytes_117 += int(new_data[i][7])
        if str(118) == new_data[i][1]:
            totalbytes_118 += int(new_data[i][7])
        if str(119) == new_data[i][1]:
            totalbytes_119 += int(new_data[i][7])
        if str(120) == new_data[i][1]:
            totalbytes_120 += int(new_data[i][7])
        if str(121) == new_data[i][1]:
            totalbytes_121 += int(new_data[i][7])
        if str(122) == new_data[i][1]:
            totalbytes_122 += int(new_data[i][7])
        if str(123) == new_data[i][1]:
            totalbytes_123 += int(new_data[i][7])
        if str(124) == new_data[i][1]:
            totalbytes_124 += int(new_data[i][7])
        if str(125) == new_data[i][1]:
            totalbytes_125 += int(new_data[i][7])
        if str(126) == new_data[i][1]:
            totalbytes_126 += int(new_data[i][7])
        if str(127) == new_data[i][1]:
            totalbytes_127 += int(new_data[i][7])
        if str(128) == new_data[i][1]:
            totalbytes_128 += int(new_data[i][7])
        if str(129) == new_data[i][1]:
            totalbytes_129 += int(new_data[i][7])
        if str(130) == new_data[i][1]:
            totalbytes_130 += int(new_data[i][7])
        if str(131) == new_data[i][1]:
            totalbytes_131 += int(new_data[i][7])
        if str(132) == new_data[i][1]:
            totalbytes_132 += int(new_data[i][7])
        if str(133) == new_data[i][1]:
            totalbytes_133 += int(new_data[i][7])
        if str(134) == new_data[i][1]:
            totalbytes_134 += int(new_data[i][7])
        if str(135) == new_data[i][1]:
            totalbytes_135 += int(new_data[i][7])
        if str(136) == new_data[i][1]:
            totalbytes_136 += int(new_data[i][7])
        if str(137) == new_data[i][1]:
            totalbytes_137 += int(new_data[i][7])
        if str(138) == new_data[i][1]:
            totalbytes_138 += int(new_data[i][7])
        if str(139) == new_data[i][1]:
            totalbytes_139 += int(new_data[i][7])
        if str(140) == new_data[i][1]:
            totalbytes_140 += int(new_data[i][7])
        if str(141) == new_data[i][1]:
            totalbytes_141 += int(new_data[i][7])
        if str(142) == new_data[i][1]:
            totalbytes_142 += int(new_data[i][7])
        if str(143) == new_data[i][1]:
            totalbytes_143 += int(new_data[i][7])
        if str(144) == new_data[i][1]:
            totalbytes_144 += int(new_data[i][7])
        if str(145) == new_data[i][1]:
            totalbytes_145 += int(new_data[i][7])
        if str(146) == new_data[i][1]:
            totalbytes_146 += int(new_data[i][7])
        if str(147) == new_data[i][1]:
            totalbytes_147 += int(new_data[i][7])
        if str(148) == new_data[i][1]:
            totalbytes_148 += int(new_data[i][7])
        if str(149) == new_data[i][1]:
            totalbytes_149 += int(new_data[i][7])
        if str(150) == new_data[i][1]:
            totalbytes_150 += int(new_data[i][7])
        if str(151) == new_data[i][1]:
            totalbytes_151 += int(new_data[i][7])
        if str(152) == new_data[i][1]:
            totalbytes_152 += int(new_data[i][7])
        if str(153) == new_data[i][1]:
            totalbytes_153 += int(new_data[i][7])
        if str(154) == new_data[i][1]:
            totalbytes_154 += int(new_data[i][7])
        if str(155) == new_data[i][1]:
            totalbytes_155 += int(new_data[i][7])
        if str(156) == new_data[i][1]:
            totalbytes_156 += int(new_data[i][7])
        if str(157) == new_data[i][1]:
            totalbytes_157 += int(new_data[i][7])
        if str(158) == new_data[i][1]:
            totalbytes_158 += int(new_data[i][7])
        if str(159) == new_data[i][1]:
            totalbytes_159 += int(new_data[i][7])
        if str(160) == new_data[i][1]:
            totalbytes_160 += int(new_data[i][7])
        if str(161) == new_data[i][1]:
            totalbytes_161 += int(new_data[i][7])
        if str(162) == new_data[i][1]:
            totalbytes_162 += int(new_data[i][7])
        if str(163) == new_data[i][1]:
            totalbytes_163 += int(new_data[i][7])
        if str(164) == new_data[i][1]:
            totalbytes_164 += int(new_data[i][7])
        if str(165) == new_data[i][1]:
            totalbytes_165 += int(new_data[i][7])
        if str(166) == new_data[i][1]:
            totalbytes_166 += int(new_data[i][7])
        if str(167) == new_data[i][1]:
            totalbytes_167 += int(new_data[i][7])
        if str(168) == new_data[i][1]:
            totalbytes_168 += int(new_data[i][7])
        if str(169) == new_data[i][1]:
            totalbytes_169 += int(new_data[i][7])
        if str(170) == new_data[i][1]:
            totalbytes_170 += int(new_data[i][7])
        if str(171) == new_data[i][1]:
            totalbytes_171 += int(new_data[i][7])
        if str(172) == new_data[i][1]:
            totalbytes_172 += int(new_data[i][7])
        if str(173) == new_data[i][1]:
            totalbytes_173 += int(new_data[i][7])
        if str(174) == new_data[i][1]:
            totalbytes_174 += int(new_data[i][7])
        if str(175) == new_data[i][1]:
            totalbytes_175 += int(new_data[i][7])
        if str(176) == new_data[i][1]:
            totalbytes_176 += int(new_data[i][7])
        if str(177) == new_data[i][1]:
            totalbytes_177 += int(new_data[i][7])
        if str(178) == new_data[i][1]:
            totalbytes_178 += int(new_data[i][7])
        if str(179) == new_data[i][1]:
            totalbytes_179 += int(new_data[i][7])
        if str(180) == new_data[i][1]:
            totalbytes_180 += int(new_data[i][7])
        if str(181) == new_data[i][1]:
            totalbytes_181 += int(new_data[i][7])
        if str(182) == new_data[i][1]:
            totalbytes_182 += int(new_data[i][7])
        if str(183) == new_data[i][1]:
            totalbytes_183 += int(new_data[i][7])
        if str(184) == new_data[i][1]:
            totalbytes_184 += int(new_data[i][7])
        if str(185) == new_data[i][1]:
            totalbytes_185 += int(new_data[i][7])
        if str(186) == new_data[i][1]:
            totalbytes_186 += int(new_data[i][7])
        if str(187) == new_data[i][1]:
            totalbytes_187 += int(new_data[i][7])
        if str(188) == new_data[i][1]:
            totalbytes_188 += int(new_data[i][7])
        if str(189) == new_data[i][1]:
            totalbytes_189 += int(new_data[i][7])
        if str(190) == new_data[i][1]:
            totalbytes_190 += int(new_data[i][7])
        if str(191) == new_data[i][1]:
            totalbytes_191 += int(new_data[i][7])
        if str(192) == new_data[i][1]:
            totalbytes_192 += int(new_data[i][7])
        if str(193) == new_data[i][1]:
            totalbytes_193 += int(new_data[i][7])
        if str(194) == new_data[i][1]:
            totalbytes_194 += int(new_data[i][7])
        if str(195) == new_data[i][1]:
            totalbytes_195 += int(new_data[i][7])
        if str(196) == new_data[i][1]:
            totalbytes_196 += int(new_data[i][7])
        if str(197) == new_data[i][1]:
            totalbytes_197 += int(new_data[i][7])
        if str(198) == new_data[i][1]:
            totalbytes_198 += int(new_data[i][7])
        if str(199) == new_data[i][1]:
            totalbytes_199 += int(new_data[i][7])
        if str(200) == new_data[i][1]:
            totalbytes_200 += int(new_data[i][7])
        if str(201) == new_data[i][1]:
            totalbytes_201 += int(new_data[i][7])
        if str(202) == new_data[i][1]:
            totalbytes_202 += int(new_data[i][7])
        if str(203) == new_data[i][1]:
            totalbytes_203 += int(new_data[i][7])
        if str(204) == new_data[i][1]:
            totalbytes_204 += int(new_data[i][7])
        if str(205) == new_data[i][1]:
            totalbytes_205 += int(new_data[i][7])
        if str(206) == new_data[i][1]:
            totalbytes_206 += int(new_data[i][7])
        if str(207) == new_data[i][1]:
            totalbytes_207 += int(new_data[i][7])
        if str(208) == new_data[i][1]:
            totalbytes_208 += int(new_data[i][7])
        if str(209) == new_data[i][1]:
            totalbytes_209 += int(new_data[i][7])
        if str(210) == new_data[i][1]:
            totalbytes_210 += int(new_data[i][7])
        if str(211) == new_data[i][1]:
            totalbytes_211 += int(new_data[i][7])
        if str(212) == new_data[i][1]:
            totalbytes_212 += int(new_data[i][7])
        if str(213) == new_data[i][1]:
            totalbytes_213 += int(new_data[i][7])
        if str(214) == new_data[i][1]:
            totalbytes_214 += int(new_data[i][7])
        if str(215) == new_data[i][1]:
            totalbytes_215 += int(new_data[i][7])
        if str(216) == new_data[i][1]:
            totalbytes_216 += int(new_data[i][7])
        if str(217) == new_data[i][1]:
            totalbytes_217 += int(new_data[i][7])
        if str(218) == new_data[i][1]:
            totalbytes_218 += int(new_data[i][7])
        if str(219) == new_data[i][1]:
            totalbytes_219 += int(new_data[i][7])
        if str(220) == new_data[i][1]:
            totalbytes_220 += int(new_data[i][7])
        if str(221) == new_data[i][1]:
            totalbytes_221 += int(new_data[i][7])
        if str(222) == new_data[i][1]:
            totalbytes_222 += int(new_data[i][7])
        if str(223) == new_data[i][1]:
            totalbytes_223 += int(new_data[i][7])
        if str(224) == new_data[i][1]:
            totalbytes_224 += int(new_data[i][7])
        if str(225) == new_data[i][1]:
            totalbytes_225 += int(new_data[i][7])
        if str(226) == new_data[i][1]:
            totalbytes_226 += int(new_data[i][7])
        if str(227) == new_data[i][1]:
            totalbytes_227 += int(new_data[i][7])
        if str(228) == new_data[i][1]:
            totalbytes_228 += int(new_data[i][7])
        if str(229) == new_data[i][1]:
            totalbytes_229 += int(new_data[i][7])
        if str(230) == new_data[i][1]:
            totalbytes_230 += int(new_data[i][7])
        if str(231) == new_data[i][1]:
            totalbytes_231 += int(new_data[i][7])
        if str(232) == new_data[i][1]:
            totalbytes_232 += int(new_data[i][7])
        if str(233) == new_data[i][1]:
            totalbytes_233 += int(new_data[i][7])
        if str(234) == new_data[i][1]:
            totalbytes_234 += int(new_data[i][7])
        if str(235) == new_data[i][1]:
            totalbytes_235 += int(new_data[i][7])
        if str(236) == new_data[i][1]:
            totalbytes_236 += int(new_data[i][7])
        if str(237) == new_data[i][1]:
            totalbytes_237 += int(new_data[i][7])
        if str(238) == new_data[i][1]:
            totalbytes_238 += int(new_data[i][7])
        if str(239) == new_data[i][1]:
            totalbytes_239 += int(new_data[i][7])
        if str(240) == new_data[i][1]:
            totalbytes_240 += int(new_data[i][7])
        if str(241) == new_data[i][1]:
            totalbytes_241 += int(new_data[i][7])
        if str(242) == new_data[i][1]:
            totalbytes_242 += int(new_data[i][7])
        if str(243) == new_data[i][1]:
            totalbytes_243 += int(new_data[i][7])
        if str(244) == new_data[i][1]:
            totalbytes_244 += int(new_data[i][7])
        if str(245) == new_data[i][1]:
            totalbytes_245 += int(new_data[i][7])
        if str(246) == new_data[i][1]:
            totalbytes_246 += int(new_data[i][7])
        if str(247) == new_data[i][1]:
            totalbytes_247 += int(new_data[i][7])
        if str(248) == new_data[i][1]:
            totalbytes_248 += int(new_data[i][7])
        if str(249) == new_data[i][1]:
            totalbytes_249 += int(new_data[i][7])
        if str(250) == new_data[i][1]:
            totalbytes_250 += int(new_data[i][7])
        if str(251) == new_data[i][1]:
            totalbytes_251 += int(new_data[i][7])
        if str(252) == new_data[i][1]:
            totalbytes_252 += int(new_data[i][7])
        if str(253) == new_data[i][1]:
            totalbytes_253 += int(new_data[i][7])
        if str(254) == new_data[i][1]:
            totalbytes_254 += int(new_data[i][7])
        if str(255) == new_data[i][1]:
            totalbytes_255 += int(new_data[i][7])
        if str(256) == new_data[i][1]:
            totalbytes_256 += int(new_data[i][7])
        if str(257) == new_data[i][1]:
            totalbytes_257 += int(new_data[i][7])
        if str(258) == new_data[i][1]:
            totalbytes_258 += int(new_data[i][7])
        if str(259) == new_data[i][1]:
            totalbytes_259 += int(new_data[i][7])
        if str(260) == new_data[i][1]:
            totalbytes_260 += int(new_data[i][7])
        if str(261) == new_data[i][1]:
            totalbytes_261 += int(new_data[i][7])
        if str(262) == new_data[i][1]:
            totalbytes_262 += int(new_data[i][7])
        if str(263) == new_data[i][1]:
            totalbytes_263 += int(new_data[i][7])
        if str(264) == new_data[i][1]:
            totalbytes_264 += int(new_data[i][7])
        if str(265) == new_data[i][1]:
            totalbytes_265 += int(new_data[i][7])
        if str(266) == new_data[i][1]:
            totalbytes_266 += int(new_data[i][7])
        if str(267) == new_data[i][1]:
            totalbytes_267 += int(new_data[i][7])
        if str(268) == new_data[i][1]:
            totalbytes_268 += int(new_data[i][7])
        if str(269) == new_data[i][1]:
            totalbytes_269 += int(new_data[i][7])
        if str(270) == new_data[i][1]:
            totalbytes_270 += int(new_data[i][7])
        if str(271) == new_data[i][1]:
            totalbytes_271 += int(new_data[i][7])
        if str(272) == new_data[i][1]:
            totalbytes_272 += int(new_data[i][7])
        if str(273) == new_data[i][1]:
            totalbytes_273 += int(new_data[i][7])
        if str(274) == new_data[i][1]:
            totalbytes_274 += int(new_data[i][7])
        if str(275) == new_data[i][1]:
            totalbytes_275 += int(new_data[i][7])
        if str(276) == new_data[i][1]:
            totalbytes_276 += int(new_data[i][7])
        if str(277) == new_data[i][1]:
            totalbytes_277 += int(new_data[i][7])
        if str(278) == new_data[i][1]:
            totalbytes_278 += int(new_data[i][7])
        if str(279) == new_data[i][1]:
            totalbytes_279 += int(new_data[i][7])
        if str(280) == new_data[i][1]:
            totalbytes_280 += int(new_data[i][7])
        if str(281) == new_data[i][1]:
            totalbytes_281 += int(new_data[i][7])
        if str(282) == new_data[i][1]:
            totalbytes_282 += int(new_data[i][7])
        if str(283) == new_data[i][1]:
            totalbytes_283 += int(new_data[i][7])
        if str(284) == new_data[i][1]:
            totalbytes_284 += int(new_data[i][7])
        if str(285) == new_data[i][1]:
            totalbytes_285 += int(new_data[i][7])
        if str(286) == new_data[i][1]:
            totalbytes_286 += int(new_data[i][7])
        if str(287) == new_data[i][1]:
            totalbytes_287 += int(new_data[i][7])
        if str(288) == new_data[i][1]:
            totalbytes_288 += int(new_data[i][7])
        if str(289) == new_data[i][1]:
            totalbytes_289 += int(new_data[i][7])
        if str(290) == new_data[i][1]:
            totalbytes_290 += int(new_data[i][7])
        if str(291) == new_data[i][1]:
            totalbytes_291 += int(new_data[i][7])
        if str(292) == new_data[i][1]:
            totalbytes_292 += int(new_data[i][7])
        if str(293) == new_data[i][1]:
            totalbytes_293 += int(new_data[i][7])
        if str(294) == new_data[i][1]:
            totalbytes_294 += int(new_data[i][7])
        if str(295) == new_data[i][1]:
            totalbytes_295 += int(new_data[i][7])
        if str(296) == new_data[i][1]:
            totalbytes_296 += int(new_data[i][7])
        if str(297) == new_data[i][1]:
            totalbytes_297 += int(new_data[i][7])
        if str(298) == new_data[i][1]:
            totalbytes_298 += int(new_data[i][7])
        if str(299) == new_data[i][1]:
            totalbytes_299 += int(new_data[i][7])
        if str(300) == new_data[i][1]:
            totalbytes_300 += int(new_data[i][7])
        if str(301) == new_data[i][1]:
            totalbytes_301 += int(new_data[i][7])
        if str(302) == new_data[i][1]:
            totalbytes_302 += int(new_data[i][7])
        if str(303) == new_data[i][1]:
            totalbytes_303 += int(new_data[i][7])
        if str(304) == new_data[i][1]:
            totalbytes_304 += int(new_data[i][7])
        if str(305) == new_data[i][1]:
            totalbytes_305 += int(new_data[i][7])
        if str(306) == new_data[i][1]:
            totalbytes_306 += int(new_data[i][7])
        if str(307) == new_data[i][1]:
            totalbytes_307 += int(new_data[i][7])
        if str(308) == new_data[i][1]:
            totalbytes_308 += int(new_data[i][7])
        if str(309) == new_data[i][1]:
            totalbytes_309 += int(new_data[i][7])
        if str(310) == new_data[i][1]:
            totalbytes_310 += int(new_data[i][7])
        if str(311) == new_data[i][1]:
            totalbytes_311 += int(new_data[i][7])
        if str(312) == new_data[i][1]:
            totalbytes_312 += int(new_data[i][7])
        if str(313) == new_data[i][1]:
            totalbytes_313 += int(new_data[i][7])
        if str(314) == new_data[i][1]:
            totalbytes_314 += int(new_data[i][7])
        if str(315) == new_data[i][1]:
            totalbytes_315 += int(new_data[i][7])
        if str(316) == new_data[i][1]:
            totalbytes_316 += int(new_data[i][7])
        if str(317) == new_data[i][1]:
            totalbytes_317 += int(new_data[i][7])
        if str(318) == new_data[i][1]:
            totalbytes_318 += int(new_data[i][7])
        if str(319) == new_data[i][1]:
            totalbytes_319 += int(new_data[i][7])
        if str(320) == new_data[i][1]:
            totalbytes_320 += int(new_data[i][7])
        if str(321) == new_data[i][1]:
            totalbytes_321 += int(new_data[i][7])
        if str(322) == new_data[i][1]:
            totalbytes_322 += int(new_data[i][7])
        if str(323) == new_data[i][1]:
            totalbytes_323 += int(new_data[i][7])
        if str(324) == new_data[i][1]:
            totalbytes_324 += int(new_data[i][7])
        if str(325) == new_data[i][1]:
            totalbytes_325 += int(new_data[i][7])
        if str(326) == new_data[i][1]:
            totalbytes_326 += int(new_data[i][7])
        if str(327) == new_data[i][1]:
            totalbytes_327 += int(new_data[i][7])
        if str(328) == new_data[i][1]:
            totalbytes_328 += int(new_data[i][7])
        if str(329) == new_data[i][1]:
            totalbytes_329 += int(new_data[i][7])
        if str(330) == new_data[i][1]:
            totalbytes_330 += int(new_data[i][7])
        if str(331) == new_data[i][1]:
            totalbytes_331 += int(new_data[i][7])
        if str(332) == new_data[i][1]:
            totalbytes_332 += int(new_data[i][7])
        if str(333) == new_data[i][1]:
            totalbytes_333 += int(new_data[i][7])
        if str(334) == new_data[i][1]:
            totalbytes_334 += int(new_data[i][7])
        if str(335) == new_data[i][1]:
            totalbytes_335 += int(new_data[i][7])
        if str(336) == new_data[i][1]:
            totalbytes_336 += int(new_data[i][7])
        if str(337) == new_data[i][1]:
            totalbytes_337 += int(new_data[i][7])
        if str(338) == new_data[i][1]:
            totalbytes_338 += int(new_data[i][7])
        if str(339) == new_data[i][1]:
            totalbytes_339 += int(new_data[i][7])
        if str(340) == new_data[i][1]:
            totalbytes_340 += int(new_data[i][7])
        if str(341) == new_data[i][1]:
            totalbytes_341 += int(new_data[i][7])
        if str(342) == new_data[i][1]:
            totalbytes_342 += int(new_data[i][7])
        if str(343) == new_data[i][1]:
            totalbytes_343 += int(new_data[i][7])
        if str(344) == new_data[i][1]:
            totalbytes_344 += int(new_data[i][7])
        if str(345) == new_data[i][1]:
            totalbytes_345 += int(new_data[i][7])
        if str(346) == new_data[i][1]:
            totalbytes_346 += int(new_data[i][7])
        if str(347) == new_data[i][1]:
            totalbytes_347 += int(new_data[i][7])
        if str(348) == new_data[i][1]:
            totalbytes_348 += int(new_data[i][7])
        if str(349) == new_data[i][1]:
            totalbytes_349 += int(new_data[i][7])
        if str(350) == new_data[i][1]:
            totalbytes_350 += int(new_data[i][7])
        if str(351) == new_data[i][1]:
            totalbytes_351 += int(new_data[i][7])
        if str(352) == new_data[i][1]:
            totalbytes_352 += int(new_data[i][7])
        if str(353) == new_data[i][1]:
            totalbytes_353 += int(new_data[i][7])
        if str(354) == new_data[i][1]:
            totalbytes_354 += int(new_data[i][7])
        if str(355) == new_data[i][1]:
            totalbytes_355 += int(new_data[i][7])
        if str(356) == new_data[i][1]:
            totalbytes_356 += int(new_data[i][7])
        if str(357) == new_data[i][1]:
            totalbytes_357 += int(new_data[i][7])
        if str(358) == new_data[i][1]:
            totalbytes_358 += int(new_data[i][7])
        if str(359) == new_data[i][1]:
            totalbytes_359 += int(new_data[i][7])
        if str(360) == new_data[i][1]:
            totalbytes_360 += int(new_data[i][7])
        if str(361) == new_data[i][1]:
            totalbytes_361 += int(new_data[i][7])
        if str(362) == new_data[i][1]:
            totalbytes_362 += int(new_data[i][7])
        if str(363) == new_data[i][1]:
            totalbytes_363 += int(new_data[i][7])
        if str(364) == new_data[i][1]:
            totalbytes_364 += int(new_data[i][7])
        if str(365) == new_data[i][1]:
            totalbytes_365 += int(new_data[i][7])
        if str(366) == new_data[i][1]:
            totalbytes_366 += int(new_data[i][7])
        if str(367) == new_data[i][1]:
            totalbytes_367 += int(new_data[i][7])
        if str(368) == new_data[i][1]:
            totalbytes_368 += int(new_data[i][7])
        if str(369) == new_data[i][1]:
            totalbytes_369 += int(new_data[i][7])
        if str(370) == new_data[i][1]:
            totalbytes_370 += int(new_data[i][7])
        if str(371) == new_data[i][1]:
            totalbytes_371 += int(new_data[i][7])
        if str(372) == new_data[i][1]:
            totalbytes_372 += int(new_data[i][7])
        if str(373) == new_data[i][1]:
            totalbytes_373 += int(new_data[i][7])
        if str(374) == new_data[i][1]:
            totalbytes_374 += int(new_data[i][7])
        if str(375) == new_data[i][1]:
            totalbytes_375 += int(new_data[i][7])
        if str(376) == new_data[i][1]:
            totalbytes_376 += int(new_data[i][7])
        if str(377) == new_data[i][1]:
            totalbytes_377 += int(new_data[i][7])
        if str(378) == new_data[i][1]:
            totalbytes_378 += int(new_data[i][7])
        if str(379) == new_data[i][1]:
            totalbytes_379 += int(new_data[i][7])
        if str(380) == new_data[i][1]:
            totalbytes_380 += int(new_data[i][7])
        if str(381) == new_data[i][1]:
            totalbytes_381 += int(new_data[i][7])
        if str(382) == new_data[i][1]:
            totalbytes_382 += int(new_data[i][7])
        if str(383) == new_data[i][1]:
            totalbytes_383 += int(new_data[i][7])
        if str(384) == new_data[i][1]:
            totalbytes_384 += int(new_data[i][7])
        if str(385) == new_data[i][1]:
            totalbytes_385 += int(new_data[i][7])
        if str(386) == new_data[i][1]:
            totalbytes_386 += int(new_data[i][7])
        if str(387) == new_data[i][1]:
            totalbytes_387 += int(new_data[i][7])
        if str(388) == new_data[i][1]:
            totalbytes_388 += int(new_data[i][7])
        if str(389) == new_data[i][1]:
            totalbytes_389 += int(new_data[i][7])
        if str(390) == new_data[i][1]:
            totalbytes_390 += int(new_data[i][7])
        if str(391) == new_data[i][1]:
            totalbytes_391 += int(new_data[i][7])
        if str(392) == new_data[i][1]:
            totalbytes_392 += int(new_data[i][7])
        if str(393) == new_data[i][1]:
            totalbytes_393 += int(new_data[i][7])
        if str(394) == new_data[i][1]:
            totalbytes_394 += int(new_data[i][7])
        if str(395) == new_data[i][1]:
            totalbytes_395 += int(new_data[i][7])
        if str(396) == new_data[i][1]:
            totalbytes_396 += int(new_data[i][7])
        if str(397) == new_data[i][1]:
            totalbytes_397 += int(new_data[i][7])
        if str(398) == new_data[i][1]:
            totalbytes_398 += int(new_data[i][7])
        if str(399) == new_data[i][1]:
            totalbytes_399 += int(new_data[i][7])


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
# cell1.append(totalbytes_61)
# cell1.append(totalbytes_62)
# cell1.append(totalbytes_63)
# cell1.append(totalbytes_64)
# cell1.append(totalbytes_65)
# cell1.append(totalbytes_66)
# cell1.append(totalbytes_67)
# cell1.append(totalbytes_68)
# cell1.append(totalbytes_69)
# cell1.append(totalbytes_70)
# cell1.append(totalbytes_71)
# cell1.append(totalbytes_72)
# cell1.append(totalbytes_73)
# cell1.append(totalbytes_74)
# cell1.append(totalbytes_75)
# cell1.append(totalbytes_76)
# cell1.append(totalbytes_77)
# cell1.append(totalbytes_78)
# cell1.append(totalbytes_79)
# cell1.append(totalbytes_80)
# cell1.append(totalbytes_81)
# cell1.append(totalbytes_82)
# cell1.append(totalbytes_83)
# cell1.append(totalbytes_84)
# cell1.append(totalbytes_85)
# cell1.append(totalbytes_86)
# cell1.append(totalbytes_87)
# cell1.append(totalbytes_88)
# cell1.append(totalbytes_89)
# cell1.append(totalbytes_90)
# cell1.append(totalbytes_91)
# cell1.append(totalbytes_92)
# cell1.append(totalbytes_93)
# cell1.append(totalbytes_94)
# cell1.append(totalbytes_95)
# cell1.append(totalbytes_96)
# cell1.append(totalbytes_97)
# cell1.append(totalbytes_98)
# cell1.append(totalbytes_99)
# cell1.append(totalbytes_100)
# cell1.append(totalbytes_101)
# cell1.append(totalbytes_102)
# cell1.append(totalbytes_103)
# cell1.append(totalbytes_104)
# cell1.append(totalbytes_105)
# cell1.append(totalbytes_106)
# cell1.append(totalbytes_107)
# cell1.append(totalbytes_108)
# cell1.append(totalbytes_109)
# cell1.append(totalbytes_110)
# cell1.append(totalbytes_111)
# cell1.append(totalbytes_112)
# cell1.append(totalbytes_113)
# cell1.append(totalbytes_114)
# cell1.append(totalbytes_115)
# cell1.append(totalbytes_116)
# cell1.append(totalbytes_117)
# cell1.append(totalbytes_118)
# cell1.append(totalbytes_119)
# cell1.append(totalbytes_120)
# cell1.append(totalbytes_121)
# cell1.append(totalbytes_122)
# cell1.append(totalbytes_123)
# cell1.append(totalbytes_124)
# cell1.append(totalbytes_125)
# cell1.append(totalbytes_126)
# cell1.append(totalbytes_127)
# cell1.append(totalbytes_128)
# cell1.append(totalbytes_129)
# cell1.append(totalbytes_130)
# cell1.append(totalbytes_131)
# cell1.append(totalbytes_132)
# cell1.append(totalbytes_133)
# cell1.append(totalbytes_134)
# cell1.append(totalbytes_135)
# cell1.append(totalbytes_136)
# cell1.append(totalbytes_137)
# cell1.append(totalbytes_138)
# cell1.append(totalbytes_139)
# cell1.append(totalbytes_140)
# cell1.append(totalbytes_141)
# cell1.append(totalbytes_142)
# cell1.append(totalbytes_143)
# cell1.append(totalbytes_144)
# cell1.append(totalbytes_145)
# cell1.append(totalbytes_146)
# cell1.append(totalbytes_147)
# cell1.append(totalbytes_148)
# cell1.append(totalbytes_149)
# cell1.append(totalbytes_150)
# cell1.append(totalbytes_151)
# cell1.append(totalbytes_152)
# cell1.append(totalbytes_153)
# cell1.append(totalbytes_154)
# cell1.append(totalbytes_155)
# cell1.append(totalbytes_156)
# cell1.append(totalbytes_157)
# cell1.append(totalbytes_158)
# cell1.append(totalbytes_159)
# cell1.append(totalbytes_160)
# cell1.append(totalbytes_161)
# cell1.append(totalbytes_162)
# cell1.append(totalbytes_163)
# cell1.append(totalbytes_164)
# cell1.append(totalbytes_165)
# cell1.append(totalbytes_166)
# cell1.append(totalbytes_167)
# cell1.append(totalbytes_168)
# cell1.append(totalbytes_169)
# cell1.append(totalbytes_170)
# cell1.append(totalbytes_171)
# cell1.append(totalbytes_172)
# cell1.append(totalbytes_173)
# cell1.append(totalbytes_174)
# cell1.append(totalbytes_175)
# cell1.append(totalbytes_176)
# cell1.append(totalbytes_177)
# cell1.append(totalbytes_178)
# cell1.append(totalbytes_179)
# cell1.append(totalbytes_180)
# cell1.append(totalbytes_181)
# cell1.append(totalbytes_182)
# cell1.append(totalbytes_183)
# cell1.append(totalbytes_184)
# cell1.append(totalbytes_185)
# cell1.append(totalbytes_186)
# cell1.append(totalbytes_187)
# cell1.append(totalbytes_188)
# cell1.append(totalbytes_189)
# cell1.append(totalbytes_190)
# cell1.append(totalbytes_191)
# cell1.append(totalbytes_192)
# cell1.append(totalbytes_193)
# cell1.append(totalbytes_194)
# cell1.append(totalbytes_195)
# cell1.append(totalbytes_196)
# cell1.append(totalbytes_197)
# cell1.append(totalbytes_198)
# cell1.append(totalbytes_199)
# cell1.append(totalbytes_200)
# cell1.append(totalbytes_201)
# cell1.append(totalbytes_202)
# cell1.append(totalbytes_203)
# cell1.append(totalbytes_204)
# cell1.append(totalbytes_205)
# cell1.append(totalbytes_206)
# cell1.append(totalbytes_207)
# cell1.append(totalbytes_208)
# cell1.append(totalbytes_209)
# cell1.append(totalbytes_210)
# cell1.append(totalbytes_211)
# cell1.append(totalbytes_212)
# cell1.append(totalbytes_213)
# cell1.append(totalbytes_214)
# cell1.append(totalbytes_215)
# cell1.append(totalbytes_216)
# cell1.append(totalbytes_217)
# cell1.append(totalbytes_218)
# cell1.append(totalbytes_219)
# cell1.append(totalbytes_220)
# cell1.append(totalbytes_221)
# cell1.append(totalbytes_222)
# cell1.append(totalbytes_223)
# cell1.append(totalbytes_224)
# cell1.append(totalbytes_225)
# cell1.append(totalbytes_226)
# cell1.append(totalbytes_227)
# cell1.append(totalbytes_228)
# cell1.append(totalbytes_229)
# cell1.append(totalbytes_230)
# cell1.append(totalbytes_231)
# cell1.append(totalbytes_232)
# cell1.append(totalbytes_233)
# cell1.append(totalbytes_234)
# cell1.append(totalbytes_235)
# cell1.append(totalbytes_236)
# cell1.append(totalbytes_237)
# cell1.append(totalbytes_238)
# cell1.append(totalbytes_239)
# cell1.append(totalbytes_240)
# cell1.append(totalbytes_241)
# cell1.append(totalbytes_242)
# cell1.append(totalbytes_243)
# cell1.append(totalbytes_244)
# cell1.append(totalbytes_245)
# cell1.append(totalbytes_246)
# cell1.append(totalbytes_247)
# cell1.append(totalbytes_248)
# cell1.append(totalbytes_249)
# cell1.append(totalbytes_250)
# cell1.append(totalbytes_251)
# cell1.append(totalbytes_252)
# cell1.append(totalbytes_253)
# cell1.append(totalbytes_254)
# cell1.append(totalbytes_255)
# cell1.append(totalbytes_256)
# cell1.append(totalbytes_257)
# cell1.append(totalbytes_258)
# cell1.append(totalbytes_259)
# cell1.append(totalbytes_260)
# cell1.append(totalbytes_261)
# cell1.append(totalbytes_262)
# cell1.append(totalbytes_263)
# cell1.append(totalbytes_264)
# cell1.append(totalbytes_265)
# cell1.append(totalbytes_266)
# cell1.append(totalbytes_267)
# cell1.append(totalbytes_268)
# cell1.append(totalbytes_269)
# cell1.append(totalbytes_270)
# cell1.append(totalbytes_271)
# cell1.append(totalbytes_272)
# cell1.append(totalbytes_273)
# cell1.append(totalbytes_274)
# cell1.append(totalbytes_275)
# cell1.append(totalbytes_276)
# cell1.append(totalbytes_277)
# cell1.append(totalbytes_278)
# cell1.append(totalbytes_279)
# cell1.append(totalbytes_280)
# cell1.append(totalbytes_281)
# cell1.append(totalbytes_282)
# cell1.append(totalbytes_283)
# cell1.append(totalbytes_284)
# cell1.append(totalbytes_285)
# cell1.append(totalbytes_286)
# cell1.append(totalbytes_287)
# cell1.append(totalbytes_288)
# cell1.append(totalbytes_289)
# cell1.append(totalbytes_290)
# cell1.append(totalbytes_291)
# cell1.append(totalbytes_292)
# cell1.append(totalbytes_293)
# cell1.append(totalbytes_294)
# cell1.append(totalbytes_295)
# cell1.append(totalbytes_296)
# cell1.append(totalbytes_297)
# cell1.append(totalbytes_298)
# cell1.append(totalbytes_299)
# cell1.append(totalbytes_300)
# cell1.append(totalbytes_301)
# cell1.append(totalbytes_302)
# cell1.append(totalbytes_303)
# cell1.append(totalbytes_304)
# cell1.append(totalbytes_305)
# cell1.append(totalbytes_306)
# cell1.append(totalbytes_307)
# cell1.append(totalbytes_308)
# cell1.append(totalbytes_309)
# cell1.append(totalbytes_310)
# cell1.append(totalbytes_311)
# cell1.append(totalbytes_312)
# cell1.append(totalbytes_313)
# cell1.append(totalbytes_314)
# cell1.append(totalbytes_315)
# cell1.append(totalbytes_316)
# cell1.append(totalbytes_317)
# cell1.append(totalbytes_318)
# cell1.append(totalbytes_319)
# cell1.append(totalbytes_320)
# cell1.append(totalbytes_321)
# cell1.append(totalbytes_322)
# cell1.append(totalbytes_323)
# cell1.append(totalbytes_324)
# cell1.append(totalbytes_325)
# cell1.append(totalbytes_326)
# cell1.append(totalbytes_327)
# cell1.append(totalbytes_328)
# cell1.append(totalbytes_329)
# cell1.append(totalbytes_330)
# cell1.append(totalbytes_331)
# cell1.append(totalbytes_332)
# cell1.append(totalbytes_333)
# cell1.append(totalbytes_334)
# cell1.append(totalbytes_335)
# cell1.append(totalbytes_336)
# cell1.append(totalbytes_337)
# cell1.append(totalbytes_338)
# cell1.append(totalbytes_339)
# cell1.append(totalbytes_340)
# cell1.append(totalbytes_341)
# cell1.append(totalbytes_342)
# cell1.append(totalbytes_343)
# cell1.append(totalbytes_344)
# cell1.append(totalbytes_345)
# cell1.append(totalbytes_346)
# cell1.append(totalbytes_347)
# cell1.append(totalbytes_348)
# cell1.append(totalbytes_349)
# cell1.append(totalbytes_350)
# cell1.append(totalbytes_351)
# cell1.append(totalbytes_352)
# cell1.append(totalbytes_353)
# cell1.append(totalbytes_354)
# cell1.append(totalbytes_355)
# cell1.append(totalbytes_356)
# cell1.append(totalbytes_357)
# cell1.append(totalbytes_358)
# cell1.append(totalbytes_359)
# cell1.append(totalbytes_360)
# cell1.append(totalbytes_361)
# cell1.append(totalbytes_362)
# cell1.append(totalbytes_363)
# cell1.append(totalbytes_364)
# cell1.append(totalbytes_365)
# cell1.append(totalbytes_366)
# cell1.append(totalbytes_367)
# cell1.append(totalbytes_368)
# cell1.append(totalbytes_369)
# cell1.append(totalbytes_370)
# cell1.append(totalbytes_371)
# cell1.append(totalbytes_372)
# cell1.append(totalbytes_373)
# cell1.append(totalbytes_374)
# cell1.append(totalbytes_375)
# cell1.append(totalbytes_376)
# cell1.append(totalbytes_377)
# cell1.append(totalbytes_378)
# cell1.append(totalbytes_379)
# cell1.append(totalbytes_380)
# cell1.append(totalbytes_381)
# cell1.append(totalbytes_382)
# cell1.append(totalbytes_383)
# cell1.append(totalbytes_384)
# cell1.append(totalbytes_385)
# cell1.append(totalbytes_386)
# cell1.append(totalbytes_387)
# cell1.append(totalbytes_388)
# cell1.append(totalbytes_389)
# cell1.append(totalbytes_390)
# cell1.append(totalbytes_391)
# cell1.append(totalbytes_392)
# cell1.append(totalbytes_393)
# cell1.append(totalbytes_394)
# cell1.append(totalbytes_395)
# cell1.append(totalbytes_396)
# cell1.append(totalbytes_397)
# cell1.append(totalbytes_398)
# cell1.append(totalbytes_399)

print(cell1)
