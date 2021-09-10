# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包

# 自定义包

from config.ini_config import Config

GET_HISTORY_MSG = Config.get_value('http-info', 'get_history_msg')
GET_TALK_INFO = Config.get_value('http-info', 'get_talk_info')


print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")