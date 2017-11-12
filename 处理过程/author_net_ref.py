import pymysql
import pymysql.cursors
import time
import re

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test',
    'charset': 'utf8'
}
for i in range(900):
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # ff 执行sql语句，进行查询
            sql = "select author,ref_author,time,ref_time,Type from ref where id=%s"
            cursor.execute(sql, (i))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

    if len(result) == 0:
        continue  # 如果没查到，跳过
    if result[0][1] == None or result[0][1] == '':
        continue  # 如果是单一作者，跳过

    author1 = result[0][0]
    author2 = result[0][1]
    author2 = re.sub(r'(著|编|主编|等著|等编)', '', author2)
    time1 = result[0][2]
    time2 = result[0][3]
    Type = result[0][4]
    print(author1, author2)
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select id,author1,author2,num from author_net where (author1=%s and author2=%s) or (author1=%s and author2=%s)"
            cursor.execute(sql, (result[0][0], result[0][1], result[0][1], result[0][0]))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            if len(result) > 0:
                print(result[0])
                if Type == '[J]' or Type == '[D]':
                    if int(time1) > int(time2):
                        num = float(result[0][3]) + 0.1
                    else:
                        num = float(result[0][3]) + 0.5
                else:
                    num = float(result[0][3]) + 0.25
                sql = "update author_net set num=%s where id=%s"
                cursor.execute(sql, (num, result[0][0]))
            else:
                if Type == '[J]' or Type == '[D]':
                    if int(time1) > int(time2):
                        num = 0.1
                    else:
                        num = 0.5
                else:
                    num = 0.25
                sql = "insert into author_net (author1,author2,num) values (%s,%s,%s)"
                cursor.execute(sql, (author1, author2, num))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
