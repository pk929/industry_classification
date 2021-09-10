# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/9

# 系统包
import random

# 自定义包
from timing_task.mapper import *
from common import *
from classify_utils.classification_utils import *


def __train_industry_keyword_model(model):
    """
    加载、训练行业百度搜搜关键词分类算法模型
    :param model:
    :return:
    """
    log.info("开始加载、训练行业标题分类算法模型")
    start_time = time.time()
    print("keyword_1:" + str(time.time()))
    # 获取模型数据
    x_train = list()
    y_train = list()
    x_test = list()
    y_test = list()
    result_industry_keywords = queryBySQL_sqlal(CcsKeyWordBasicsMapper.S_KEY_WORD_GROUP_BY_INDUSTRY_ID, {})
    print("keyword_2:" + str(time.time()))
    if len(result_industry_keywords) <= 0:
        return

    for industry_keywords_dict in result_industry_keywords:
        industry_id = industry_keywords_dict.get("industry_id")
        key_word = industry_keywords_dict.get("key_word")
        company_num = industry_keywords_dict.get("company_num")
        if not check_contain_chinese(key_word):
            continue

        # for i in range(int(company_num)):
        x_train.append(key_word)
        y_train.append(industry_id)
        if industry_id not in y_test:
            x_test.append(key_word)
            y_test.append(industry_id)

    print("keyword_3:" + str(time.time()))

    # 标签列表
    label_list = list(set(y_train)).sort()
    y_train_len = len(y_train)
    random_list = random.sample(range(0, y_train_len), int(y_train_len / 4))  # 随机取1/3数据测试
    for ra in random_list:
        x_test.append(x_train[ra])
        y_test.append(y_train[ra])

    print("keyword_4:" + str(time.time()))
    score, matrix, report = model.train_model(x_train, y_train, x_test, y_test)
    print("keyword_5:" + str(time.time()))

    end_time = time.time()
    log.info("百度搜索关键词分类模型准确率:")
    log.info(score)
    log.info("百度搜索关键词分类模型混淆矩阵:")
    log.info(matrix)
    log.info("百度搜索关键词分类模型召回率:")
    log.info(report)
    log.info("百度搜索关键词分类模型训练时间:")
    log.info(end_time - start_time)


def get_industry_keyword_model(stop_list):
    """
    获取行业标题分类算法模型
    :param stop_list: 停用词列表
    :return:
    """
    myMultinomialNB = MyMultinomialNB(stop_list)
    __train_industry_keyword_model(model=myMultinomialNB)
    return myMultinomialNB
