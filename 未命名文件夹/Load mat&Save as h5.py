#!/usr/bin/python
#load .mat file
import scipy.io as scio
import numpy as np
import h5py
dataFile = '/Users/zhangdan/Documents/GitHub/Volve-Fault-Detection/DNN_NEW/Start.mat'
data = scio.loadmat(dataFile)
Training_X=data['Training_X']#存储数据为变量，data为Python字典
Training_Y=data['Training_Y']
Dev_X=data['Dev_X']
Dev_Y=data['Dev_Y']
Test_X=data['Test_X']
Test_Y=data['Test_Y']
X_Abnormal=data['X_Abnormal']
#save as .h5
file=h5py.File('Dataset.h5','w')#创建h5文件
file.create_dataset('Training_X',data=Training_X)#写入变量
file.create_dataset('Training_Y',data=Training_Y)
file.create_dataset('Dev_X',data=Dev_X)
file.create_dataset('Dev_Y',data=Dev_Y)
file.create_dataset('Test_X',data=Test_X)
file.create_dataset('Test_Y',data=Test_Y)
file.create_dataset('X_Anomaly',data=X_Abnormal)
file.close()#关闭文件
#read .h5
# 读方式打开文件
file=h5py.File('Dataset.h5','r')
# 尽管后面有 '[:]', 但是矩阵怎么进去的就是怎么出来的，不会被拉长（matlab后遗症）
train_set_data = file['train_set_x'][:]
train_set_y = file['train_set_y'][:]
train_set_img_num= file['train_set_img_num'][:]
# .........
file.close()

#存为。mat
import scipy.io as sio
sio.savemat('saveddata.mat', {'Y_train': Y_train,'Y_test': Y_test}) 
