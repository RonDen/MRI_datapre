import pydicom
import matplotlib.pyplot as plt
import scipy.misc
import pandas as pd
import numpy as np
import os


def Dcm2png(file_path):
    # 获取所有图片名称
    c = []
    names = os.listdir(file_path)  # 路径
    # 将文件夹中的文件名称与后边的 .dcm分开
    for name in names:
        index = name.rfind('.')
        name = name[:index]
        c.append(name)

    for files in c:
        picture_path = file_path + "\\" + files + ".dcm"
        out_path = file_path + "\\" + files + ".png"
        ds = pydicom.read_file(picture_path)
        img = ds.pixel_array  # 提取图像信息
        scipy.misc.imsave(out_path, img)

    print('all is changed')


Dcm2png('F:\\PKU\\SR\\data\\Test1Set\\patient19\\P19dicom')