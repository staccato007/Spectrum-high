import os

def output_func(final_data, out_filepath):
    parent_path = os.path.dirname(out_filepath) #获取父级目录
    dirname = os.path.basename(out_filepath)
    ff = open(f'{parent_path}/{dirname}output.txt', 'w') #以只写方式打开（创建输出文件）
    for x in final_data:
        # print(x.name, x.intens, end='\n')
        ff.write(f'{x.pressure}')
        for i in x.intens:
            ff.write(f' {i}')
        ff.write(f'\n')
    ff.close()
    print('输出文件已经放在:',f'{parent_path}/{dirname}output.txt')