#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import re
import pymysql

# 打开数据库连接
db = pymysql.connect('127.0.0.1', 'root', 'root', 'sentence', charset='utf8')
# 使用cursor()方法获取操作游标
cursor = db.cursor()

#死循环到天长地久
while(True):
    response = requests.get('https://www.nihaowua.com/')
    # 正则匹配文本
    match = re.findall(r'<p><!--markdown-->([\s\S]*?)</p>', response.text)
    if match:
        sql = "INSERT INTO `sexy` (`content`) VALUES ('%s')" % (match[0])
        try:
           # 执行sql语句
           cursor.execute(sql)
           # 提交到数据库执行
           db.commit()
        except:
           # 如果发生错误则回滚
           db.rollback()
        # 输出sql语句到控制台
        print(sql)
    else:
        # 输出html代码到控制台
        print(response.text)

#db.close()