#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import time
import datetime


class TimeLib:

    # 给一个开始时间如： 2019-09-06 12:12:12
    @staticmethod
    def get_days_later_time(start_time: str, day: int):
        start_time = start_time.split(' ')[0]
        y, m, d = time.strptime(start_time, "%Y-%m-%d")[0: 3]
        end_time = datetime.datetime(y, m, d) - datetime.timedelta(days=day)    # 可以加或者减
        return end_time.strftime('%Y-%m-%d %X')

    # 时间格式 2012-12-12 00:00:00 or 2012-12-12
    @staticmethod
    def get_random_time(start_time: str, end_time: str):
        random_time = random.randint(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S")),
                                     time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S")))
        return time.strftime("%Y-%m-%d %X", time.localtime(random_time))

    # 计算两个日期的时间差 2012-12-12 00:00:00 or 2012-12-12
    @staticmethod
    def get_d_values(start_time: str, end_time: str):
        y1, m1, d1 = time.strptime(start_time.split(' ')[0],"%Y-%m-%d")[0: 3]
        y2, m2, d2 = time.strptime(end_time.split(' ')[0],"%Y-%m-%d")[0: 3]
        return (datetime.datetime(y2, m2, d2) - (datetime.datetime(y1, m1, d1))).days
        # return (datetime.datetime(y2, m2, d2) - (datetime.datetime(y1, m1, d1))).hour

    @staticmethod
    def get_h_values(start_time, end_time):
        # print(round((time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S")) - time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S"))/3600),4))
        hour = ((time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S")) - time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S")))/3600)
        print("%.3f" % hour)
        print(round(hour, 3))


if __name__ == '__main__':
    start = '2020-06-17 12:12:12'
    end = '2020-06-17 13:42:55'
    # print(TimeLib.get_days_later_time(a, 5))

    TimeLib.get_h_values(start,end)