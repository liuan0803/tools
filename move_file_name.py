# -*- encoding: utf-8 -*-
'''
@File    :   move_file_name.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/3/4 16:20
@Desciption  :   None
'''

import numpy as np
import shutil
import os

file_path = r'D:\liuan58\ocrdata\xingming-opt\xm_jpg_xml_add_208_short_bad_cases\xm_jpg_add_208_short_bad_cases'
jpg_dir_list = os.listdir(file_path)
need_file_path = r'D:\liuan58\ocrdata\xingming-opt\presign_10000_short_xm_opt\xm_from_10000_short_badcase'
need_jpg = os.listdir(need_file_path)

print("need_jpg:", need_jpg)

for each_xml_dir in jpg_dir_list:
    a = each_xml_dir.split('.')[-2] + '.jpg'
    print("a", a)
    if  a in need_jpg:
        shutil.move(file_path + '/' + each_xml_dir, r'D:\liuan58\ocrdata\xingming-opt\presign_10000_short_xm_opt\xm_from_10000_short_badcase_jpg')

print("successed!")