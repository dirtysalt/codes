#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) dirlt

############################################################
# https://blog.csdn.net/BigBoy_Coder/article/details/103406332
import requests
import time
import hashlib
import random


class ximalaya(object):

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Safari/537.36"
        }

    def getServerTime(self):
        """
        获取喜马拉雅服务器的时间戳
        :return:
        """
        # 这个地址就是返回服务器时间戳的接口
        serverTimeUrl = "https://www.ximalaya.com/revision/time"
        response = requests.get(serverTimeUrl,headers = self.headers)
        return response.text

    def getLocalTime(self):
        return str(round(time.time() * 1000))

    def getSign(self,serverTime):
        """
        生成 xm-sign
        规则是 md5(ximalaya-服务器时间戳)(100以内随机数)服务器时间戳(100以内随机数)现在时间戳
        :param serverTime:
        :return:
        """
        nowTime = self.getLocalTime()

        sign = str(hashlib.md5("himalaya-{}".format(serverTime).encode()).hexdigest()) + "({})".format(str(round(random.random()*100))) + serverTime + "({})".format(str(round(random.random()*100))) + nowTime
        # 将xm-sign添加到请求头中
        self.headers["xm-sign"] = sign
        return sign

_xmly = ximalaya()

def GetSign():
    return _xmly.getSign(_xmly.getLocalTime())

############################################################

import functools
from bs4 import BeautifulSoup

@functools.lru_cache()
def getDownloadLink(item_id):
    url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(item_id)
    print(url)
    sign = GetSign()
    r = requests.get(url, headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36', 'Content-Type': 'application/json',
        'xm-sign':sign,
    })
    print(r.status_code, r.content)
    link = r.json()['data']['src']
    return link


def loadElements(inputFile):
    html = open(inputFile, encoding='utf8').read()
    bs = BeautifulSoup(html)
    elements = bs.select('#anchor_sound_list > div.sound-list._is > ul > li > div.text.lF_')
    return elements


def parseElement(x):
    y = next(x.children)
    link = y.attrs['href']
    title = y.text
    item_id = link.split('/')[-1]
    return {'item_id': item_id,'title':title}
