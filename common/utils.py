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


def stopwordslist(filepath):
    """
    读取停用词
    :param filepath:
    :return:
    """
    stopwords = []

    try:
        stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    except Exception as e:
        log.error('utils_stopwordslist_e:' + str(e))
    finally:
        return stopwords


def check_contain_chinese(check_str):
    """
    判断文本中是否含有中文字符
    :param check_str:
    :return:
    """
    for ch in check_str.encode('utf-8').decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

