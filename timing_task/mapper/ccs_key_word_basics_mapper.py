# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/9/8

# 系统包

# 自定义包


class CcsKeyWordBasicsMapper(object):
    S_KEY_WORD_GROUP_BY_INDUSTRY_ID = "SELECT industry_id, key_word, company_num FROM `ccs_key_word_basics` WHERE industry_id IN (SELECT industry_id FROM `ccs_key_word_basics` GROUP BY industry_id HAVING COUNT(*) >= 10)"


