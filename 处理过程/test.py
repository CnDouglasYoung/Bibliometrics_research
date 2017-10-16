import time


H=int(time.strftime('%H',time.localtime(time.time())))+16
M='6'
if len(M)==1:
    M='0'+M
print(H,M)
