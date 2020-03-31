# -*- coding: UTF-8 -*-


#使用时先把原图转为高一个位数的图片名称，再转回去
import os

def convert(dir):
    file_list = os.listdir(dir)
    n=0
    addnum = 2010 #自己设置，图片从哪个序号开始

    print(file_list)
    for filename in file_list:
        oldname=dir+file_list[n]
        newn = n + addnum - 1
        #设置新文件名
        #s = str(n + 1)
        s=str(newn+1)
        st=s.zfill(7) #这里的数字为名称的总数位，比如000000递增就是6
        newname=dir+st+'.jpg'

        #用os模块中的rename方法对文件改名
        os.rename(oldname,newname)
        print(oldname,'====》',newname)

        n+=1

if __name__ == '__main__':
   dir = input('please input the operate dir:')
   convert(dir)
