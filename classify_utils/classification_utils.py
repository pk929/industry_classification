# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/31

# 系统包
import jieba
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB
from sklearn import metrics

from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm

import pandas as pd
from keras import models
from keras import layers
from keras.utils.np_utils import to_categorical

# 自定义包


class MyClassificationModel(object):
    def __init__(self, model, stop_list):
        # alpga表示平滑参数，越小越容易造成过拟合；越大越容易欠拟合。
        # 拉普拉斯或利德斯通平滑的参数λ ，如果设置为0则表示完全没有平滑选项。但是需要注意的是，平滑相当于人为给概率加上一些噪音，因此λ \lambdaλ设置得越大，多项式朴素贝叶斯的精确性会越低（虽然影响不是非常大）。
        # self.model = MultinomialNB(alpha=0.001)
        self.model = model
        # 文本数据转换成数据值数据矩阵
        self.count = CountVectorizer(stop_words=stop_list)

    def train_network_model(self, x_train, y_train, x_test, y_test):
        """
        训练神经网络模型
        :param x_train: 训练集
        :param y_train: 标识集，需有序列表
        :param x_test: 测试集
        :param y_test: 测试标识集
        :return:
        """
        # 中文分词
        x_train_cut = self.text_jieba(x_train)
        x_test_cut = self.text_jieba(x_test)
        # 编码器处理文本标签
        le = LabelEncoder()
        y_train_le = le.fit_transform(y_train)
        y_test_le = le.fit_transform(y_test)
        # 文本数据转换成数据值数据矩阵
        self.count.fit(list(x_train_cut))
        x_train_count = self.count.transform(x_train_cut).toarray()
        x_test_count = self.count.transform(x_test_cut).toarray()

        feature_num = x_train_count.shape[1]  # 设置所希望的特征数量

        # 独热编码目标向量来创建目标矩阵
        y_train_cate = to_categorical(y_train_le)
        y_test_cate = to_categorical(y_test_le)
        # ----------------------------------------------------
        # 2 添加神经连接层
        # 第一层必须有并且一定是 [输入层], 必选
        self.model.add(layers.Dense(  # 添加带有 relu 激活函数的全连接层
            units=128,
            activation='relu',
            input_shape=(feature_num,)
        ))

        # 介于第一层和最后一层之间的称为 [隐藏层]，可选
        self.model.add(layers.Dense(  # 添加带有 relu 激活函数的全连接层
            units=128,
            activation='relu'
        ))
        self.model.add(layers.Dropout(0.8))
        # 最后一层必须有并且一定是 [输出层], 必选
        self.model.add(layers.Dense(  # 添加带有 softmax 激活函数的全连接层
            units=len(set(y_test)),
            activation='sigmoid'
        ))

        # -----------------------------------------------------
        # 3 编译神经网络
        self.model.compile(loss='categorical_crossentropy',  # 分类交叉熵损失函数
                           optimizer='rmsprop',
                           metrics=['accuracy']  # 准确率度量
                           )

        # -----------------------------------------------------
        # 4 开始训练神经网络
        history = self.model.fit(x_train_count,  # 训练集特征
                                 y_train_cate,  # 训练集标签
                                 epochs=20,  # 迭代次数
                                 batch_size=300,  # 每个批量的观测数  可做优化
                                 validation_data=(x_test_count, y_test_cate)  # 验证测试集数据
                                 )
        self.model.summary()

        # -----------------------------------------------------

        # 6 性能评估
        score = self.model.evaluate(x_test_count,
                                    y_test_cate,
                                    batch_size=32)
        return score[1]

    def train_model(self, x_train, y_train, x_test, y_test):
        """
        训练模型
        :param x_train: 训练集
        :param y_train: 标识集，需有序列表
        :param x_test: 测试集
        :param y_test: 测试标识集
        :return: 准确率,混淆矩阵,召回率
        """
        # 中文分词
        x_train_cut = self.text_jieba(x_train)
        x_test_cut = self.text_jieba(x_test)

        # 编码器处理文本标签
        le = LabelEncoder()
        y_train_le = le.fit_transform(y_train)
        y_test_le = le.fit_transform(y_test)
        # 文本数据转换成数据值数据矩阵
        self.count.fit(list(x_train_cut))
        x_train_count = self.count.transform(x_train_cut).toarray()
        x_test_count = self.count.transform(x_test_cut).toarray()

        self.model.fit(x_train_count, y_train_le)

        y_pred_model = self.model.predict(x_test_count)
        score = metrics.accuracy_score(y_test_le, y_pred_model)  # 准确率
        matrix = metrics.confusion_matrix(y_test_le, y_pred_model)  # 混淆矩阵
        report = metrics.classification_report(y_test_le, y_pred_model)  # 召回率
        # print('>>>准确率\n', score)
        # print('\n>>>混淆矩阵\n', matrix)
        # print('\n>>>召回率\n', report)
        return score, matrix, report

    def predict(self, msg):
        """
        预测分类
        :param msg:
        :return: 返回标签下标及概率
        """
        msg_cut = self.text_jieba([msg])
        msg_count = self.count.transform(msg_cut).toarray()
        result = self.model.predict(msg_count)[0]
        result_proba = self.model.predict_proba(msg_count)[0][result]
        return str(result), str(result_proba)

    def text_jieba(self, x_text):
        """
        对数据进行jieba分词
        :param x_text:
        :return:
        """
        x_word = [jieba.cut(words) for words in x_text]
        x_cut = [' '.join(word) for word in x_word]
        return x_cut
