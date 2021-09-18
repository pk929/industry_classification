# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包
import json

# 自定义包
from common import *
from timing_task import *
from mapper import *


def get_title_kw_from_land_page():
    """
    定时任务：处理着陆页
    :return:
    """
    log.info("........开始分析着陆页")
    try:
        result_company_ids = queryBySQL_sqlal(CcsActiveCustomerMapper.S_COMID_BY_NOT_QUALITY, {})
        for company_id_dict in result_company_ids:
            company_id = company_id_dict.get("company_id")
            # log.info(company_id)
            # 判断该comID是否已存在
            count1_list = queryBySQL_sqlal(CcsTraceTitleMapper.S_COUNT_BY_COMID, {"company_id":company_id})
            count1 = count1_list[0].get("count")

            if int(count1) > 0:
                continue

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
                        print(land_page)
                        domain_name = str(land_page).split('/')[2]

                        # 判断该着陆页域名是否已经存在
                        count2_list = queryBySQL_sqlal(CcsTraceTitleMapper.S_COUNT_BY_COMID_AND_TRACE,
                                                       {"company_id": company_id, "trace": domain_name})
                        count2 = count2_list[0].get("count")
                        if int(count2) > 0:
                            continue

                        title, description, keywords = url_analysis(land_page)
                        # log.info(title)
                        # log.info(description)
                        # log.info(keywords)

                        # 插入数据表
                        param_dict = {"trace":land_page, "title":title, "description":description, "keywords":keywords, "company_id":company_id}
                        l1 = executeBySQL_sqlal(CcsTraceTitleMapper.I_CCS_TRACE_TITLE, param_dict)
    except Exception as e:
        log.error_ex("get_title_kw_from_land_page_e:" + str(e))

