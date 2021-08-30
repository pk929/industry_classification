# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包
import time
import json

# 自定义包
from timing_task.task_mapper import *
from common import *
from timing_task import *


def get_title_kw_from_land_page():
    """
    定时任务：处理着陆页
    :return:
    """
    log.info("........开始分析着陆页")

    result_company_ids = queryBySQL_sqlal(S_COMID_BY_NOT_QUALITY, {})
    for company_id_dict in result_company_ids:
        company_id = company_id_dict.get("company_id")
        log.info(company_id)
        get_talk_info_send = post(GET_TALK_INFO, data={"company_id":company_id})
        get_talk_info_response = json.loads(get_talk_info_send)
        # print(get_talk_info_response)
        code = get_talk_info_response.get("code")
        msg = get_talk_info_response.get("msg")
        if "200" == str(code):
            data_list = get_talk_info_response.get("data")
            for date_dict in data_list:
                land_page = date_dict.get("land_page")
                if not str_is_None(land_page):
                    title, description, keywords = url_analysis(land_page)
                    log.info(title)
                    log.info(description)
                    log.info(keywords)

        else:
            ''

