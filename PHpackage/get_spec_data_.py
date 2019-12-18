import matplotlib.pyplot as plt
import numpy as np

def split_spec_data_func(datalist):
    wavenumber = []
    intensity = []
    for i in datalist[:]: #将二维列表，拆分为波数和信号值得两个列表
        wavenumber.append(i[0])
        intensity.append(i[1])
    return wavenumber, intensity

def get_spec_data_func(filename): #从文件中获取光谱数据
    f = open(filename, 'r')
    string = []
    data = []
    Num_of_filelines = -1
    for line in f:
        Num_of_filelines = Num_of_filelines + 1 #数据点个数（行数）
        string.append(line.replace('\n', '')) #去除换行符
        if line.find('\t') != -1:
            data.append([float(string[Num_of_filelines][:line.find('\t')]), float(string[Num_of_filelines][line.find('\t'):])])
        if line.find(' ') != -1:
            data.append([float(string[Num_of_filelines][:line.find(' ')]), float(string[Num_of_filelines][line.find(' '):])])
    # print(string)
    # print(data[:])
    f.close()
    return data #范围以行为单位的列表，数据为单位的二维列表

# plot_scatter_func(wavenumber, intensity, [1,1,0.000432], 0.95, [wavenumber[0], wavenumber[len(wavenumber)-1]], [0, 0])
