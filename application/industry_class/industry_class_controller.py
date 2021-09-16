# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包
from flask import request

# 自定义包
from application.industry_class import industry_class
from application.result_json import *
from common.flask_log import Log as log
# from application import industry_title_model, industry_keyword_model

@industry_class.route('/', methods=['GET', 'POST'])
def index():
    return 'The Flask Server is running...'

#
@industry_class.route('/test', methods=['POST'])
def test():
    msg = request.values.get("msg")  # 访客说

    if str_is_None(msg):
        return return_fail("数据为空")

    # # 获取模型
    # result, result_proba = industry_title_model.predict(msg)
    #
    # result_dict = {"result": result, "result_proba": result_proba}
    #
    # log.info(msg)
    # log.info(result_dict)
    # return return_success(result_dict)
    return return_success({})


@industry_class.route('/keyword', methods=['POST'])
def keyword():
    msg = request.values.get("msg")
    if str_is_None(msg):
        return return_fail("数据为空")
    # result, result_proba = industry_keyword_model.predict(msg)
    # result_dict = {"result": result, "result_proba": result_proba}
    #
    # log.info(msg)
    # log.info(result_dict)
    # return return_success(result_dict)
    return return_success({})
