import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from show_plot_ import plot_scatter_func
import get_spec_data_

def cut_list_func(dlist, lb, ub): #去除列表dlist中下界lb和上界ub之外的数据
    for i in dlist[:]:
        if (i[1] < lb or i[1] > ub):
            # print(i)
            dlist.remove(i)
        # print(dlist)
    return dlist #返回处理后的列表

def remove_abnormal_data_func(datalist): #消除光谱数据中的异常数据点
    split_tuple = get_spec_data_.split_spec_data_func(datalist)
    wavenumber = split_tuple[0]
    intensity = split_tuple[1]
    # print(wavenumber)
    # print(intensity)
    dmean = np.mean(intensity)
    # dmax = np.max(intensity)
    # dmin = np.min(intensity)
    dstd = np.std(intensity)
    upboundry = dmean + 1.5 * dstd
    lowboundry = dmean - 1.5 * dstd
    # print(dmean, dstd, lowboundry, upboundry, (dstd/dmean))
    if (dstd/dmean) <= 0.05: #递归至列表的百分偏差小于2%
        plot_scatter_func((dstd/dmean), wavenumber, intensity, [0,0], 0)
        return datalist
    else:
        dlist = cut_list_func(datalist, lowboundry, upboundry)
        plot_scatter_func((dstd/dmean), wavenumber, intensity, [0,0], 0)
        # print(dlist)
        return(remove_abnormal_data_func(dlist))
    return datalist

def get_Polynomial_Features_func(datalist):
    model = Pipeline([('poly', PolynomialFeatures(degree=1)),('linear', LinearRegression(fit_intercept=False))])
    wavenumber = []
    intensity = []
    for i in datalist[:]: #将二维列表，拆分为波数和信号值得两个列表
        wavenumber.append(i[0])
        intensity.append(i[1])
    x = np.array(wavenumber) #创建numpy数组
    y = intensity
    model = model.fit(x[:, np.newaxis], y)
    R2 = model.score(x[:, np.newaxis], y)
    # print(model.named_steps['linear'].coef_)
    # print(R2)
    coefficient = model.named_steps['linear'].coef_
    # plot_scatter_func(wavenumber, intensity, coefficient, R2, [wavenumber[0], wavenumber[len(wavenumber)-1]], [0, 0])

    return (coefficient, R2)

def get_spec_height_func(coef, maxintensity, maxlocation):
    x = 0
    power = -1
    for i in coef:
        power = power + 1
        x = x + i * maxlocation ** power
        # print(i, x)
    return maxintensity - x

