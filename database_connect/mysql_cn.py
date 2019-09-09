#!/usr/bin/python
# -*- coding: utf-8 -*-

import pymysql


class MysqlCn:
    def __init__(self, host, port, user, password, database=None):
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