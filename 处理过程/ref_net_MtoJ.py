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

try:
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = "select ref_cn,tag,sum(num) from ref_net3 where num>20  and tag='引用' group by ref_cn,tag"
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();

for i in range(len(result)):
    if result[i][1]=='引用':
        print('{"name":"%s","value":"%s","type":"L1",},'%((result[i][0]+'引用'),result[i][2]))

try:
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = "select cn,sum(num) from ref_net3 where num>20  group by cn"
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();

for i in range(len(result)):
    print('{"name":"%s","value":"%s","type":"L2",},'%((result[i][0]+'文献'),result[i][1]))

try:
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = "select ref_cn,tag,sum(num) from ref_net3 where num>20 and tag='被引' group by ref_cn,tag"
        cursor.execute(sql)
        # 获取查询结果
        result = cursor.fetchall()
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();

for i in range(len(result)):
    if result[i][1]=='被引':
        print('{"name":"%s","value":"%s","type":"L3",},'%((result[i][0]+'被引'),result[i][2]))



print('],links: [')
for i in range(5000):
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select * from ref_net3 where id=%s"
            cursor.execute(sql, (i))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

    if len(result) == 0:
        continue  # 如果没查到，跳过
    if float(result[0][5]) <= 20:
        continue

    if result[0][1] == '引用':
        target = result[0][2]+'文献'
        if result[0][3] == 'J/D':
            source = result[0][4]+'引用'
        else:
            source = result[0][3]+'引用'
    else:
        target = result[0][4] + '被引'
        source = result[0][2] + '文献'
    if source == None or target == None or source == '' or target == '':
        continue

    print('{"source":"%s","target":"%s","value":"%s"},' % (source, target, result[0][5]))
