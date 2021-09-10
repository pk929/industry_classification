# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包
import json

# 自定义包
from common import *


CODE_SUCCES = 200
CODE_FAIL = 900


def return_success(data):
    return_dict = {'code': CODE_SUCCES, 'info': '', 'data': data}
    vo = json.dumps(return_dict, ensure_ascii=False)
    log.info('RESULT_return_success:{}'.format(vo))
    return vo


def return_fail(errorMsg):
    return_dict = {'code': CODE_FAIL, 'info': errorMsg, 'data': ''}
    vo = json.dumps(return_dict, ensure_ascii=False)
    log.info('RESULT_return_fail:{}'.format(vo))
    return vo


def return_fail_code(code, errorMsg):
    return_dict = {'code': code, 'info': errorMsg, 'data': ''}
    vo = json.dumps(return_dict, ensure_ascii=False)
    log.info('RESULT_return_fail_code:{}'.format(vo))
    return vo


def jsonResultVo(code, message, data):
    return_dict = {'code': code, 'info': message, 'data': data}
    vo = json.dumps(return_dict, ensure_ascii=False)
    log.info('RESULT_jsonResultVo:{}'.format(vo))
    return vo
