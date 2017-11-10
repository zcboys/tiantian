# coding=utf-8
import os, pymysql
pymysql.install_as_MySQLdb()

DEBUG = True
SECRET_KEY = os.urandom(24)

# dialect+driver://username:password@host:port/database
USERNAME = 'root'
PASSWORD = 'centos'
HOSTNAME = '192.168.48.22'
PORT = '3306'
DATABASE = 'zlktqa'

DB_URI = "mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

SQLALCHEMY_TRACK_MODIFICATIONS = False