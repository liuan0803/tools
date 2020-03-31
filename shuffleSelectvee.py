# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 16:23
# @Author  : 2014Vee
# @Email   : 1976535998@qq.com
# @File    : shuffleSelect.py
# @Software: PyCharm
##深度学习过程中，需要制作训练集和验证集、测试集。
#其中把原始的图片和对应的xml文件分为训练集和测试集
#训练集还是在原始文件夹，测试集存放再新建的output中

import os, random, shutil
def moveFile(fileDir):
        pathjpgDir = os.listdir(fileDir + "orgData/")    #取图片的原始路径
        pathtxtDir = os.listdir(fileDir + "orgXml/")     #取txt的原始路径
        dictionary = list(zip(pathjpgDir, pathtxtDir))

        filenumber=len(pathjpgDir)
        rate=0.1    #自定义抽取图片的比例，比方说100张抽10张，那就是0.1
        picknumber=int(filenumber*rate) #按照rate比例从文件夹中取一定数量图片
        iterator_num = int(filenumber / picknumber)
        sample = []
        ####写一个循环，隔一定数目就抽取一张移动到其他的文件夹
        n = 0 ##记录数字
        for pick in dictionary:
            if (n >= iterator_num and n % iterator_num == 0):
                sample.append(pick)
            n = n + 1
        #sample = random.sample(dictionary, picknumber)  #随机选取picknumber数量的样本图片
        print(sample)
        targetDir = fileDir + 'output/'
        if not os.path.exists(targetDir):
            os.makedirs(targetDir)
        for name in sample:
                if not os.path.exists(targetDir+'jpgout/'):
                    os.makedirs(targetDir+'jpgout/')
                if not os.path.exists(targetDir + 'xmlout/'):
                    os.makedirs(targetDir + 'xmlout/')
                shutil.move(fileDir+"orgData/"+ name[0], targetDir+"jpgout/"+name[0])
                shutil.move(fileDir +"orgxml/"+ name[1], targetDir +"xmlout/"+ name[1])
        return

if __name__ == '__main__':
	fileDir = "C:/Users/2014Vee/Desktop/data/"    #源图片和标签文件夹路径
	moveFile(fileDir)
