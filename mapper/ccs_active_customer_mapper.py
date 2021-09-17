# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/30

# 系统包

# 自定义包


class CcsActiveCustomerMapper(object):
    S_COMID_BY_NOT_QUALITY = "SELECT company_id FROM `ccs_active_customer` WHERE quality_test_state IN (0,2) AND delete_at IS NULL"

