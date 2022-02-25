#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://portswigger.net/web-security/sql-injection/blind/lab-conditional-responses"
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

r = requests.get(url=url,proxies=proxies,verify=False)
print(r.status_code)