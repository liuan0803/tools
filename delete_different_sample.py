########比较两个文件夹中的内容，删除差集############

import os

srcPath = '/data/liuan/data/liuan/project/kerasyolov3/VOCdevkit/VOC2007/addannotations'
destPath = '/data/liuan/data/liuan/project/kerasyolov3/VOCdevkit/VOC2007/Annotations'
src_name = os.listdir(srcPath)
dest_name = os.listdir(destPath)
for temp in dest_name:
    if temp not in src_name:
        target = os.path.join(destPath, temp)
        os.remove(target)
