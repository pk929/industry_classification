# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包
from urllib import request
from bs4 import BeautifulSoup
from urllib.parse import quote
import string

# 自定义包
from common.flask_log import Log as log

def url_analysis(url):
    """
    获取网页标题、描述、关键词
    :param url: 解析网址
    :return:
    """
    title, description, keywords = "", "", ""
    try:
        url = quote(url, safe=string.printable)
        page = request.urlopen(url)
        contents = page.read()
        soup = BeautifulSoup(contents, "html.parser")
        title = str(soup.title.string)
        description_bs4 = soup.find(attrs={"name": "description"})
        keywords_bs4 = soup.find(attrs={"name": "keywords"})
        if description_bs4 is not None:
            description = description_bs4['content']
        if keywords_bs4 is not None:
            keywords = keywords_bs4['content']

    except Exception as e:
        log.error_ex("utils_url_analysis_e:" + str(e))
    return title, description, keywords


def str_is_None(st):
    """
    判断字符是否为空
    :param st:
    :return:
    """
    if st is None or st == '' or st == 'None' or st == 'null':
        return True
    return False

