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
    industry_title_list = list()
    a_dict = dict()
    b_dict = dict()
    try:
        # 查询该公司的标题数据
        result_titles = queryBySQL_sqlal(CcsTraceTitleMapper.S_CCS_TRACE_TITLE_BY_COMPANY_ID, {"company_id": company_id})
        industry_title_len = len(result_titles)

        for result_title_dict in result_titles:
            title = result_title_dict.get("title")
            result_label, result_proba = industry_title_model.predict(title)
            print({"industry_id": result_label, "similarity": result_proba})
            if float(result_proba) > 0.5:
                if result_label in a_dict.keys():
                    a_dict[result_label] = float(a_dict.get(result_label)) + float(result_proba)
                    b_dict[result_label] = int(b_dict.get(result_label)) + 1
                else:
                    a_dict[result_label] = float(result_proba)
                    b_dict[result_label] = 1
        print(a_dict)
        print(b_dict)
    except Exception as e:
        log.error_ex(str(e))
    return a_dict
