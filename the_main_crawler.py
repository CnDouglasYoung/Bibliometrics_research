import requests  # 导入requests 模块
import re
from urllib import request
import random
import time
import xlrd
from xlrd import open_workbook
from xlutils.copy import copy


class BeautifulPicture():
    def get_pic(self):
        data = xlrd.open_workbook(r'F:\new3.xls')  # 打开xls文件
        table = data.sheets()[0]  # 打开第一张表
        table2 = data.sheets()[1]  # 打开第一张表
        i = table.nrows
        i1 = 0
        i2 = table2.nrows
        told = 0

        rb = open_workbook('f:\\new3.xls')
        wb = copy(rb)
        # 通过get_sheet()获取的sheet有write()方法
        ws = wb.get_sheet(0)
        ws1 = wb.get_sheet(1)
        p = 102
        for num in range(22,26):
            web_url = 'http://kns.cnki.net/kns/brief/brief.aspx?curpage=%s&RecordsPerPage=50&QueryID=1&ID=&turnpage=1' \
                      '&tpagemode=L&dbPrefix=CJFQ&Fields=&DisplayMode=listmode&PageName=ASP.brief_default_result_aspx#J_ORDER&' % num
            print(web_url)
            t = int(time.clock())
            print(t/60,'分钟')
            useTime = t - told
            if useTime<10:
                whiteTime = 30
                print("等待%s秒" % whiteTime)
                #time.sleep(whiteTime)
            if not(useTime > 120 or useTime<10):
                print("useTime=%s" % useTime)
                whiteTime = 120 - useTime
                print("等待%s秒" % whiteTime)
                time.sleep(whiteTime)
            told = int(time.clock())
            print(t)
            print('开始网页get请求')
            r = self.request(web_url)
            yan = re.search(r'参数错误', r.text)
            if yan != None:
                print("参数")
                break
            yan = re.search(r'验证码', r.text)
            if yan != None:
                print("验证")
                break
            soup = re.findall(r'<TR([.$\s\S]*?)</TR>', r.text)
            for a in soup:
                print("-", i1)
                i1 += 1
                name = re.search(r'_blank.*<', a)
                name = name.group()[8:-1]
                name = re.sub(r'<font class=Mark>', '', name)
                name = re.sub(r'</font>', '', name)

                url = re.search(r'href=.*? ', a)
                url = url.group()

                url = "http://kns.cnki.net/KCMS/" + url[11:-2]
                #print("url:%s" % url)
                FN = re.search(r'filename.*?&', url).group()
                print(FN)
                DN = re.search(r'dbname.*?&', url).group()
                DC = re.search(r'DbCode.*?&', url).group()
                DUrl = "http://kns.cnki.net/kcms/detail/frame/list.aspx?%s%s%sRefType=1" % (FN, DN, DC)
                print(DUrl)
                R = self.request(DUrl)

                isR = re.search(r'参考文献', R.text)
                if i1 == 1:
                    print("name:%s" % name)
                if isR == None:
                    continue
                # 详情页
                print(i)
                print("name:%s" % name)
                d = self.request(url).text
                # print(d)
                type = re.search(r'"\).html\(".*?"', d)
                type = type.group()[9:-1]
                ins = re.search(r'TurnPageToKnet\(\'in\',\'.*?\'', d)
                if ins == None:
                    continue
                ins = ins.group()[21:-1]
                wt = re.findall(r'TurnPageToKnet\(\'au\',\'.*?\'', d)
                writer = ""
                for w in wt:
                    writer = writer + "," + w[21:-1]
                writer = writer[1:]
                ws.write(i, 0, name)
                ws.write(i, 1, writer)
                ws.write(i, 2, type)
                ws.write(i, 15, num)
                ws.write(i, 16, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                kw = re.findall(r'TurnPageToKnet\(\'kw\',\'.*?\'', d)
                tnum = 0

                for tkw in kw:
                    tnum += 1
                    tkw = tkw[21:-1]
                    if tnum > 8:
                        break
                    ws.write(i, 2 + tnum, tkw)
                fund = re.search(r'TurnPageToKnet\(\'fu\',\'.*?\'', d)
                if fund != None:
                    fund = fund.group()[21:-1]
                    ws.write(i, 11, fund)
                cn = re.search(r'ZTCLS.*?</p', d)
                if cn != None:
                    cn = cn.group()[19:-3]
                    ws.write(i, 12, cn)
                jg = re.search(r'TurnPageToKnet\(\'in\',\'.*?\'', d)
                if jg != None:
                    jg = jg.group()[21:-1]
                    print(jg)
                    ws.write(i, 17, jg)
                sourinfo = re.search(r'sourinfo([.$\s\S]*?)</div', d)
                if sourinfo != None:
                    sourinfo = sourinfo.group()
                    # print(sourinfo)
                    from_ = re.search(r'title.*</a', sourinfo).group()
                    from_ = re.sub(r'title">.*?>', '', from_)
                    from_ = re.sub(r'</a', '', from_)
                    ws.write(i, 13, from_)
                    core = re.search(r'中文核心期刊', sourinfo)
                    if core != None:
                        print(core.group())
                        ws.write(i, 14, "中文核心期刊")

                print(DUrl)
                if isR != None:
                    # print(R.text)
                    tdb = re.findall(r'dbTitle">([.$\s\S]*?)</ul', R.text)
                    for db in tdb:
                        list = re.findall(r'<li([.$\s\S]*?)/li', db)
                        for tlist in list:
                            Tlist = ""
                            tlist = re.sub(r' ', '', tlist)
                            tlist = re.sub(r'\s+', '', tlist)
                            tlist = re.findall(r'>([.$\s\S]*?)<', tlist)
                            for part in tlist:
                                Tlist = Tlist + part
                            print("<-", Tlist)
                            ws1.write(i2, 0, name)
                            ws1.write(i2, 1, writer)
                            ws1.write(i2, 2, Tlist)
                            ws1.write(i2, 4, num)
                            ws1.write(i2, 5, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                            i2 += 1

                Next = re.findall(r'ShowPage.*,', R.text)
                for TN in Next:
                    NextNum = re.search(r'\'.*?\'', TN).group()[1:-2]
                    TN = TN[15:-2]

                    print()
                    print(TN)
                    TN = re.sub(r'\'', '', TN)
                    for NNum in range(2, int(NextNum)):
                        turl = "http://kns.cnki.net/kcms/detail/frame/list.aspx?%s%s%sRefType=1&CurDBCode=%s&page=%s" % (
                        FN, DN, DC, TN, NNum)
                        if turl == "http://kns.cnki.net/kcms/detail/frame/list.aspx?FileName=1014421085.nh&DbName=CDFDLAST2015&DbCode=CDFD&RefType=1&CurDBCode=CBBD&page=3":
                            continue
                        print(turl)
                        ThisHtml = self.request(turl)
                        # print(ThisHtml.text)
                        regex = TN + '">[0-9]([.$\s\S]*?)/ul'
                        p = re.compile(r'' + regex + '')
                        m = p.search(ThisHtml.text)
                        if m != None:
                            list = re.findall(r'<li([.$\s\S]*?)/li', m.group())
                            for tlist in list:
                                Tlist = ""
                                tlist = re.sub(r' ', '', tlist)
                                tlist = re.sub(r'\s+', '', tlist)
                                tlist = re.findall(r'>([.$\s\S]*?)<', tlist)
                                for part in tlist:
                                    Tlist = Tlist + part
                                print("<-", Tlist)
                                ws1.write(i2, 0, name)
                                ws1.write(i2, 1, writer)
                                ws1.write(i2, 2, Tlist)
                                ws1.write(i2, 4, num)
                                ws1.write(i2, 5, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                                i2 += 1



                DUrl = "http://kns.cnki.net/kcms/detail/frame/list.aspx?%s%s%sRefType=3" % (FN, DN, DC)
                R1 = self.request(DUrl)
                isR = re.search(r'文献', R1.text)
                if isR != None:
                    tdb = re.findall(r'dbTitle">([.$\s\S]*?)</ul', R1.text)
                    for db in tdb:
                        list = re.findall(r'<li([.$\s\S]*?)/li', db)
                        for tlist in list:
                            Tlist = ""
                            tlist = re.sub(r' ', '', tlist)
                            tlist = re.sub(r'\s+', '', tlist)
                            tlist = re.findall(r'>([.$\s\S]*?)<', tlist)
                            for part in tlist:
                                Tlist = Tlist + part
                            print("->", Tlist)
                            ws1.write(i2, 0, name)
                            ws1.write(i2, 1, writer)
                            ws1.write(i2, 2, Tlist)
                            ws1.write(i2, 3, "1")
                            ws1.write(i2, 4, num)
                            ws1.write(i2, 5, time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
                            i2 += 1


                    Next = re.findall(r'ShowPage.*,', R1.text)
                    for TN in Next:
                        NextNum = re.search(r'\'.*?\'', TN).group()[1:-2]
                        TN = TN[15:-2]
                        print(TN)
                        for NNum in range(2, int(NextNum) + 2):
                            turl = "http://kns.cnki.net/kcms/detail/frame/list.aspx?%s%s%sRefType=3&CurDBCode=" \
                                   "%s&page=%s" % (FN, DN, DC, TN, NNum)
                            print(turl)
                            ThisHtml = self.request(turl)
                            regex = TN + '">([.$\s\S]*?)/ul'
                            p = re.compile(r'' + regex + '')
                            m = p.search(ThisHtml.text)
                            if m != None:
                                list = re.findall(r'<li([.$\s\S]*?)/li', m.group())
                                n = 1
                                for tlist in list:
                                    n = n + 1
                                    Tlist = ""
                                    tlist = re.sub(r' ', '', tlist)
                                    tlist = re.sub(r'\s+', '', tlist)
                                    tlist = re.findall(r'>([.$\s\S]*?)<', tlist)
                                    for part in tlist:
                                        Tlist = Tlist + part
                                    print("->", Tlist)
                                    ws1.write(i2, 0, name)
                                    ws1.write(i2, 1, writer)
                                    ws1.write(i2, 2, Tlist)
                                    ws1.write(i2, 3, "1")
                                    ws1.write(i2, 4, num)
                                    ws1.write(i2, 5, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
                                    i2 += 1


                # ws.write(i, 0, a)
                i += 1

        wb.save('f:\\new3.xls')

    def request(self, url):  # 返回网页的response

        #print(url)
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Ch' \
                     'rome/58.0.3029.81 Safari/537.36'
        referer = "nhttp://kns.cnki.net/kns/brief/result.aspx"
        cookie = 'Ecp_ClientId=5170306082301247979; kc_cnki_net_uid=83156c67-5744-0529-58ac-fe492f7211a1; UM_distinctid=15ae6a0e0c43e2-08fcf5b31b567-5d4e211f-100200-15ae6a0e0c5766; cnkiUserKey=e382401a-29dd-f206-d207-84603f47bbc8; RsPerPage=50; ASP.NET_SessionId=xagntzexbqfjm1xhbtio2mnc; SID_kns=123107; SID_kinfo=125103; SID_klogin=125143; SID_kredis=125143; SID_krsnew=125131; SID_crrs=125134; DisplaySave=10; ASPSESSIONIDAQQQRSCR=ODMLCIIBOKCOJHDMBBEIBMFC; LID=WEEvREcwSlJHSldRa1FhdkJkcGkyNTdZUjRsV0dMMXZLNDkwQmhtaTA4bz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!; c_m_LinID=LinID=WEEvREcwSlJHSldRa1FhdkJkcGkyNTdZUjRsV0dMMXZLNDkwQmhtaTA4bz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4ggI8Fm4gTkoUKaID8j8gFw!!&ot=06/04/2017 22:26:43; c_m_expire=2017-06-04 22:26:43; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"nj0232","ShowName":"%e8%8b%8f%e5%b7%9e%e5%a4%a7%e5%ad%a6%e5%9b%be%e4%b9%a6%e9%a6%86","UserType":"bk","r":"q30qYT"}'



        headers = {'User-Agent': user_agent,
                   "Referer": referer,
                   "cookie": cookie}
        r = requests.get(url, headers=headers, timeout=30)
        return r


print(time.clock())
beauty = BeautifulPicture()  # 创建类的实例
beauty.get_pic()  # 执行类中的方法
