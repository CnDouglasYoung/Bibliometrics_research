import xlrd
import re
import time
import xlwt
import pymysql
import pymysql.cursors

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
data = xlrd.open_workbook(r'F:\crawlers\NRef2.xls')  # 打开xls文件
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
for i in range(0, nrows):  # 循环逐行打印
    print(i)
    title1 = (str((table.row_values(i)[1])))
    author1 = (str((table.row_values(i)[2])))
    title2 = (str((table.row_values(i)[3])))
    author2 = (str((table.row_values(i)[4])))
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            author1 = re.split(r',', author1)
            sql = "select id,num from ref where title=%s and author=%s"
            cursor.execute(sql, (title1, author1[0]))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
    if len(result) == 0:
        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                sql = "insert into ref (title,author,num) values (%s,%s,%s)"
                cursor.execute(sql, (title1, author1[0], 1))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close();
    else:
        num = re.split(r',', str(result[0]))[1][:-1]
        Id = re.split(r',', str(result[0]))[0][1:]
        num = int(num) + 1
        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                sql = "update ref set num=%s where id=%s"
                cursor.execute(sql, (num, Id))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close();

    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            author2 = re.split(r',', author2)
            sql = "select id,num from ref where title=%s and author=%s"
            cursor.execute(sql, (title2, author2[0]))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
    if len(result) == 0:
        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                sql = "insert into ref (title,author,num) values (%s,%s,%s)"
                cursor.execute(sql, (title2, author2[0], 1))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close();
    else:
        num = re.split(r',', str(result[0]))[1][:-1]
        Id = re.split(r',', str(result[0]))[0][1:]
        num = int(num) + 1
        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                sql = "update ref set num=%s where id=%s"
                cursor.execute(sql, (num, Id))
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close();
print("over")
