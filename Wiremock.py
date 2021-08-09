import random

import json
import requests

url = "http://sks06ap569.ks.rt.ru:8088/__admin/mappings/new"
# body = {
#   "request": {
#     "method": "GET",
#     "url": "/apiman-gateway/adapters/start-plsql-adapter-vlg-udm/1.0-test/v1/finAccounts/5980885317/infoFinance?dateStart=2019-03&dateEnd=2021-02"
#   },
#   "response": {
#     "status": 200,
#     "jsonBody": {
#     "calculations": [],
#     "totalAccrued": "0.00",
#     "totalPaid": "0.00"
#
# },
#     "headers": {
#       "Content-Type": "text/plain"
#     },
#    "delayDistribution": {
#         "type": "uniform",
#         "lower": 1000,
#         "upper": 100
# }
#   }
# }
def ext():
    data_list = []
    with open('data.txt') as file_data:
        for line_data in file_data:
            data_list.append(line_data.rstrip())
            #print(a)
    with open('1.txt','r') as file_ext:
        for line_ext in file_ext:
            #print(line_ext.rstrip())
            body =  {
            "request": {
            "method": "GET",
            "url": f"/{line_ext.rstrip()}/infoFinance?dateStart=2019-03&dateEnd=2021-02"
            },
            "response": {
            "status": 200,
            "jsonBody": json.loads(random.choice(data_list).rstrip()),
            "headers": {
            "Content-Type": "application/json"
            },
            "delayDistribution":{
            "type":"uniform",
            "upper":1000,
            "lower":100
            }
            }
 }
            r = requests.post(url, json=body)
            print(r.status_code)





ext()

# def G():
#     with open('data.txt') as file:
#         for line in file:
#             print(line.rstrip())
#             #print(line[each])
#
#
# G()
#
# def Get():
#     request = requests.post(url,data = body)
#     return request