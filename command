# 进入项目目录
cd /opt/industry_classification

# 生成虚拟环境
python36 -m venv /opt/industry_classification/venv

# 激活虚拟环境
source /opt/industry_classification/venv/bin/activate

# 退出虚拟环境
deactivate

————激活以后——————
# 获取项目所有依赖类包
pip freeze > requirements.txt

# 安装包
pip3 install -r requirements.txt

# 升级安装
pip3 install --upgrade -r requirements.txt

# 设置虚拟环境默认编码
export LC_ALL="en_US.utf8"

# 在虚拟环境中启动服务
nohup python36 industry_classification_main.py runserver >/dev/null 2>&1 &
nohup python36 industry_classification_main.py runserver >> /var/log/53kf/industry_classification/industry_classification.log &

python36 industry_classification_main.py runserver

#查看进程
ps -ef|grep industry_classification_main



