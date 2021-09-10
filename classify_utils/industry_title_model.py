# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/7

# 系统包
import random
import time

# 自定义包
from timing_task.mapper import *
from common import *
from classify_utils.classification_utils import *


def __train_industry_title_model(model):
    """
    加载、训练行业标题分类算法模型
    :return:
    """
    log.info("开始加载、训练行业标题分类算法模型")
    start_time = time.time()
    print("title_1:" + str(time.time()))
    # 获取模型数据
    x_train = list()
    y_train = list()
    x_test = list()
    y_test = list()
    result_industry_trace_titles = queryBySQL_sqlal(CcsTraceTitleBasicsMapper.S_TRACE_TITLE_GROUP_BY_INDUSTRY_ID, {})
    print("title_2:" + str(time.time()))
    for industry_trace_titles_dict in result_industry_trace_titles:
        trace_title = industry_trace_titles_dict.get("trace_title")
        industry_id = industry_trace_titles_dict.get("industry_id")
        if not check_contain_chinese(trace_title):
            continue
        x_train.append(trace_title)
        y_train.append(industry_id)
        if industry_id not in y_test:
            x_test.append(trace_title)
            y_test.append(industry_id)
    print("title_3:" + str(time.time()))
    label_list = list(set(y_train)).sort()
    y_train_len = len(y_train)
    random_list = random.sample(range(0, y_train_len), int(y_train_len / 4))  # 随机取1/3数据测试
    for ra in random_list:
        x_test.append(x_train[ra])
        y_test.append(y_train[ra])

    # # 获取行业数据
    # result_second_industry_ids = queryBySQL_sqlal(CcsIndustryMapper.S_SECOND_INDUSTRY_ID, {})
    # second_industry_id_list = list()
    # for second_industry_ids_dict in result_second_industry_ids:
    #     second_industry_id = second_industry_ids_dict.get("id")
    #     second_industry_id_list.append(second_industry_id)
    #
    # x_train = list()
    # y_train = list()
    # x_test = list()
    # y_test = list()
    # label_set = set()
    # for industry_id in second_industry_id_list:
    #     # 查询行业标题
    #     result_industry_trace_titles = queryBySQL_sqlal(CcsTraceTitleBasicsMapper.S_TRACE_TITLE_BY_INDUSTRY_ID,
    #                                                     {"industry_id": industry_id})
    #     for industry_trace_titles_dict in result_industry_trace_titles:
    #         trace_title = industry_trace_titles_dict.get("trace_title")
    #         if not check_contain_chinese(trace_title):
    #             continue
    #         x_train.append(trace_title)
    #         y_train.append(industry_id)
    #         label_set.add(industry_id)
    #
    #         if industry_id not in y_test:
    #             x_test.append(trace_title)
    #             y_test.append(industry_id)
    #
    # label_list = list(label_set)
    # label_list.sort()
    # log.info("!!!!!!!!!!!!!!!!")
    # log.info(label_list)
    #
    # log.info(len(x_train))
    # ll = len(y_train)
    # log.info(ll)
    # random_list = random.sample(range(0, ll), int(ll / 4))  # 随机取1/3数据测试
    # for ra in random_list:
    #     x_test.append(x_train[ra])
    #     y_test.append(y_train[ra])
    print("title_4:" + str(time.time()))
    score, matrix, report = model.train_model(x_train, y_train, x_test, y_test)
    print("title_5:" + str(time.time()))
    end_time = time.time()
    log.info("准确率:")
    log.info(score)
    log.info("混淆矩阵")
    log.info(matrix)
    log.info("召回率")
    log.info(report)
    log.info("训练时间")
    log.info(end_time - start_time)


def get_industry_title_model(stop_list):
    """
    获取行业标题分类算法模型
    :param stop_list: 停用词列表
    :return:
    """
    myMultinomialNB = MyMultinomialNB(stop_list)
    __train_industry_title_model(model=myMultinomialNB)
    return myMultinomialNB




