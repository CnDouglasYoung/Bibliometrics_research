import xlrd
import re
import pymysql
import pymysql.cursors


data2 = xlrd.open_workbook(r'F:\crawlers\New\cn.xls')  # 打开xls文件
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
for i in range(nrows):
    cell = [1] * 2
    print(i)
    for num in range(0, 2):
        cell[num] = " "
        cell[num] = (str((table2.row_values(i)[num])))
    if cell[1]=="":
        continue
    cn = re.split(r';',cell[1])


    try:
        connection = pymysql.connect(**config)
        with connection.cursor() as cursor:
            # 执行sql语句，进行查询
            if len(cn)>1:
                sql = "update ref set ref_cn1=%s,ref_cn2=%s where id=%s"
                cursor.execute(sql, (cn[0],cn[1],cell[0] ))
            else:
                sql = "update ref set ref_cn1=%s where id=%s"
                cursor.execute(sql, (cn[0], cell[0]))
            # 获取查询结果
        # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
        connection.commit()

    finally:
        connection.close();
