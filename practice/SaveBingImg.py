# -*- coding: utf-8 -*-
"""
  保存Bing每日一图
"""
import urllib.request
import requests
import os.path
import ctypes
import sys


# 请求网页，跳转到最终 img 地址
def get_img_url(url='https://area.sinaapp.com/bingImg/'):
    r = requests.get(url)
    img_url = r.url # 得到图片文件的网址
    print('Get img url is  ', img_url)
    return img_url


def save_img(img_url,dirname):
    # 保存图片到磁盘文件夹dirname中
    try:
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        # 获得图片文件名，包括后缀
        basename = os.path.basename(img_url)
        # 拼接目录与文件名，得到图片路径
        filepath = os.path.join(dirname, basename)
        print('Start download img from',img_url,'...')
        # 下载图片，并保存到文件夹中
        urllib.request.urlretrieve(img_url, filepath)
    except IOError as e:
        print('文件操作失败', e)
    except Exception as e:
        print('错误 ：', e)
    print("Save", filepath, "successfully!")

# 设置图片绝对路径 filepath 所指向的图片为壁纸
def set_img_as_wallpaper(filepath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 0)


if __name__ == '__main__':
    args = sys.argv
    img_url = get_img_url(args[1])
    filepath = save_img(img_url, args[2])  # 图片文件的的路径
    # set_img_as_wallpaper(filepath)