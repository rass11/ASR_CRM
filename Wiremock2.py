import requests
import random
t2 = 1
url = "http://sks06ap569.ks.rt.ru:8088/__admin/mappings/new"
body = {

    "url": "/apiman-gateway/adapters/start-plsql-adapter-vlg-udm/1.0-test/v1/finAccounts//infoFinance?dateStart=2019-03&dateEnd=2021-02"
  }

def Get():
    request = requests.post(url,data = body)
    return request

def G():
    with open('data.txt') as file:
        for line in file:
            print(line.rstrip())
            #print(line[each])


def t2():
    with open('1.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
t2()