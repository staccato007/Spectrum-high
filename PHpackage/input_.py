def check_file_input_func(filepath):
    #print('1 ', filepath)
    filepath = repr(filepath) #转换为python字符串，忽略转义字符
    #print('2 ', filepath)
    filepath = filepath.replace('\\', '/') #替换反斜杠'\'
    #print('3 ', filepath)
    filepath = eval(filepath) #转换为普通字符串
    #print('4 ', filepath)
    filepath = filepath.rstrip('///') #去除末尾'/'
    return filepath
    
def input_func():
    print('请输入文件夹路径：', end=' ')
    filepath = input()
    filepath = check_file_input_func(filepath) #检查文件夹路径末尾是否有不合格的'\''/'
    print('请输入文件数：', end=' ')
    filenum = int(input())
    print('请选择分类指标（输入数字：1-压力，2-温度，3-不分类）：', end=' ')
    class_type = int(input())
    return filepath, filenum, class_type