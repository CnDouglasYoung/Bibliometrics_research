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
try:
    connection = pymysql.connect(**config)
    with connection.cursor() as cursor:
        # 执行sql语句，进行查询
        sql = "SELECT id FROM `ref_net` "
        cursor.execute(sql)
        # 获取查询结果
        Result = cursor.fetchall()
    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
    connection.commit()
finally:
    connection.close();

for i in range(0,len(Result)):
    if i==3662:
        print(1)
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select * from ref_net where id=%s"
            cursor.execute(sql, (Result[i][0]))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

    if len(result) == 0:
        continue

    result = result[0]
    # print(result)
    tag = result[1]
    cn = result[2][:2]
    ref_Type = result[3]
    ref_cn = result[4]
    num = float(result[5])
    if ref_cn == None:
        ref_cn = '缺失'

    if ref_Type == "J/D":

        if ref_cn == None:
            ref_cn = '缺失'
        ref_cn = re.split(r'，', ref_cn)
        if len(ref_cn) > 1:
            print(ref_cn)
            if len(ref_cn[0])>2:
                ref_cn[0]=ref_cn[0][:2]
            if len(ref_cn[1]) > 2:
                ref_cn[1] = ref_cn[1][:2]
            # 是否存在 ref_cn0
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select id,num from ref_net3 where tag=%s and cn=%s and ref_cn=%s"
                    cursor.execute(sql, (tag, cn, ref_cn[0]))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
            # 如果存在，update
            if len(result) > 0:
                try:
                    connection = pymysql.connect(**config)
                    with connection.cursor() as cursor:
                        # 执行sql语句，进行查询
                        Num = float(result[0][1]) + num
                        sql = "update ref_net3 set num=%s where id=%s"
                        cursor.execute(sql, (Num, result[0][0]))
                        # 获取查询结果
                        result = cursor.fetchall()
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    connection.close();
            # 如果不存在，insert
            else:
                try:
                    connection = pymysql.connect(**config)
                    with connection.cursor() as cursor:
                        # 执行sql语句，进行查询
                        sql = "insert into ref_net3 (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                        cursor.execute(sql, (tag, cn, ref_Type, ref_cn[0], num))
                        # 获取查询结果
                        result = cursor.fetchall()
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    connection.close();

            # 是否存在 ref_cn1
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select id,num from ref_net3 where tag=%s and cn=%s and ref_cn=%s"
                    cursor.execute(sql, (tag, cn, ref_cn[1]))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
            # 如果存在，update
            if len(result) > 0:
                try:

                    connection = pymysql.connect(**config)
                    with connection.cursor() as cursor:
                        # 执行sql语句，进行查询
                        Num = float(result[0][1]) + num * 0.7
                        sql = "update ref_net3 set num=%s where id=%s"
                        cursor.execute(sql, (Num, result[0][0]))
                        # 获取查询结果
                        result = cursor.fetchall()
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    connection.close();
            # 如果不存在
            else:
                try:
                    connection = pymysql.connect(**config)
                    with connection.cursor() as cursor:
                        # 执行sql语句，进行查询
                        num = num * 0.7
                        sql = "insert into ref_net3 (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                        cursor.execute(sql, (tag, cn, ref_Type, ref_cn[1], num))
                        # 获取查询结果
                        result = cursor.fetchall()
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    connection.close();
        else:
            if len(ref_cn[0]) > 2:
                ref_cn[0] = ref_cn[0][:2]
            if len(cn) > 2:
                cn = cn[:2]
            # 是否存在
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select id,num from ref_net3 where tag=%s and cn=%s and ref_cn=%s"
                    cursor.execute(sql, (tag, cn, ref_cn[0]))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
            # 如果存在，update
            if len(result) > 0:
                try:
                    connection = pymysql.connect(**config)
                    with connection.cursor() as cursor:
                        # 执行sql语句，进行查询
                        Num = float(result[0][1]) + num
                        sql = "update ref_net3 set num=%s where id=%s"
                        cursor.execute(sql, (Num, result[0][0]))
                        # 获取查询结果
                        result = cursor.fetchall()
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    connection.close();
            # 如果不存在，insert
            else:
                try:
                    connection = pymysql.connect(**config)
                    with connection.cursor() as cursor:
                        # 执行sql语句，进行查询
                        sql = "insert into ref_net3 (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                        cursor.execute(sql, (tag, cn, ref_Type, ref_cn[0], num))
                        # 获取查询结果
                        result = cursor.fetchall()
                    # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                    connection.commit()
                finally:
                    connection.close();
    else:
        if len(cn) > 2:
            cn = cn[:2]
        if len(ref_cn) > 2:
            ref_cn = ref_cn[:2]
            print(cn, ref_cn)
        try:
            connection = pymysql.connect(**config)
            with connection.cursor() as cursor:
                # 执行sql语句，进行查询
                print(tag, cn, ref_cn)
                sql = "select id,num from ref_net3 where tag=%s and cn=%s and ref_Type=%s"
                cursor.execute(sql, (tag, cn, ref_Type))
                # 获取查询结果
                result = cursor.fetchall()
            # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
            connection.commit()
        finally:
            connection.close();
        # 如果存在，update
        if len(result) > 0:
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    Num = float(result[0][1]) + num
                    sql = "update ref_net3 set num=%s where id=%s"
                    cursor.execute(sql, (Num, result[0][0]))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
        # 如果不存在，insert
        else:
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "insert into ref_net3 (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                    cursor.execute(sql, (tag, cn, ref_Type, ref_cn, num))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
    print(cn,ref_cn)
