# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/1

# 系统包

# 自定义包


class CcsTraceTitleBasicsMapper(object):
    S_TRACE_TITLE_BY_INDUSTRY_ID = "SELECT trace_title FROM `ccs_trace_title_basics` WHERE industry_id = :industry_id"

