#!/usr/bin/python
# -*- coding: utf-8 -*-


# test Hbase

from database.hbase_cn import HbaseCn
c = HbaseCn('192.168.1.1', 9090)


# print(c.query_data("dadfsfd", "2oc0000001687211", "d:j"))
# print(c.query_data("dasdsdfg", "7oc000003424603", "d:j"))
# print(c.query_data("daaqwbint", "f201909d7f53151d568b070eb025417", "d:j"))
c.insert_or_update_data("dadfgdfnt","123321","d:j","wocaonima")
print(c.query_data("dadfgdfnt", "123321", "d:j"))

# ————————————————————————————————————————————————————————————————————————————————————


# from database_connect.mysql_cn import MysqlCn
#
# host='173'
# port=9301
# user='root'
# password="123456"
# database="ds"
# m = MysqlCn(host=host,port=port,user=user,password=password,database=database)
# list = [
#     'lsent',
# ]
#
# m.truncate_tables(list)
# m.update()
# m.close()

# ————————————————————————————————————————————————————————————————————————————————————

# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def index():
#     return "index_page"
#
# @app.route('/hello')
# def hello_world():
#     return "hello,world"