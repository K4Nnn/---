import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kvn&&tj-md5-sry'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://YOUR_USERNAME:YOUR_PASSWORD@YOUR_IP_ADDRESS/YOUR_DB_NAME'  # 这里替换为您的 MySQL 数据库连接信息
    SQLALCHEMY_TRACK_MODIFICATIONS = False
