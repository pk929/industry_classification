# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/9

# 系统包

# 自定义包
from timing_task.mapper import *
from common import *


def load_industry_title_data():
    """
    加载数量较少的行业标题数据
    :return:
    """
    result_industry_trace_titles = queryBySQL_sqlal(CcsTraceTitleBasicsMapper.S_TRACE_TITLE_GROUP_BY_INDUSTRY_ID_LESS, {})
