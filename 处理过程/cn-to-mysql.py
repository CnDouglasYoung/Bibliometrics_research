import requests  # 导入requests 模块
import re
from urllib import request
import random
import time
import pymysql
import pymysql.cursors
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


class BeautifulPicture():
    def get_pic(self):
        told = 0
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '',
            'db': 'test',
            'charset': 'utf8'
        }
        data = xlrd.open_workbook(r'F:\crawlers\New\cn2.xls')  # 打开xls文件
        table = data.sheets()[0]  # 打开第一张表
        i = table.nrows
        rb = open_workbook('f:\\crawlers\\New\cn2.xls')
        wb = copy(rb)
        ws = wb.get_sheet(0)

        for num in range(10001,13699):
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select Type,ref_title,ref_cn1 from ref where id=%s"
                    cursor.execute(sql, (num))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
            if not (result[0][0] == '[J]' or result[0][0] == '[D]'):
                continue
            if result[0][2] != None:
                continue

            url = "http://xueshu.baidu.com/s?wd=" + result[0][1][0:-3]
            print(url)
            tag = 0
            web = self.request(url)
            ref_url = re.search(r'http://www.cnki.com.cn/Article/([.$\s\S]*?)"', web.text)
            if ref_url == None:
                ref_url = re.search(r'http://kns.cnki.([.$\s\S]*?)"', web.text)
                if ref_url == None:
                    print('Error')
                    continue
                else:
                    tag = 1
                    ref_url = ref_url.group()[:-1]
            else:
                tag = 2
                ref_url = ref_url.group()[:-1]

            print(ref_url)
            ref_web = self.request(ref_url).text

            if tag == 1:
                cn = re.search(r'分类号：<([.$\s\S]*?)<', ref_web)
                if cn != None:
                    cn = re.search(r'>.*?<', cn.group()).group()[1:-1]
                    print(cn)
                else:
                    print(ref_web)
            if tag == 2:
                cn = re.search(r'分类号】：<.([.$\s\S]*?)<([.$\s\S]*?)<', ref_web)
                if cn != None:
                    cn = cn.group()[16:]
                    cn = re.search(r'>([.$\s\S]*?)<', cn).group()[1:-1]
                    print(cn)
            i = i + 1
            ws.write(i, 0, num)
            ws.write(i, 1, cn)

            print(num)
        wb.save('cn2.xls')

    def request(self, url):  # 返回网页的response

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch' \
                     'rome/58.0.3029.81 Safari/537.36'

        headers = {'User-Agent': user_agent,
                   }
        r = requests.get(url, headers=headers, timeout=100)
        return r


print(time.clock())
count = 19
beauty = BeautifulPicture()  # 创建类的实例
beauty.get_pic()  # 执行类中的方法
