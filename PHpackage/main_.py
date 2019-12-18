import sys
import os
import numpy as numpy
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
import input_
import get_dir_file_
import get_spec_data_
import get_feature_
import get_classtype_
import output_
from show_plot_ import plot_scatter_func

class final_data_point():
    def __init__(self, pressure, intens_sum):
        self.pressure = pressure
        self.intens = []
        self.intens_sum = intens_sum

def get_sort_key_wavenumber(elem):
    return elem[0]

def get_sort_key_intensity(elem):
    return elem[1]

input_tuple = input_.input_func() #元组 = （数据文件夹路径，文件数，分类依据（1=压力，2=温度，3=不分类））
eachfile_tuple = get_dir_file_.eachfile(input_tuple[0]) #元组 =（需处理文件的路径列表，文件数-1）
allfiles = eachfile_tuple[0]
filesum = eachfile_tuple[1]
if input_tuple[1] != eachfile_tuple[1] + 1:
    print('输入的文件数与目录下找到的所需文件数不一致，请检查文件名')
    print(f'找到了 {eachfile_tuple[1] + 1} 个文件:')
    for f in allfiles:
        print(' ',f)
    sys.exit(0)
final_data = [] #初始化最终数据
dic_classtype_to_keynum = {} #初始化查找字典
data_lines = -1
for filepath in allfiles:
    datalist_original = get_spec_data_.get_spec_data_func(filepath)
    datalist = sorted(datalist_original, key=get_sort_key_intensity) #以intensity为key排序数据列表
    maxvalue = datalist[len(datalist)-1][1] #获取最大的信号值
    maxlocation = datalist[len(datalist)-1][0] #获取最大信号值的波数（位置）
    # print(len(datalist))
    datalist = get_feature_.remove_abnormal_data_func(datalist) #剔除异常值
    # print(len(datalist))
    polyfittuple = get_feature_.get_Polynomial_Features_func(datalist) #获取回归结果元组，包括回归系数和R2
    coeflist = polyfittuple[0]
    fitscore = polyfittuple[1]

    split_tuple = get_spec_data_.split_spec_data_func(datalist_original)
    wavenumber = split_tuple[0]
    intensity = split_tuple[1]
    plot_scatter_func(os.path.basename(filepath), wavenumber, intensity, coeflist, fitscore)

    nameu = os.path.basename(filepath) #获取simple文件名
    intensityu = get_feature_.get_spec_height_func(coeflist, maxvalue, maxlocation) #获取峰高值
    pressureu = get_classtype_.getpressure(nameu) #获取该文件压力
    if pressureu in dic_classtype_to_keynum: #如果该压力已经在字典中
        pressure_index = dic_classtype_to_keynum[pressureu] #找到该压力对应的序号（行索引）
        final_data[pressure_index].intens.append(intensityu) #将新峰高加入峰高列表
        final_data[pressure_index].intens_sum = final_data[pressure_index].intens_sum + 1 #峰高值个数+1
    else: #如果字典中没有该压力
        data_lines = data_lines + 1 #总行数+1（压力值个数）
        dic_classtype_to_keynum[pressureu] = data_lines #添加该压力对应行索引的键值对
        x = final_data_point(pressureu, 0) #新建数据点
        x.intens.append(intensityu) 
        final_data.append(x)

output_.output_func(final_data, input_tuple[0])

