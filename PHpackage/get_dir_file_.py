import os

def eachfile(filepath):
    pathdir = os.listdir(filepath) #将目录下所有文件（夹）名称，编入list
    #print(len(pathdir))
    x = -1
    child = [] #需要遍历的文件的路径的list
    for alldir in pathdir:
        if (alldir.find('DS_Store') != -1) or (alldir.find('.txt') == -1): continue
        x = x + 1
        child.append(os.path.join('%s/%s' % (filepath, alldir))) #拼接父级目录和文件（夹）名称
        #print(child[x], x)
    #print(child)
    return child, x #返回所需处理的文件列表和文件数