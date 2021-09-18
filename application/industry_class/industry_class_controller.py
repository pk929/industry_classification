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
from application.industry_class.industry_class_service import *
from application import industry_title_model
from application import industry_keyword_model


@industry_class.route('/', methods=['GET', 'POST'])
def index():
    return 'The Flask Server is running...'


@industry_class.route('/testKeyword', methods=['POST'])
def testKeyword():
    msg = request.values.get("msg")  # 访客说

    if str_is_None(msg):
        return return_fail("数据为空")
    result, result_proba = industry_keyword_model.predict_network(msg)
    result_dict = {"result": result, "result_proba": result_proba}

    log.info(msg)
    log.info(result_dict)
    return return_success(result_dict)


@industry_class.route('/testTitle', methods=['POST'])
def testTitle():
    msg = request.values.get("msg")
    if str_is_None(msg):
        return return_fail("数据为空")
    result, result_proba = industry_title_model.predict(msg)
    result_dict = {"result": result, "result_proba": result_proba}

    log.info(msg)
    log.info(result_dict)
    return return_success(result_dict)


@industry_class.route('/classify', methods=['POST'])
def classify():
    company_id = request.values.get("company_id")
    if str_is_None(company_id):
        return return_fail("参数错误")
    ret_data = get_classify(company_id=company_id)

    return return_success(ret_data)
