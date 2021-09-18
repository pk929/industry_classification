# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/16

# 系统包

# 自定义包
from application import industry_title_model
from common import *
from mapper import *


def get_classify(company_id):
    """
    获取该企业的行业分类
    :param company_id:
    :return:
    """
    re = {"type": "no", "industry_id": None, "similarity": None}
    industry_title_dict = dict()
    a_dict = dict()
    b_dict = dict()
    try:
        # 查询该公司的标题数据
        result_titles = queryBySQL_sqlal(CcsTraceTitleMapper.S_CCS_TRACE_TITLE_BY_COMPANY_ID, {"company_id": company_id})

        for result_title_dict in result_titles:
            title = result_title_dict.get("title")
            result_label, result_proba = industry_title_model.predict(title)
            log.info({"industry_id": result_label, "similarity": result_proba})
            if float(result_proba) > 0.5:
                if result_label in a_dict.keys():
                    a_dict[result_label] = float(a_dict.get(result_label)) + float(result_proba)
                    b_dict[result_label] = int(b_dict.get(result_label)) + 1
                else:
                    a_dict[result_label] = float(result_proba)
                    b_dict[result_label] = 1
        log.info(a_dict)
        log.info(b_dict)
        for key in a_dict.keys():
            a_sim = a_dict.get(key)
            b_len = b_dict.get(key)
            industry_title_dict[key] = a_sim / b_len

    except Exception as e:
        log.error_ex(str(e))
    return industry_title_dict
