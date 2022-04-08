import subprocess
import time
from datetime import datetime
Time = False
# ghat
ip = subprocess.check_output('ipconfig/release',shell=True)
print("Disconnect")
# vasl
# ip = subprocess.check_output('ipconfig/renew',shell=True)
while (Time==False) :
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    maine_time = str(current_time)
    print(maine_time)
    time.sleep(60)
    if maine_time == "02:00"or maine_time == "2:00" or maine_time == "02:01"or maine_time == "2:01":
        Time = True
        ip = subprocess.check_output('ipconfig/renew',shell=True)
        print("Connect")
while (Time==True):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    maine_time = str(current_time)
    print(maine_time)
    time.sleep(60)
    if maine_time == "07:00"or maine_time == "7:00" or maine_time == "07:01"or maine_time == "7:01":
        Time = False
        ip = subprocess.check_output('ipconfig/release',shell=True)
        print("Disconnect")
a = input("are you conect the net ?")
if a == 'yes':
     ip = subprocess.check_output('ipconfig/renew',shell=True)
     print("Connect")
        