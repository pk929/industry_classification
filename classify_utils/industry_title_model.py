# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/7

# 系统包
import random
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier


# 自定义包
from common import *
from classify_utils.classification_model_utils import *
from mapper import *


# def __train_network_model(model):
#     """
#     神经网络模型
#     :param model:
#     :return:
#     """
#     log.info("开始加载、训练行业标题分类神经网络算法模型")
#     start_time = time.time()
#     # 获取模型数据
#     x_train = list()
#     y_train = list()
#     x_test = list()
#     y_test = list()
#     result_industry_trace_titles = queryBySQL_sqlal(CcsTraceTitleBasicsMapper.S_TRACE_TITLE_GROUP_BY_INDUSTRY_ID, {})
#     for industry_trace_titles_dict in result_industry_trace_titles:
#         trace_title = industry_trace_titles_dict.get("trace_title")
#         industry_id = industry_trace_titles_dict.get("industry_id")
#         if not check_contain_chinese(trace_title):
#             continue
#         x_train.append(trace_title)
#         y_train.append(industry_id)
#         if industry_id not in y_test:
#             x_test.append(trace_title)
#             y_test.append(industry_id)
#     label_list = list(set(y_train))
#     label_list.sort()
#
#     y_train_len = len(y_train)
#     random_list = random.sample(range(0, y_train_len), int(y_train_len / 4))  # 随机取1/3数据测试
#     for ra in random_list:
#         x_test.append(x_train[ra])
#         y_test.append(y_train[ra])
#
#     # 数据集准备完毕
#     score = model.train_network_model(label_list=label_list, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
#     end_time = time.time()
#     log.info("准确率:")
#     log.info(score)
#     log.info("训练时间:")
#     log.info(end_time - start_time)


def __train_industry_title_model(model):
    """
    加载、训练行业标题分类算法模型
    :return:
    """
    log.info("开始加载、训练行业标题分类算法模型")
    start_time = time.time()
    # 获取模型数据
    x_train = list()
    y_train = list()
    x_test = list()
    y_test = list()
    result_industry_trace_titles = queryBySQL_sqlal(CcsTraceTitleBasicsMapper.S_TRACE_TITLE_GROUP_BY_INDUSTRY_ID, {})
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

    label_list = list(set(y_train))
    label_list.sort()
    y_train_len = len(y_train)
    random_list = random.sample(range(0, y_train_len), int(y_train_len / 4))  # 随机取1/3数据测试
    for ra in random_list:
        x_test.append(x_train[ra])
        y_test.append(y_train[ra])

    score, matrix, report = model.train_model(label_list=label_list, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
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
    # model = MultinomialNB(alpha=0.001)  # 多项式朴素贝叶斯
    model = RandomForestClassifier()  # 随机森林算法

    myClassificationModel = MyClassificationModel(model=model, stop_list=stop_list)
    __train_industry_title_model(model=myClassificationModel)
    return myClassificationModel


# def my_industry_model_test(stop_list):
#     # log.info("_____________1k近邻算法")
#     # knc = KNeighborsClassifier()
#     # knc_model = MyClassificationModel(model=knc, stop_list=stop_list)
#     # __train_industry_title_model(model=knc_model)
#
#     log.info("_____________2决策树")
#     dtc = DecisionTreeClassifier()
#     dtc_model = MyClassificationModel(model=dtc, stop_list=stop_list)
#     __train_industry_title_model(model=dtc_model)
#     #
#     # log.info("_____________3多层感知器")
#     # mlpc = MLPClassifier()
#     # mlpc_model = MyClassificationModel(model=mlpc, stop_list=stop_list)
#     # __train_industry_title_model(model=mlpc_model)
#
#     # log.info("_____________4伯努力贝叶斯算法")
#     # bnb = BernoulliNB()
#     # bnb_model = MyClassificationModel(model=bnb, stop_list=stop_list)
#     # __train_industry_title_model(model=bnb_model)
#
#     log.info("_____________5高斯贝叶斯")
#     gnb = GaussianNB()
#     gnb_model = MyClassificationModel(model=gnb, stop_list=stop_list)
#     __train_industry_title_model(model=gnb_model)
#
#     log.info("_____________6多项式朴素贝叶斯")
#     mnb = MultinomialNB(alpha=0.001)
#     mnb_model = MyClassificationModel(model=mnb, stop_list=stop_list)
#     __train_industry_title_model(model=mnb_model)
#
#     log.info("_____________7逻辑回归算法")
#     lgr = LogisticRegression()
#     lgr_model = MyClassificationModel(model=lgr, stop_list=stop_list)
#     __train_industry_title_model(model=lgr_model)
#
#     # log.info("_____________8支持向量机算法")
#     # svc = svm.SVC()
#     # svc_model = MyClassificationModel(model=svc, stop_list=stop_list)
#     # __train_industry_title_model(model=svc_model)
#
#     log.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
#     log.info("_____________9随机森林算法")
#     rfc = RandomForestClassifier()
#     rfc_model = MyClassificationModel(model=rfc, stop_list=stop_list)
#     __train_industry_title_model(model=rfc_model)
#
#     # log.info("_____________10自增强算法")
#     # abc = AdaBoostClassifier()
#     # abc_model = MyClassificationModel(model=abc, stop_list=stop_list)
#     # __train_industry_title_model(model=abc_model)
#
#     # log.info("_____________11lightgbm算法")
#     # gbm = lightgbm.LGBMClassifier()
#     # gbm_model = MyClassificationModel(model=gbm, stop_list=stop_list)
#     # __train_industry_title_model(model=gbm_model)
#
#     # log.info("_____________12xgboost算法")
#     # xgb = xgboost.XGBClassifier()
#     # xgb_model = MyClassificationModel(model=xgb, stop_list=stop_list)
#     # __train_industry_title_model(model=xgb_model)


# def my_industry_model_test2(stop_list):
#     """
#     模型预测
#     :param stop_list:
#     :return:
#     """
#     # 1 创建神经网络
#     network = models.Sequential()
#     network_model = MyClassificationModel(model=network, stop_list=stop_list)
#     __train_network_model(network_model)
#     return network_model
