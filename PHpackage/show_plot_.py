import matplotlib.pyplot as plt
import numpy as np
import os

def plot_scatter_func(title, sx, sy, coef_, R2):
    maxx = sx[0]
    minx = sx[0]
    for i in sx:
        if i > maxx: maxx = i
        if i < minx: minx = i
    maxy = sy[0]
    miny = sy[0]
    for i in sy:
        if i > maxy: maxy = i
        if i < miny: miny = i
    x = np.linspace(minx, maxx, 500)
    y = []
    for i in x:
        yy = 0
        power = -1
        for j in coef_:
            power = power + 1
            yy = yy + j * (i ** power)
        y.append(yy)
    # print(x)
    # print(y)
    plt.scatter(sx, sy, label='Spectrum point', color='b', s=5, alpha=0.9)
    plt.plot(sx, sy, color='b', alpha=0.5)
    plt.plot(x, y, label='Fit Curve', color='r')
    plt.xlabel('Wavenumber/cm${^{-1}}$')
    plt.ylabel('Intensity/a.u.')
    plt.title(f'{title}')
    plt.legend()
    plt.show()

# plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
# plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题
# plt.rcParams['font.sans-serif']=['SimHei'] #title可以是中文
# plot_scatter_func('hehe', [1,2,3,4], [1, 4, 9, 16], [0, 0 ,1], 0.999)
