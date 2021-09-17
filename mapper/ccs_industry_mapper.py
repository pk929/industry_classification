# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/1

# 系统包

# 自定义包


class CcsIndustryMapper(object):
    S_SECOND_INDUSTRY_ID = "SELECT id FROM `ccs_industry` WHERE industry_level = 2 AND industry_status = 1"

