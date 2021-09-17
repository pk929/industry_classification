# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/9

# 系统包
import random

# 自定义包
from common import *
from classify_utils.classification_utils import *
from mapper import *

def __train_keyword_network_model(model):
    """
    神经网络模型
    :param model:
    :return:
    """
    log.info("开始加载、训练行业标题分类神经网络算法模型")
    start_time = time.time()
    # 获取模型数据
    x_train = list()
    y_train = list()
    x_test = list()
    y_test = list()
    result_industry_trace_titles = queryBySQL_sqlal(CcsKeyWordBasicsMapper.S_KEY_WORD_GROUP_BY_INDUSTRY_ID, {})
    for industry_keywords_dict in result_industry_trace_titles:
        industry_id = industry_keywords_dict.get("industry_id")
        key_word = industry_keywords_dict.get("key_word")
        company_num = industry_keywords_dict.get("company_num")
        if not check_contain_chinese(key_word):
            continue
        x_train.append(key_word)
        y_train.append(industry_id)
        if industry_id not in y_test:
            x_test.append(key_word)
            y_test.append(industry_id)
    label_list = list(set(y_train))
    label_list.sort()
    y_train_len = len(y_train)
    random_list = random.sample(range(0, y_train_len), int(y_train_len / 4))  # 随机取1/3数据测试
    for ra in random_list:
        x_test.append(x_train[ra])
        y_test.append(y_train[ra])

    # 数据集准备完毕
    score = model.train_network_model(label_list=label_list, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
    end_time = time.time()
    log.info("准确率:")
    log.info(score)
    log.info("训练时间:")
    log.info(end_time - start_time)

def __train_industry_keyword_model(model):
    """
    加载、训练行业百度搜搜关键词分类算法模型
    :param model:
    :return:
    """
    log.info("开始加载、训练行业标题分类算法模型")
    start_time = time.time()
    log.info("keyword_1:" + str(time.time()))
    # 获取模型数据
    x_train = list()
    y_train = list()
    x_test = list()
    y_test = list()
    result_industry_keywords = queryBySQL_sqlal(CcsKeyWordBasicsMapper.S_KEY_WORD_GROUP_BY_INDUSTRY_ID, {})
    log.info("keyword_2:" + str(time.time()))
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

    log.info("keyword_3:" + str(time.time()))

    # 标签列表
    label_list = list(set(y_train))
    label_list.sort()
    y_train_len = len(y_train)
    random_list = random.sample(range(0, y_train_len), int(y_train_len / 4))  # 随机取1/3数据测试
    for ra in random_list:
        x_test.append(x_train[ra])
        y_test.append(y_train[ra])

    log.info("keyword_4:" + str(time.time()))
    score, matrix, report = model.train_model(label_list=label_list, x_train=x_train, y_train=y_train, x_test=x_test, y_test=y_test)
    log.info("keyword_5:" + str(time.time()))

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
    model = MultinomialNB(alpha=0.001)
    myClassificationModel = MyClassificationModel(model=model, stop_list=stop_list)
    __train_industry_keyword_model(model=myClassificationModel)
    return myClassificationModel

def my_keyword_model_test(stop_list):
    """

    :param stop_list:
    :return:
    """
    # log.info("_____________1-k近邻算法")
    # knc = KNeighborsClassifier()
    # knc_model = MyClassificationModel(model=knc, stop_list=stop_list)
    # __train_industry_keyword_model(model=knc_model)
    #
    # log.info("_____________2决策树")
    # dtc = DecisionTreeClassifier()
    # dtc_model = MyClassificationModel(model=dtc, stop_list=stop_list)
    # __train_industry_keyword_model(model=dtc_model)
    #
    # log.info("_____________3多层感知器")
    # mlpc = MLPClassifier()
    # mlpc_model = MyClassificationModel(model=mlpc, stop_list=stop_list)
    # __train_industry_keyword_model(model=mlpc_model)
    #
    # log.info("_____________4伯努力贝叶斯算法")
    # bnb = BernoulliNB()
    # bnb_model = MyClassificationModel(model=bnb, stop_list=stop_list)
    # __train_industry_keyword_model(model=bnb_model)
    #
    # log.info("_____________5高斯贝叶斯")
    # gnb = GaussianNB()
    # gnb_model = MyClassificationModel(model=gnb, stop_list=stop_list)
    # __train_industry_keyword_model(model=gnb_model)
    #
    # log.info("_____________6多项式朴素贝叶斯")
    # mnb = MultinomialNB(alpha=0.001)
    # mnb_model = MyClassificationModel(model=mnb, stop_list=stop_list)
    # __train_industry_keyword_model(model=mnb_model)

    log.info("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    log.info("_____________9随机森林算法")
    rfc = RandomForestClassifier()
    rfc_model = MyClassificationModel(model=rfc, stop_list=stop_list)
    __train_industry_keyword_model(model=rfc_model)

    log.info("_____________7逻辑回归算法")
    lgr = LogisticRegression()
    lgr_model = MyClassificationModel(model=lgr, stop_list=stop_list)
    __train_industry_keyword_model(model=lgr_model)

    # log.info("_____________8支持向量机算法")
    # svc = svm.SVC()
    # svc_model = MyClassificationModel(model=svc, stop_list=stop_list)
    # __train_industry_keyword_model(model=svc_model)



    log.info("_____________10自增强算法")
    abc = AdaBoostClassifier()
    abc_model = MyClassificationModel(model=abc, stop_list=stop_list)
    __train_industry_keyword_model(model=abc_model)


def my_keyword_model_test2(stop_list):
    """
    模型预测
    :param stop_list:
    :return:
    """
    # 1 创建神经网络
    network = models.Sequential()
    network_model = MyClassificationModel(model=network, stop_list=stop_list)
    __train_keyword_network_model(network_model)


