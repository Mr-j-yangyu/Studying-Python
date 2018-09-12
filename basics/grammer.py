# -*- coding: utf-8 -*-
"""
   practice code
"""
__author__ = 'jiwenxiang'

import calendar
import datetime
import logging.config
import sys
from dateutil.relativedelta import relativedelta
from functools import reduce
from enum import Enum, unique
from io import StringIO
from io import BytesIO
import os # 调用操作系统提供的接口函数。
import json
import pickle
from multiprocessing import Process  #进程模块
from multiprocessing import Pool
import multiprocessing
import threading
import  psutil #跨平台的获取进程和系统应用情况 pip install psutil
import re #正则表达模块
import requests
import http.cookiejar

def date_sample():
    """
       日期相关
    """
    datetime.date(2017, 12, 17)
    cal_date=datetime.date.today()
    print(calendar.monthrange(cal_date.year, cal_date.month))
    print(cal_date +datetime.timedelta(1))
    print(cal_date + relativedelta(months=-1))
    print(cal_date + datetime.timedelta(days=6 - cal_date.weekday()))
    print(round(1/3, 4))


def iteration_sample():
    """
        切片
    """
    L = list(range(50))
    print(L[:2]) #前两个
    print(L[-10:]) #后10个
    print(L[:10:2]) #前10个每隔2取一个

    """
        迭代Iterable，list、tuple、string都可以是迭代对象 isinstance('abc', Iterable)
        注意和Iterator区别，Iterator可以调用next()，看做一个数据流
    """
    dict = {'a': 1, 'b': 2, 'c': 3}
    for key in dict:
        print(key)
    for value in dict.values():
        print(value)
    for k, v in dict.items():
        print(k, v)

    """
       列表生成式
    """
    lists = [x * x for x in range(1, 11) if x % 2 == 0]
    print(lists)

    """
       生成器generator，边循环变计算下个值，节省空间
    """
    g = (x * x for x in range(10))
    for n in g:
        print(n, end="\t")
    # while(1):
    #     try:
    #         print(next(g), end="\t")
    #     except StopIteration as e:
    #         print("遍历结束")
    #         break
    #     finally:
    #         pass


def higher_function(mapfuc, reducefunc, filterfunc, sortedfunc):
    """
         map/reduce/filter/sorted
    """
    L = list(range(10))
    mapl = list(map(mapfuc, L))
    print(mapl)
    reducel = reduce(reducefunc, L)
    print(reducel)
    filterl = list(filter(filterfunc, L))
    print(filterl)
    word = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    sortedl =list(sorted(word, key=sortedfunc, reverse=True))
    print(sortedl)

def func_sample():
    """
        返回函数
            注意:返回闭包（内部函数引用外部函数的参数和局部变量，相关参数和变量都保存在返回的函数中）
            时牢记一点：返回函数不要引用任何循环变量,下面例子返回9,9,9 不是1，4,9
    """
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)

    for f in fs:
        print(f())

class ClassTest(object):
    """
           类相关
    """
    def __init__(self, param1=None, param2=None):
        #实例变量
        self.parm = param1
        self.parm2 = param2

    def general_methd(self, var):
        #类变量
        ClassTest.classVar = var
        print(self.parm+var+ClassTest.classVar)


class EnumTest(Enum):
    """
        枚举类
             定义： Enum('Month', {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4})
             遍历：for name, member in EnumTest.__members__.items():
    """
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 1
    Sat = 6


def fileIO_sample():
    """
        IO流相关
            mode:r,rb,w,wb,a，a+  (a表示追加，+表示读写，b表示二进制)
            errors:文件包含非法编码字符时

            seek(offect,whence) whence：给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    """
    with open('E:/tmp2.txt', mode='a+', encoding='utf-8',  errors='ignore') as f:
        f.write("hellow world")
        index = f.tell() #当前游标位置
        f.seek(0,0)
        print(f.read())

    """
        系统目录和文件
    """
    print("系统变量java_home: %s" % os.environ.get("JAVA_HOME"))
    print("绝对路径: %s" % os.path.abspath('.'))
    print("新建目录路径: %s" % os.path.join(os.path.abspath('.'), 'testdir'))
    if not os.path.exists(os.path.join(os.path.abspath('.'), 'testdir')):
        print("新建目录: %s" % os.mkdir(os.path.join(os.path.abspath('.'), 'testdir')))
    else:
        print("目录:%s 已存在" %os.path.join(os.path.abspath('.'), 'testdir'))

    print([x for x in os.listdir('E:/PyCharm') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

    """
        序列化
    """
    d = dict(name='Bob', age=20, score=88)
    # pickle.dumps(d,f) # 序列化为二进制
    # pickle.load(f) # 反序列化出对象

    d = dict(name='Bob', age=20, score=88)
    json.dumps(d)
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    json.loads(json_str)
    print(json.dumps(ClassTest(1, 2), default=lambda obj: obj.__dict__)) #序列化对象

def print_some(x):
    print("%s 当前进程：%s 当前线程：%s" %(x,multiprocessing.current_process().name,threading.current_thread().name))

def process_thread():
    """
         多进程，linux 直接调用os.fork()在当前进程中称为父进程）复制了一份（称为子进程），分别父进程和子进程内返回，子进程返回0
    """
    p = Process(target=print_some, args=('test',), name="selfProcess")
    p.start()
    p.join()
    p = Pool(4)
    for i in range(5):
        p.apply_async(print_some, args=(i,))
    p.close() #不允许添加新子进程
    p.join()

    """
        多线程
         1.多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，
            所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改
         2.local_school = threading.local() local_school.x =z,  线程对x读写互不影响
         3.利用managers 模块实现分布式进程
    """
    t = threading.Thread(target=print_some, name='LoopThread', args=(6,))
    t.start()
    t.join()

def regular_expression():
    """
        正则表达式
          \d ： 数字、 \w ： 字母 、.：任意字符 、* ：任意个字符、 + ：至少一个字符、
           ? ： 0个或1个字符、{n}：n个字符、{n,m} ：n-m个字符：、\s ：空格
           A|B ：匹配A或者B、^ \d ：数字开头、\d$ ：数字结尾
        eg: \d{3}\s+\d{3,8}  可以匹配以任意个空格（\s+）隔开的带区号（\d{3}）的电话号码（\d{3,8}
        r': 不需要用转义
    """
    m =re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
    if m:
        print(m.group(0))
    else:
        print('not match')

    print(re.split(r'[\s\,]+', 'a,b, c  d'))

def notes():
    """
        Pillow 图像处理
        chardet检测编码

    """

def requests_sample():
    """
        http请求

    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'Referer':'https://www.zhihu.com/'
    }
    params = {'type':'content', 'q':'阿达'}
    cookies = http.cookiejar.LWPCookieJar('cookies')
    cookies.load(ignore_discard=True)
    rs = requests.get("https://www.zhihu.com", params=params, headers=headers, cookies=cookies)
    print(rs.text)

def test(*k):
    print(k[-1:])

if __name__ == '__main__':

     date_sample()
    # iteration_sample()
    # higher_function(lambda x: str(x), lambda x, y: x*10+y, lambda x:x%2==0,lambda x:x[1])
    # func_sample()
    # for name, member in EnumTest.__members__.items():
    #     print(name, '=>', member, ',', member.value)
    # classt = ClassTest(1, 2)
    # classt.general_methd(3)
    # fileIO_sample()
    # regular_expression()
    # requests_sample()