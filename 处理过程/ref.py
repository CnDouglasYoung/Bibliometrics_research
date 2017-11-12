import re
import time
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import pymysql
import pymysql.cursors

data = xlrd.open_workbook(r'F:\ref.xls')  # 打开xls文件
table = data.sheets()[0]  # 打开第一张表
i = table.nrows

rb = open_workbook('f:\\ref.xls')
wb = copy(rb)
# 通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)

data2 = xlrd.open_workbook(r'F:\crawlers\Nref.xls')  # 打开xls文件
table2 = data2.sheets()[0]  # 打开第一张表
nrows = table2.nrows  # 获取表的行数
print(nrows)
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test',
    'charset': 'utf8'
}
for i in range(1, nrows):  # 循环逐行打印
    print(i)
    cell = [1] * 7
    for num in range(0, 7):
        cell[num] = (str((table2.row_values(i)[num])))
    ws.write(i, 5, cell[0])
    ws.write(i, 6, cell[3])
    if cell[4] != "":
        author = re.split(r',', cell[4])[0]
    else:
        author = ""
    ws.write(i, 7, author)
    ws.write(i, 8, cell[5])
    ws.write(i, 9, cell[6])
    title = cell[1]
    if cell[2] != "":
        author = re.split(r',', cell[2])[0]
    else:
        author = ""
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select cn1,cn2,time from cnki where title like %s and author1=%s"
            cursor.execute(sql, (title, author))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
    if len(result) == 1:
        ws.write(i, 0, title)
        ws.write(i, 1, author)
        ws.write(i, 2, result[0][0])
        ws.write(i, 3, result[0][1])
        ws.write(i, 4, result[0][2])
    else:
        print('Error')
        print('title:%s ,author:%s' % (title, author))
    i = i+1
wb.save('f:\\ref.xls')
