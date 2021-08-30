# -*- ecoding: utf-8 -*-
# @Function: <主启动类>
# @Author: pkuokuo
# @Time: 2021/8/26

# 系统包
from flask import redirect, url_for
from flask_script import Manager
# from flask_migrate import Migrate, MigrateCommand
from flask_apscheduler import APScheduler

# 自定义包
from application import init_app, init_runserver, db

app = init_app()


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('industry_class.index'))


manager = Manager(app)
# Migrate(app, db)
# manager.add_command('db', MigrateCommand)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

manager.add_command('runserver', init_runserver())

if __name__ == '__main__':
    manager.run()

