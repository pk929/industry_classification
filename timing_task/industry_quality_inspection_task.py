# -*- ecoding: utf-8 -*-
# @Function: <行业质检>
# @Author: pkuokuo
# @Time: 2021/9/1

# 系统包
import random
import time

# 自定义包
from timing_task.mapper import *
from common import *


# import warnings
# warnings.filterwarnings("ignore")

# def industry_quality_inspection_task():
#     """
#     行业自动质检
#     :return:
#     """
#     # 获取行业数据
#     log.info("开始行业自动质检")
#     start_time = time.time()
#     result_second_industry_ids = queryBySQL_sqlal(CcsIndustryMapper.S_SECOND_INDUSTRY_ID, {})
#     second_industry_id_list = list()
#     for second_industry_ids_dict in result_second_industry_ids:
#         second_industry_id = second_industry_ids_dict.get("id")
#         second_industry_id_list.append(second_industry_id)
#
#     # second_industry_id_list.sort()
#     # log.info(second_industry_id_list)
#
#     x_train = list()
#     y_train = list()
#     x_test = list()
#     y_test = list()
#     label_set = set()
#     for industry_id in second_industry_id_list:
#         # 查询行业标题
#         result_industry_trace_titles = queryBySQL_sqlal(CcsTraceTitleBasicsMapper.S_TRACE_TITLE_BY_INDUSTRY_ID,
#                                                         {"industry_id": industry_id})
#         for industry_trace_titles_dict in result_industry_trace_titles:
#             trace_title = industry_trace_titles_dict.get("trace_title")
#             if not check_contain_chinese(trace_title):
#                 continue
#             x_train.append(trace_title)
#             y_train.append(industry_id)
#             label_set.add(industry_id)
#
#             if industry_id not in y_test:
#                 x_test.append(trace_title)
#                 y_test.append(industry_id)
#
#     #
#     label_list = list(label_set)
#     label_list.sort()
#     log.info("!!!!!!!!!!!!!!!!")
#     log.info(label_list)
#
#     log.info(len(x_train))
#     ll = len(y_train)
#     log.info(ll)
#     random_list = random.sample(range(0, ll), int(ll / 4))  # 随机取1/3数据测试
#     for ra in random_list:
#         x_test.append(x_train[ra])
#         y_test.append(y_train[ra])
#
#     stop_list = stopwordslist("text_similarity_modular/date/stopWord.txt")
#     myMultinomialNB = MyMultinomialNB(stop_list)
#     score, matrix, report = myMultinomialNB.train_model(x_train, y_train, x_test, y_test)
#     # print(x_train)
#     # print(y_train)
#     # print(x_test)
#     # print(y_test)
#     end_time = time.time()
#     log.info("准确率:")
#     log.info(score)
#     log.info("混淆矩阵")
#     log.info(matrix)
#     log.info("召回率")
#     log.info(report)
#     log.info("训练时间")
#     log.info(end_time - start_time)

#
