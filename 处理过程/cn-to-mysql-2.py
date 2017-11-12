import requests  # 导入requests 模块
import re
from urllib import request
import random
import time
import pymysql
import pymysql.cursors


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
        for num in range(4787, 5001):
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    sql = "select Type,ref_title from ref where id=%s"
                    cursor.execute(sql, (num))
                    # 获取查询结果
                    result = cursor.fetchall()
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
            if not (result[0][0] == '[J]' or result[0][0] == '[D]'):
                continue
            print(result)
            continue
            # print(num,result[0][0],result[0][1][0:-3])
            url = "http://s.wanfangdata.com.cn/Paper.aspx?q=%s&f=top" % result[0][1][0:-3]
            web = self.request(url)
            ref_url = re.search(r'class="title" h.*target=', web.text)
            if ref_url == None:
                continue
            ref_url = re.search(r'http.*\'', ref_url.group())
            t = int(time.clock())
            useTime = t - told
            print(useTime, 's ,共用时', str(t / 60)[:6], '分钟', )
            told = int(time.clock())
            time.sleep(1)

            ref_web = self.request(ref_url.group()[:-1])
            cn = re.search(r'分类号([.$\s\S]*?)<([.$\s\S]*?)<([.$\s\S]*?)<', ref_web.text)
            if cn == None:
                continue
            cn = re.search(r'">.*<', cn.group()).group()[2:-1]
            cn = re.split(r' ', cn)
            try:
                connection = pymysql.connect(**config)
                with connection.cursor() as cursor:
                    # 执行sql语句，进行查询
                    if len(cn) > 1:
                        print('   ', num, ref_url.group(), cn[0], cn[1])
                        sql = "update ref set ref_cn1=%s,ref_cn2=%s where id=%s"
                        cursor.execute(sql, (cn[0], cn[1], num))
                    else:
                        print('   ', num, ref_url.group(), cn[0])
                        sql = "update ref set ref_cn1=%s where id=%s"
                        cursor.execute(sql, (cn[0], num))
                        # 获取查询结果
                # 没有设置默认自动提交，需要主动提交，以保存所执行的语句
                connection.commit()
            finally:
                connection.close();
            time.sleep(1)

    def request(self, url):  # 返回网页的response
        global count
        global H
        global M
        count = count + 1
        if count % 50 == 0:
            H = str(int(time.strftime('%H', time.localtime(time.time()))) + 16)
            M = time.strftime('%M', time.localtime(time.time()))
            if len(M) == 1:
                M = '0' + M
        print(url, H, M)
        # print(url)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch' \
                     'rome/58.0.3029.81 Safari/537.36'
        referer = "nhttp://kns.cnki.net/kns/brief/result.aspx"
        cookie = 'WFKS.Auth%3d%7b%22Context%22%3a%7b%22AccountIds%22%3a%5b%5d%2c%22Data%22%3a%5b%5d%2c%22Sessi' \
                 'onId%22%3a%22548d6c9f-f3de-4049-9439-c80d94ee85a6%22%2c%22Sign%22%3a%22hi+authserv%22%7d%2c%2' \
                 '2LastUpdate%22%3a%222017-06-06T' + H + '%3a' + M + '%3a58Z%22%2c%22Ti' \
                                                                     'cketSign%22%3a%228KUr94j9zXscKroQDl4J9A%3d%3d%22%7d'

        headers = {'User-Agent': user_agent,
                   "Referer": referer,
                   "cookie": cookie}
        r = requests.get(url, headers=headers, timeout=100, proxies="183.153.40.32:808")
        return r


count = 49
print(time.clock())
beauty = BeautifulPicture()  # 创建类的实例
beauty.get_pic()  # 执行类中的方法
