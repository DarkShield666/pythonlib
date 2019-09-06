#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import time,datetime

class TimeLib:

    # 给一个开始时间如： 2019-09-06 12:12:12
    def get_intdays_later_time(start_time: str, day: int):
        start_time = start_time.split(' ')[0]
        y, m, d = time.strptime(start_time, "%Y-%m-%d")[0: 3]
        end_time = datetime.datetime(y, m, d) + datetime.timedelta(days=day)
        return end_time.strftime('%Y-%m-%d %X')


    # 时间格式 2012-12-12 00:00:00
    def get_random_time(start_time: str, end_time: str):
        random_time = random.randint(time.mktime(time.strptime(start_time, "%Y-%m-%d %H:%M:%S")),
                                     time.mktime(time.strptime(end_time, "%Y-%m-%d %H:%M:%S")))
        return time.strftime("%Y-%m-%d %X", time.localtime(random_time))


if __name__ == '__main__':
    start_day = '2019-09-01 00:00:00'
    end_time = "2019-09-10 00:00:00"
    print(TimeLib.get_random_time(start_day,end_time))