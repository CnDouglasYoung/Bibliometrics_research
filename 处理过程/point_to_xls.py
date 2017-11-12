import xlrd
import re
import time
import xlwt
import pymysql
import pymysql.cursors

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test',
    'charset': 'utf8'
}
for i in range(1, 5716):  # 循环逐行打印
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select * from ref where id=%s"
            cursor.execute(sql, (i))
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
    ws.write(i,0,result[0][1])
    ws.write(i, 1, result[0][2])
    if result[0][3]>1:
        ws.write(i, 2, result[0][1])
    ws.write(i, 3, result[0][3])
    print(i)
print("over")
wb.save('Ref-P.xls')
