# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/30

# 系统包

# 自定义包


class CcsTraceTitleMapper(object):
    S_COUNT_BY_COMID = "SELECT count(id) as `count` FROM `ccs_trace_title` where company_id = :company_id"
    S_COUNT_BY_COMID_AND_TRACE = "SELECT COUNT(*) as `count` FROM `ccs_trace_title` WHERE company_id = :company_id AND trace LIKE CONCAT('%', :trace, '%')"
    S_CCS_TRACE_TITLE_BY_COMPANY_ID = "SELECT title FROM `ccs_trace_title` WHERE company_id = :company_id"

    # I_CCS_TRACE_TITLE = "INSERT INTO `ccs_trace_title` (`id`, `trace`, `title`, `description`, `keywords`, `company_id`, `update_time`) VALUES (NULL, :trace, :title, :description, :keywords, :company_id, NOW())"

    I_CCS_TRACE_TITLE = "INSERT INTO `ccs_trace_title` (`id`, `trace`, `title`, `company_id`) VALUES (NULL, :trace, :title, :company_id)"


