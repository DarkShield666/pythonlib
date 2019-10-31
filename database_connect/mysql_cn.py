#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql


class MysqlCn:
    def __init__(self, host: str, port: int, user: str, password: str, database=None):
        self.connection = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )
        self.cur = self.connection.cursor()

    def close(self):
        self.connection.close()

    def truncate_tables(self, tablename: list):
        for i in tablename:
            sql = "truncate %s" % i
            self.cur.execute(sql)
        self.connection.commit()

    # 删除表中数据，目前仅支持kwargs仅为一个k,v 格式
    def delete_data(self, tablename: list, **kwargs):
        for i in tablename:
            for k in kwargs:
                sql = "delete from %s where %s = \'%s\'" % (i, k, kwargs[k])
                print(sql)
                self.cur.execute(sql)
        self.connection.commit()

    def query_data(self, tablename):
        sql = "select * from rc_user"
        self.cur.execute(sql)
        for i in self.cur.fetchall():
            print(i)