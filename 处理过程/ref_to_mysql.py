import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import pymysql
import pymysql.cursors
import re
import time

data = xlrd.open_workbook(r'F:\time.xls')  # 打开xls文件
table = data.sheets()[0]  # 打开第一张表
nrows = table.nrows  # 获取表的行数
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test',
    'charset': 'utf8'
}
for i in range(1,nrows):  # 循环逐行打印
    title = (str((table.row_values(i)[1])))[:6]+'%'
    _from = (str((table.row_values(i)[2])))
    time = (str((table.row_values(i)[3])))
    print(i)
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select id from cnki where title like %s and _from=%s"
            cursor.execute(sql,(title,_from))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
    if len(result)>0:
        Id = int(str(result[0])[1:-2])
        print(Id)

        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                sql = "UPDATE cnki set time=%s where id=%s"
                cursor.execute(sql,(time,Id))
                # 获取查询结果
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close();
