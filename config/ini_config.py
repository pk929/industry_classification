# -*- ecoding: utf-8 -*-
# @Function: <读取配置信息>
# @Author: pkuokuo
# @Time: 2021/8/26

# 系统包
import configparser
import os

# 自定义包


basePath = os.path.abspath(os.path.dirname(__file__))


class Config:
    cf = None

    def __new__(cls, *args, **kwargs):
        if not cls.cf:
            try:
                if cls.cf is None:
                    __CONFIG_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
                    __CONFIG_FILE_NAME = '../config.ini'
                    cls.cf = configparser.RawConfigParser()
                    cls.cf.read(os.path.join(__CONFIG_FILE_PATH, __CONFIG_FILE_NAME), encoding='utf-8')
                    print(
                        '读入config.ini配置：\n配置文件路径:{}\n配置文件版本:{}'.format(
                            os.path.join(__CONFIG_FILE_PATH, __CONFIG_FILE_NAME),
                            cls.cf.get('version', 'name')))
            except Exception as e:
                print("载入配置文件失败: " + os.path.join(__CONFIG_FILE_PATH, __CONFIG_FILE_NAME))
                print(e)
        return cls

    @staticmethod
    def get_value(section, option):
        try:
            value = Config.cf.get(section, option)
            return value
        except Exception as e:
            print("配置文件中没有该配置内容: section[" + section + "] option: " + option)
            raise e

    @staticmethod
    def strToBool(txt):
        if txt == 'True':
            return True
        elif txt == 'False':
            return False
        elif txt == 'true':
            return True
        elif txt == 'false':
            return False
        elif txt == '0':
            return False
        elif txt == '1':
            return True
        else:
            return None
