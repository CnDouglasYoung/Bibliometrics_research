import xlrd
from xlrd import open_workbook
from xlutils.copy import copy
import pymysql
import pymysql.cursors
import re
import time

data = xlrd.open_workbook(r'F:\new2.xls')  # 打开xls文件
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
for i in range(nrows):  # 循环逐行打印
    title = (str((table.row_values(i)[0])))
    author = (str((table.row_values(i)[1])))
    _type = (str((table.row_values(i)[2])))
    kw1 = (str((table.row_values(i)[3])))
    kw2 = (str((table.row_values(i)[4])))
    kw3 = (str((table.row_values(i)[5])))
    kw4 = (str((table.row_values(i)[6])))
    kw5 = (str((table.row_values(i)[7])))
    kw6 = (str((table.row_values(i)[8])))
    fund = (str((table.row_values(i)[11])))
    cn = (str((table.row_values(i)[12])))
    _from = (str((table.row_values(i)[13])))
    core = (str((table.row_values(i)[14])))
    jg=(str((table.row_values(i)[17])))
    print(title,author,_type,kw1,fund,cn,_from,core)
    authorList = re.split(r',', author)
    cn = re.split(r';', cn)

    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            if len(authorList) == 1:
                if len(cn) == 1:
                    sql = "INSERT INTO cnki (title,author1,_type,kw1,kw2,kw3,kw4,kw5,kw6,fund,cn1,_from,core,ins) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(title, authorList[0], _type, kw1, kw2, kw3, kw4, kw5, kw6, fund, cn[0], _from, core,jg))
                if len(cn) >= 2:
                    sql = "INSERT INTO cnki (title,author1,_type,kw1,kw2,kw3,kw4,kw5,kw6,fund,cn1,cn2,_from,core,ins) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(title, authorList[0], _type, kw1, kw2, kw3, kw4, kw5, kw6, fund, cn[0], cn[1],_from,core,jg))
            else:
                if len(cn) == 1:
                    sql = "INSERT INTO cnki (title,author1,author2,_type,kw1,kw2,kw3,kw4,kw5," \
                          "kw6,fund,cn1,_from,core,ins) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(title, authorList[0], authorList[1], _type, kw1, kw2, kw3, kw4, kw5, kw6, fund, cn[0],_from, core,jg))
                if len(cn) >= 2:
                    sql = "INSERT INTO cnki (title,author1,author2,_type,kw1,kw2,kw3,kw4,kw5,kw6,fund,cn1,cn2,_from,core,ins) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(sql,(title, authorList[0], authorList[1], _type, kw1, kw2, kw3, kw4, kw5, kw6, fund, cn[0],cn[1], _from, core,jg))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
    print(i)
