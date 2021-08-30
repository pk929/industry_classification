# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/26

# 系统包
import pymysql

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Server
"""db需要在其他模块声明前声明"""
pymysql.install_as_MySQLdb()
db = SQLAlchemy()

# 自定义包
from config.ini_config import Config
from application.flask_config import FlaskConfig
from common.flask_log import Log
from config.flask_scheduler_config import FlaskSchedulerConfig


baseConfig = Config()
flask_config = FlaskConfig()
Log(baseConfig)
flaskSchedulerConfig = FlaskSchedulerConfig()

def init_app():
    """
    初始化app
    :return:
    """
    app = Flask(__name__)
    app.config.from_object(flask_config)
    db.init_app(app)
    app.config.from_object(flaskSchedulerConfig)


    from application.industry_class import industry_class
    app.register_blueprint(industry_class, url_prefix='/industry_class')

    return app


def init_runserver():
    return Server(host=baseConfig.get_value('flask-runserver', 'host'),
                  port=baseConfig.get_value('flask-runserver', 'port'),
                  use_debugger=Config.strToBool(baseConfig.get_value('flask-runserver', 'use_debugger')),
                  use_reloader=Config.strToBool(baseConfig.get_value('flask-runserver', 'use_reloader')),
                  threaded=Config.strToBool(baseConfig.get_value('flask-runserver', 'threaded')),
                  passthrough_errors=Config.strToBool(baseConfig.get_value('flask-runserver', 'passthrough_errors'))
                  )