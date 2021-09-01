# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/27

# 系统包
from apscheduler.jobstores.memory import MemoryJobStore

# 自定义包
from timing_task.land_page_task import *
from timing_task.industry_quality_inspection_task import *

#
class FlaskSchedulerConfig(object):
    JOBS = [
        # {
        #     'id': 'get_title_kw_from_land_page',  # 任务标识，必须唯一
        #     'func': get_title_kw_from_land_page,
        #     'args': None,
        #     'trigger': 'cron',
        #     'year': '*',
        #     'month': '*',
        #     'day': '*',
        #     'hour': '*',
        #     'minute': 54,
        #     'second': 0
        # },
        {
            'id': 'industry_quality_inspection_task',  # 任务标识，必须唯一
            'func': industry_quality_inspection_task,
            'args': None,
            'trigger': 'cron',
            'year': '*',
            'month': 9,
            'day': 1,
            'hour': 17,
            'minute': 55,
            'second': 0
        }
    ]

    # 存储定时工作（默认是存储在内存中）
    SCHEDULER_JOBSTORES = {
        'default': MemoryJobStore()
    }
    # 设置定时工作的执行器（默认是最大执行数量为10的线程池）
    SCHEDULER_EXECUTORS = {
        'default': {'type': 'threadpool', 'max_workers': 20}
    }
    # 设置时区
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'
    SCHEDULER_JOB_DEFAULTS = {
        'coalesce': False,
        'max_instances': 3
    }
    # 开启API性能，这样才能够用api的形式去查看和批改定时工作
    SCHEDULER_API_ENABLED = True
    # API前缀（默认是/scheduler）
    SCHEDULER_API_PREFIX = '/schedule'

