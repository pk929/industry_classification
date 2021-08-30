# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/30

# 系统包
import sqlalchemy
from sqlalchemy import DateTime as sqlalchemy_DateTime, Date as sqlalchemy_Date, Time as sqlalchemy_Time, \
    text as sqlalchemy_text
import time
from datetime import datetime as cdatetime  # 有时候会返回datatime类型
from sqlalchemy import DateTime, Numeric, Date, Time  # 有时又是DateTime
from datetime import date as cdate, time as ctime

# 自定义包
from config.db_pool_config import mySQLAlchemyPool
from common.flask_log import Log as log


def executeBySQL_sqlal(sql=None, params=None):
    """
    执行
    :param sql:
    :param params:
    :return:
    """
    data = 0
    conn = None
    try:
        conn = mySQLAlchemyPool.getSQLAlchemyConn()
        statement = sqlalchemy_text(sql)
        resultProxy = conn.execute(statement, params)
        data = resultProxy.rowcount
    except Exception as e:
        raise e
    finally:
        mySQLAlchemyPool.closeSQLAlchemyConn(conn)
        return data


# 事务执行
def get_begin_conn_sqlal():
    """
    开始事务
    :return:
    """
    conn = mySQLAlchemyPool.getSQLAlchemyConn()
    trans = conn.begin()
    return conn, trans


def commit_begin_conn_sqlal(conn=None, trans=None):
    """
    提交事务
    :param conn:
    :param trans:
    :return:
    """
    try:
        trans.commit()
    except Exception as e:
        trans.rollback()
        log.error_ex("db_utils_commit_begin_conn_sqlal_e:" + str(e))
    finally:
        conn.close()


def rollback_begin_conn_sqlal(conn=None, trans=None):
    """
    回滚事务
    :param conn:
    :param trans:
    :return:
    """
    try:
        trans.rollback()
        conn.close()
    except Exception as e:
        log.error_ex("db_utils_rollback_begin_conn_sqlal_e:" + str(e))


def execute_begin_conn_sqlal(conn=None, sql=None, params=None):
    """
    执行带有事务的数据操作
    :param conn:
    :param sql:
    :param params:
    :return:
    """
    flag = False
    try:
        statement = sqlalchemy_text(sql)
        conn.execute(statement, params)
        flag = True
    except Exception as e:
        log.error_ex("db_utils_execute_begin_conn_sqlal_e" + str(e))
    finally:
        return flag


# 普通查询
def queryBySQL_sqlal(sql=None, params=None):
    """
    普通查询
    :param sql: sql
    :param params: 参数{}
    :return:
    """
    data = []
    conn = None
    try:
        conn = mySQLAlchemyPool.getSQLAlchemyConn()
        statement = sqlalchemy_text(sql)
        db_result = conn.execute(statement, params)
        data = __dbResultToDict(list(db_result))

    except Exception as e:
        log.error_ex("db_utils_queryBySQL_sqlal_e:" + str(e))
        raise e
    finally:
        mySQLAlchemyPool.closeSQLAlchemyConn(conn)
        return data


def __dbResultToDict(result=None):
    res = [dict(zip(r.keys(), r)) for r in result]
    for r in res:
        __find_datetime(r)
    return res


def __find_datetime(value):
    for v in value:
        if isinstance(value[v], cdatetime):
            value[v] = __convert_datetime(value[v])


def __convert_datetime(value):
    if value:
        if isinstance(value, (cdatetime, sqlalchemy_DateTime)):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(value, (cdate, sqlalchemy_Date)):
            return value.strftime("%Y-%m-%d")
        elif isinstance(value, (sqlalchemy_Time, time)):
            return value.strftime("%H:%M:%S")
    else:
        return value
