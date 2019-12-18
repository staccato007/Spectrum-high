
def getpressure(ffstr): #输入simple文件名
    fstr = ffstr
    bar_l = fstr.rfind('bar') #获取压力单位'bar'位置
    fstr = fstr[:bar_l+1] #裁去'bar'之后的字符
    pressure_num_l = fstr.rfind('_')
    pstr = fstr[pressure_num_l+1:bar_l] #获取数值字符串
    #print(pstr)
    if '-' in pstr: #将可能的'-'替换为'.'
        pstr = pstr.replace('-', '.')
        #print(pstr)
        pstr = pstr[:pstr.find('.')] + '.' + pstr[pstr.rfind('.')+1:]
    return pstr #返回字符串格式的压力值