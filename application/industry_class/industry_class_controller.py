# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包

# 自定义包
from application.industry_class import industry_class
from application.result_json import *
from application import *
from common.flask_log import Log as log


@industry_class.route('/', methods=['GET', 'POST'])
def index():
    return 'The Flask Server is running...'


@industry_class.route('/test', methods=['GET', 'POST'])
def test():
    print("1111111111")

    log.info("我来啦")
    return return_success("哈哈哈哈")

