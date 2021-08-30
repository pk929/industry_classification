# -*- ecoding: utf-8 -*-
# @Function: <>
# @Author: pkuokuo
# @Time: 2021/8/26

# 系统包
from flask import Blueprint

# 自定义包


industry_class = Blueprint('industry_class', __name__)

from application.industry_class import industry_class_controller
