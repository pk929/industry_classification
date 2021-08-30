# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/6/30

# 系统包
import requests

# 自定义包
from common.flask_log import Log as log


class SendRequest(object):
    def __init__(self):
        # 通过在创建类的时候就创建session对象
        self.session = requests.session()
        self.timeout = 5000

    """cookie+session鉴权的请求类封装"""

    def send_session(self, url, method, headers=None, params=None, data=None, json=None, files=None):
        """
        会话请求
        :param url:
        :param method:
        :param headers:
        :param params:
        :param data:
        :param json:
        :param files:
        :return:
        """
        method = method.lower()
        res = None
        try:
            if method == "get":
                response = self.session.get(url=url, params=params, headers=headers)
                res = response.text
            elif method == "post":
                response = self.session.post(url=url, json=json, data=data, files=files, headers=headers)
                res = response.text
            log.info('url:{0}; method:{1}; response:{2}; data:{3}; json:{4}; params:{5}'.format(url, method, res, data, json,params))
        except Exception as e:
            log.error_ex("request_utils__e:" + str(e))
            raise e
        finally:
            return res

    def post_session(self, url, headers=None, data=None, json=None, files=None):
        """
        会话post请求
        :param url:
        :param headers:
        :param data:
        :param json:
        :param files:
        :return:
        """
        res = None
        try:
            response = self.session.post(url=url, json=json, data=data, files=files, headers=headers)
            res = response.text
            log.info('url:{0}; response:{1}; data:{2}; json:{3}'.format(url, res, data, json))
        except Exception as e:
            log.error_ex("request_utils__e:" + str(e))
            raise e
        finally:
            return res

    def get_session(self, url, headers=None, params=None):
        """会话get请求"""
        res = None
        try:
            response = self.session.get(url=url, params=params, headers=headers)
            res = response.text
            log.info('url:{0}; response:{1}; params:{2}'.format(url, res, params))
        except Exception as e:
            log.error_ex("request_utils__e:" + str(e))
            raise e
        finally:
            return res


def send(url, method, headers=None, params=None, data=None, json=None, files=None):
    """
    普通请求
    :param url:
    :param method:
    :param headers:
    :param params:
    :param data:
    :param json:
    :param files:
    :return:
    """
    method = method.lower()
    res = None
    try:
        if method == "get":
            response = requests.get(url=url, params=params, headers=headers)
            res = response.text
        elif method == "post":
            response = requests.post(url=url, json=json, data=data, files=files, headers=headers)
            res = response.text
        log.info('url:{0}; method:{1}; response:{2}; data:{3}; json:{4}; params:{5}'.format(url, method, res, data, json,params))
    except Exception as e:
        log.error_ex("request_utils__e:" + str(e))
        raise e
    finally:
        return res


def post(url, headers=None, data=None, json_=None, files=None):
    """
    普通post请求
    :param url:
    :param headers:
    :param data:
    :param json_:
    :param files:
    :return:
    """
    res = None
    try:
        response = requests.post(url=url, json=json_, data=data, files=files, headers=headers)
        res = response.text
        log.info('url:{0}; response:{1}; data:{2}; json:{3}'.format(url, res, data, json_))
    except Exception as e:
        log.error_ex("request_utils__e:" + str(e))
        raise e
    finally:
        return res


def get(url, headers=None, params=None):
    """
    普通get请求
    :param url:
    :param headers:
    :param params:
    :return:
    """
    res = None
    try:
        response = requests.get(url=url, params=params, headers=headers)
        res = response.text
        log.info('url:{0}; response:{1}; params:{2}'.format(url, res, params))
    except Exception as e:
        log.error_ex("request_utils__e:" + str(e))
        raise e
    finally:
        return res
