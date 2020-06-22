#!/usr/bin/python
# -*- coding: utf-8 -*-


# format表示格式化日期的特殊字符.如"%Y-%m-%d"
# tuple表示需要转换的时间,用元祖存储;元祖中的元素分别表示年,月,日,时,分,秒
# 函数返回字符串
#
# Python提供了time处理模块处理日期和时间,函数strftime()可以实现从时间到字符串的转换,声明如下：
# strftime(format[,tuple])   -->string
#
# format格式化日期常用标记:
# %a  英文星期的简写      %d  日期1-31     
# %A  英文星期的大写      %H  小时数00-23
# %b  英文月份的小谢      %M  分钟数01-59
# %B  英文月份的大写      %m  月份01-12 
# %c  显示本地日期时间    %x  本地当天日期    %X  本地当天时间
# %Y  年份完整数字        %j  显示从本年第一天到当天的天数
# %w  显示今天是星期几    %W  显示当天属于本年的第几周


# 字符串到时间的转换需要进行两次转换,需要使用time模块和datetime类,3个步骤:
#     1.调用函数strptime()把字符串转换为一个元祖,strptime()的声明如下:
#              strptime(string,tuple) -->struct_time:
#               string表示需要转换的字符串
#               format表示日期时间的输出格式
#               函数返回一个存放时间的元祖
#
#     2.把表示时间的元祖赋值给表示年月日的3个变量
#
#     3.把表示年月日的3个变量传递给函数datetime()进行第二次转换,datetime()函数如下:
#
#         datetime(year,month,day[,hour[,minute[,second[,microsecond[,tzinfo]]]]])
#         参数年月日不可少;返回1个datetime类型的变量；


import time

# <class 'time.struct_time'>
# time.struct_time(tm_year=2019, tm_mon=9, tm_mday=6...
print(type(time.localtime()), '\n', time.localtime())


# 时间到字符串的转换,返回当前时间,strftime把当前时间格式转换为字符串类型
# 2019-09-06 14:49:11
# <class 'str'>
print(time.strftime("%Y-%m-%d %X", time.localtime()))
print(type(time.strftime("%Y-%m-%d %X", time.localtime())))


#  str ---> time
# 字符串到时间的转换,把字符串"2008-08-08"转换为一个元祖返回
# <class 'time.struct_time'>
# time.struct_time(tm_year=2008, tm_mon=8, tm_mday=8, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=4, tm_yday=221, tm_isdst=-1)
str = "2008-08-08"
print(type(time.strptime(str,"%Y-%m-%d")), '\n', time.strptime(str,"%Y-%m-%d"))

# *********************************************************************************************


import datetime

# 调用datetime()返回时间类型
# <class 'datetime.datetime'> 2019-09-06 00:00:00
a = time.strptime("2019-09-06", "%Y-%m-%d")
y, m, d = a[0:3]
print(type(datetime.datetime(y, m, d)), datetime.datetime(y, m, d))


# ————————————————————————————————————————————————————————————————————
print(type(datetime.datetime.now()), datetime.datetime.now())
# <class 'datetime.datetime'> 2019-09-06 15:36:28.960484


dt = datetime.datetime.now()
print(type(dt.strftime("%Y-%m-%d %X")), dt.strftime("%Y-%m-%d %X"))
# <class 'str'> 2019-09-06 15:38:18

# *********************************************************************************************

# CookeBook 时间换算 笔记


from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c, c.days, c.seconds, c.seconds/3600, c.total_seconds()/3600)
# 2 days, 10:30:00 2 37800 10.5 58.5


from datetime import datetime
a = datetime(2019,9,12)         # <class 'datetime.datetime'>    2019-09-12 00:00:00
print(a + timedelta(days=10))       # 2019-09-22 00:00:00

b = datetime(2019, 12, 31)
d = b - a
print(d.days, d.total_seconds()/3600/24)       # 110 110.0

now = datetime.today()          # 2020-06-20 19:23:25.694315
print( now + timedelta(minutes=10))  # 2020-06-20 19:23:25.694315





