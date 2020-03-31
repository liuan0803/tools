# -*- encoding: utf-8 -*-
'''
@File    :   shuffle_generate_train_val_data.py    
@Version :   1.0 
@Author  :   liuan
@Contact :   liuan0803@126.com
@License :   (C)Copyright liuan From UESTC
@Modify Time :   2020/3/20 11:38
@Desciption  :   None
'''

import os
import random

xmlfilepath = r'D:\liuan58\ocrdata\xingming-opt\drivinglic_1_trainval\Annotations_1'
saveBasePath = r'D:\liuan58\ocrdata\xingming-opt\liuyan_data\txtsave'

trainval_percent = 1.0
train_percent = 0.28
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

print("train and val size", tv)
print("train size", tr)
ftrainval = open(os.path.join(saveBasePath, 'trainval.txt'), 'w')
ftest = open(os.path.join(saveBasePath, 'test.txt'), 'w')
ftrain = open(os.path.join(saveBasePath, 'train.txt'), 'w')
fval = open(os.path.join(saveBasePath, 'val.txt'), 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()