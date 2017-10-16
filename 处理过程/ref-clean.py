import xlrd
import re
import time
import xlwt

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
data = xlrd.open_workbook(r'F:\crawlers\Ref2.xls')  # 打开xls文件
table = data.sheets()[0]  # 打开第一张表
nrows = table.nrows  # 获取表的行数
print(nrows)
for i in range(0,nrows):
    date = (str((table.row_values(i)[6])))[:4]
    ref = (str((table.row_values(i)[3])))
    if len(ref)<3:
        continue
    index = -4
    si = ref[index - 1:index]
    if si==".":
        print(si)
        date = ref[index:]
    print("date:%s" % date)
    for i2 in range(0,6):
        ws.write(i,i2,(str((table.row_values(i)[i2]))))
    ws.write(i,6,date)

wb.save("NRef2.xls")
print("over")
