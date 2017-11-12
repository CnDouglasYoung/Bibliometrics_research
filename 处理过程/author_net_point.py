import pymysql
import pymysql.cursors
import time

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'test',
    'charset': 'utf8'
}
for i in range(1040):
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # ff 执行sql语句，进行查询
            sql = "select author1,author2,num from author_net where id=%s"
            cursor.execute(sql, (i))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

    if len(result) == 0:
        continue  # 如果没查到，跳过

    author1 = result[0][0]
    author2 = result[0][1]
    num = float(result[0][2])
    print(author1, author2, num)
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select * from author_net_point where author=%s "
            cursor.execute(sql, author1)
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
                Num = float(result[0][2]) + num
                sql = "update author_net_point set num=%s where id=%s"
                cursor.execute(sql, (Num, result[0][0]))
            else:
                sql = "insert into author_net_point (author,num) values (%s,%s)"
                cursor.execute(sql, (author1, num))
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
            sql = "select * from author_net_point where author=%s "
            cursor.execute(sql, author2)
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
                Num = float(result[0][2]) + num
                sql = "update author_net_point set num=%s where id=%s"
                cursor.execute(sql, (Num, result[0][0]))
            else:
                sql = "insert into author_net_point (author,num) values (%s,%s)"
                cursor.execute(sql, (author2, num))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();
