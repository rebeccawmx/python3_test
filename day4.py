#!/usr/bin/env python
# encoding: utf-8
# date:2018/9/13
# comment:输入某年某月某日，判断这一天是这一年的第几天？

# 第一步：输入年月日
# 第二步：调用time函数的的tm_yday显示天数
# 第三步：输出天数


import time


# 第一步：输入年月日

Date = input("请输入年月日，格式为YYYYMMDD:")

# 第二步：调用time函数的的tm_yday显示天数
days = time.strptime(Date, '%Y%m%d').tm_yday

# 第三步：输出天数
print("这一天在这一年的 {}".format(days))
