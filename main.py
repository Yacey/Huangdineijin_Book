#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author: 栋人佳Dougle（小红书同名）
#@Date: 2024-01-17

import requests as re
import pandas as pd
import csv
from lxml import etree
from itertools import zip_longest
import time


def get_page_url(html):
    # 获得 《黄帝内经-素问》 子页面的url
    page_url = []

    tree = etree.HTML(html)
    url_M = tree.xpath('//div[@class="content"]//td/a/@href')
    # for i in url_M:
    #     page_url.append(i)
    # print(page_url)
    # return page_url
    return url_M


def getBookUrl(url):

    for i in url:
        print(i)
        url_Main = i
        headers = {
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        }

        res = re.get(url_Main, headers=headers)
        res.encoding = 'gbk'
        html = res.text
        tree = etree.HTML(html)
        title = tree.xpath('//div[@class="title"]/h2/text()')
        print(title)




# def in_GetMes(url, proxies):
#     inurl = 'https://huggingface.co'
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
#         "Upgrade-Insecure-Requests": "1",
#     }
#
#     for i in url:
#         inurl = inurl + i
#         # print(inurl)
#         res = re.get(url=inurl, headers=headers, proxies=proxies)
#         inurlput = inurl
#         # print(inurlput+"--------------")
#         inurl = 'https://huggingface.co'
#         likesurl = inurl + '/api/models' + i + '/likers'
#         likesres = re.get(url=likesurl, headers=headers)
#         likesInfo = likesres.json()
#         # print(likesurl)
#         html = res.text
#         tree = etree.HTML(html)
#         stdio = tree.xpath('//a[@class="text-gray-400 hover:text-blue-600"]/text()')
#         modelname = tree.xpath('//a[contains(@class,"font-mono")]/text()')
#         tasks = tree.xpath('//div[contains(@class,"tag-ico")]/following::span[1]/text()')
#         Downloads = tree.xpath('//div[contains(@class,"justify-between")]//dd/text()')
#         cleaned_downloads = [download.replace(",", "") for download in Downloads]
#         likes = [len(likesInfo)]
#         Downlastmonth = tree.xpath('//dl/dd[@class="font-semibold"]/text()')
#         Downlastmonth1 = [download.replace(",", "") for download in Downlastmonth]
#         # Downlastmonth = Downlastmonth1[0]
#
#         # print(Downlastmonth1)
#         # print(likes[0])
#         # 如何判断studio中如果为空值，那么就赋值为一个空格
#         # 获取当前作用域的变量名列表
#         variable_names = ["stdio", "modelname", "likes", "cleaned_downloads", "tasks", "Downlastmonth"]
#
#         # 遍历变量名，处理相应的列表
#         for variable_name in variable_names:
#             my_list = locals()[variable_name]
#             my_list[:] = my_list or [" "]
#
#         print(stdio)
#         print(modelname)
#         print(likes)
#         print(tasks)
#         all_datas = stdio + modelname + tasks + cleaned_downloads + likes + Downlastmonth1
#         all_datas.append(inurlput)
#         # print(all_datas)
#         save_data(all_datas=all_datas)



if __name__ == '__main__':
    # a = time.time()
    url = 'https://www.ee99.net/a/zhongyiguji/huangdinajing/2012/0828/2324.html'
    headers = {
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",

    }

    proxies = {
        # "http": "http://203.74.125.18:8888",
        # "https": "https://93.157.248.108:88"
        # "https": "https://204.48.31.203:80"
    }

    res = re.get(url, headers=headers)
    html = res.text
    # url_M = tree.xpath('//div[@class="content"]//td/a/@href')
    url_M = get_page_url(html)
    print(url_M)  # 测试是否获取到了子页面的url
    getBookUrl(url_M)
