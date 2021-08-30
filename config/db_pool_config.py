# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/30

# 系统包
import sqlalchemy

# 自定义包
from config.ini_config import Config
from common.flask_log import Log as log

_user = Config.get_value('flask-sqlalchemy', 'user')
_password = Config.get_value('flask-sqlalchemy', 'password')
_host = Config.get_value('flask-sqlalchemy', 'host')
_port = Config.get_value('flask-sqlalchemy', 'port')
_database = Config.get_value('flask-sqlalchemy', 'database')
_charset = Config.get_value('flask-sqlalchemy', 'charset')


# SQLAlchemy连接池
class MySQLAlchemyPool(object):
    def __init__(self):
        self.engine = sqlalchemy.create_engine(
            "mysql+pymysql://%s:%s@%s:%s/%s?charset=%s" % (_user, _password, _host, _port, _database, _charset),
            pool_size=20,  # 连接池大小
            max_overflow=200,  # 当连接池里的连接数已达到，pool_size时，且都被使用时。又要求从连接池里获取连接时，max_overflow就是允许再新建的连接数。
            pool_recycle=3600,  # 连接自动回收时间（秒）
            echo=False
        )

    def getSQLAlchemyConn(self):
        """
        获取连接
        :return:
        """
        conn = self.engine.connect()
        return conn

    def closeSQLAlchemyConn(self, conn=None):
        """
        关闭数据库连接
        :param conn:
        :return:
        """
        try:
            conn.close()
        except Exception as e:
            # raise e
            log.error_ex("MySQLAlchemyPool_closeSQLAlchemyConn_e:" + str(e))


mySQLAlchemyPool = MySQLAlchemyPool()
