# -*- coding: utf-8 -*-
"""
   查找制定文件
"""
import os # 调用操作系统提供的接口函数。
import datetime
import  time
import  sys

def find_file_in_dir(target_file, *source_dir):

    target_file_path = []

    if not target_file  and not source_dir:
        print( '参数不能为空')
    startt = time.clock()
    for dir in source_dir:
        if os.path.exists(dir):
            for parent, dirnames, filenames in os.walk(dir):
                print("当前搜索目录：%s" % parent)
                # for dirname in dirnames:
                #     print(("    {0}\n").format(dirname))
                for filename in filenames:
                   if filename == target_file:
                       target_file_path.append(os.path.join(parent, filename))
        else:
            print('目录不存在 %s' % dir)
            pass
    endt = time.clock()
    print('==========结果==========')
    print('搜索时间：%f s' % (endt-startt))
    if len(target_file_path) == 0:
        print('没有找到目标文件')
    else:
        for x in  target_file_path:
            print(x)


if __name__ == '__main__':
    args = sys.argv

    if len(args) > 2:
      find_file_in_dir(args[1], args[2])
    else:
      find_file_in_dir('dataworks3.png','E:\文档_项目')

