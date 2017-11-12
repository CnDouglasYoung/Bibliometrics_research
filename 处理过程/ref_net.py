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
for i in range(13709):
    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            sql = "select * from ref where id=%s"
            cursor.execute(sql, (i))
            # 获取查询结果
            result = cursor.fetchall()
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()
    finally:
        connection.close();

    if len(result) == 0:
        continue  # 如果没查到，跳过
    result = result[0]
    ref_Type = result[6][1]
    if ref_Type == 'J' or ref_Type == 'D':
        print('is  ', result)
        time1 = int(result[5])
        time2 = int(result[10])
        if result[4] == '':
            if result[12] == None:
                if time1 >= time2:
                    print('     1  ', result[3], '<-', result[11])
                    cn1 = result[3]
                    ref_cn1 = result[11]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
                else:
                    print('     2  ', result[11], '<-', result[3])
                    cn1 = result[3]
                    ref_cn1 = result[11]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
            else:
                if time1 >= time2:
                    print('     1  ', result[3], '<-', result[11], result[12])
                    cn1 = result[3]
                    ref_cn1 = result[11]
                    ref_cn2 = result[12]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn1, ref_cn2))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn1, 'J/D', ref_cn2, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
                else:
                    print('     2  ', result[11], result[12], '<-', result[3])
                    cn1 = result[3]
                    ref_cn1 = result[11]
                    ref_cn2 = result[12]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn1, ref_cn2))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn1, 'J/D', ref_cn2, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
        else:
            if result[12] == None:
                if time1 >= time2:
                    print('     1  ', result[3], result[4], '<-', result[11])
                    cn1 = result[3]
                    cn2 = result[4]
                    ref_cn1 = result[11]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn2, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn2, 'J/D', ref_cn1, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
                else:
                    print('     2  ', result[11], '<-', result[3], result[4])
                    cn1 = result[3]
                    cn2 = result[4]
                    ref_cn1 = result[11]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn2, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn2, 'J/D', ref_cn1, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
            else:
                if time1 >= time2:
                    print('     1  ', result[3], result[4], '<-', result[11], result[12])
                    cn1 = result[3]
                    cn2 = result[4]
                    ref_cn1 = result[11]
                    ref_cn2 = result[12]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn2, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn2, 'J/D', ref_cn1, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn2, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn2, 'J/D', ref_cn1, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='引用'"
                            cursor.execute(sql, (cn2, ref_cn2))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('引用', cn2, 'J/D', ref_cn1, '0.4'))
                            else:
                                num = float(result[0][1]) + 0.4
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
                else:
                    print('     2  ', result[11], result[12], '<-', result[3], result[4])
                    cn1 = result[3]
                    cn2 = result[4]
                    ref_cn1 = result[11]
                    ref_cn2 = result[12]
                    try:
                        connection = pymysql.connect(**config)
                        with connection.cursor() as cursor:
                            # 执行sql语句，进行查询
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn1, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn1, 'J/D', ref_cn1, '1'))
                            else:
                                num = float(result[0][1]) + 1
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn2, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn2, 'J/D', ref_cn1, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn2, ref_cn1))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn2, 'J/D', ref_cn1, '0.7'))
                            else:
                                num = float(result[0][1]) + 0.7
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
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
                            sql = "select id,num from ref_net where cn=%s and ref_cn=%s and tag='被引'"
                            cursor.execute(sql, (cn2, ref_cn2))
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
                            if len(result) == 0:
                                sql = "insert into ref_net (tag,cn,ref_Type,ref_cn,num) values (%s,%s,%s,%s,%s)"
                                cursor.execute(sql, ('被引', cn2, 'J/D', ref_cn1, '0.4'))
                            else:
                                num = float(result[0][1]) + 0.4
                                sql = 'update ref_net set num=%s where id=%s'
                                cursor.execute(sql, (num, result[0][0]))
                            # 获取查询结果
                            result = cursor.fetchall()
                        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                        connection.commit()
                    finally:
                        connection.close();
    else:
        print('not ', result)
        if result[4] == '':
            print('     3  ', result[3], '<-', result[6])
            cn1 = result[3]
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select id,num from ref_net where cn=%s and ref_Type=%s"
                    cursor.execute(sql, (cn1, ref_Type))
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
                    if len(result) == 0:
                        sql = "insert into ref_net (tag,cn,ref_Type,num) values (%s,%s,%s,%s)"
                        cursor.execute(sql, ('引用', cn1, ref_Type, '1'))
                    else:
                        num = float(result[0][1])+1
                        sql = 'update ref_net set num=%s where id=%s'
                        cursor.execute(sql, (num, result[0][0]))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();

        else:
            print('     3  ', result[3], result[4], '<-', result[6])
            cn2 = result[4]
            cn1 = result[3]
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select id,num from ref_net where cn=%s and ref_Type=%s"
                    cursor.execute(sql, (cn1, ref_Type))
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
                    if len(result) == 0:
                        sql = "insert into ref_net (tag,cn,ref_Type,num) values (%s,%s,%s,%s)"
                        cursor.execute(sql, ('引用', cn1, ref_Type, '1'))
                    else:
                        num = float(result[0][1]) + 1
                        sql = 'update ref_net set num=%s where id=%s'
                        cursor.execute(sql, (num, result[0][0]))
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
                    sql = "select id,num from ref_net where cn=%s and ref_Type=%s"
                    cursor.execute(sql, (cn2, ref_Type))
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
                    if len(result) == 0:
                        sql = "insert into ref_net (tag,cn,ref_Type,num) values (%s,%s,%s,%s)"
                        cursor.execute(sql, ('引用', cn2, ref_Type, '0.7'))
                    else:
                        num = float(result[0][1]) + 0.7
                        sql = 'update ref_net set num=%s where id=%s'
                        cursor.execute(sql, (num, result[0][0]))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
    #time.sleep(1)
