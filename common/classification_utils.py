# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/31

# 系统包
import jieba
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

# 自定义包


class MyClass(object):
    def __init__(self, stop_list):
        # alpga表示平滑参数，越小越容易造成过拟合；越大越容易欠拟合。
        # 拉普拉斯或利德斯通平滑的参数λ ，如果设置为0则表示完全没有平滑选项。但是需要注意的是，平滑相当于人为给概率加上一些噪音，因此λ \lambdaλ设置得越大，多项式朴素贝叶斯的精确性会越低（虽然影响不是非常大）。
        self.model = MultinomialNB(alpha=0.001)
        # 文本数据转换成数据值数据矩阵
        self.count = CountVectorizer(stop_words=stop_list)

    def train_model(self, x_train, y_train, x_test, y_test):
        """
        训练模型
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

        self.model.fit(x_train_count, y_train_le)

        y_pred_model = self.model.predict(x_test_count)
        score = metrics.accuracy_score(y_test_le, y_pred_model)  # 准确率
        matrix = metrics.confusion_matrix(y_test_le, y_pred_model)  # 混淆矩阵
        report = metrics.classification_report(y_test_le, y_pred_model)  # 召回率
        print('>>>准确率\n', score)
        print('\n>>>混淆矩阵\n', matrix)
        print('\n>>>召回率\n', report)

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
        return result, result_proba

    def text_jieba(self, x_text):
        """
        对数据进行jieba分词
        :param x_text:
        :return:
        """
        x_word = [jieba.cut(words) for words in x_text]
        x_cut = [' '.join(word) for word in x_word]
        return x_cut
