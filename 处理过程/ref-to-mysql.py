import re
import time
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import pymysql
import pymysql.cursors

data2 = xlrd.open_workbook(r'F:\ref.xls')  # 打开xls文件
table2 = data2.sheets()[0]  # 打开第一张表
nrows = table2.nrows  # 获取表的行数

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test',
    'charset': 'utf8'
}
for i in range(1, nrows):
    cell = [1]*10
    print(i)
    for num in range(0,10):
        cell[num]=" "
        cell[num] = (str((table2.row_values(i)[num])))
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "insert into ref (title,author,cn1,cn2,time,Type,ref_title,ref_author,mag,ref_time)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (cell[0],cell[1],cell[2],cell[3],cell[4],cell[5],cell[6],cell[7],cell[8],cell[9]))

            # 获取查询结果
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()

    finally:
        connection.close();
