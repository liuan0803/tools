# -*- encoding: utf-8 -*-
'''
@File    :   mktxt_by_orgname.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/3/31 11:29
@Desciption  :   None
'''

import numpy as np
import os

file_path = r'D:\liuan58\ocrdata\test'
jpg_dir_list = os.listdir(file_path)

temp = []
for each_xml_dir in jpg_dir_list:
    a = each_xml_dir.split('.')[-3] + '.'+each_xml_dir.split('.')[-2]
    np.savetxt(r"D:/liuan58/ocrdata/txt/" + a + '.txt',np.array(temp))

print("successed!")