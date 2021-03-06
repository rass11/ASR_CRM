import requests
import pytest

import json

from API import ASR_config

def main(extid):
    response = requests.get(
        "http://10.42.122.25/apiman-gateway/p1l/accounts-promise-payment/1.0-test/v1/finAccounts/finAccountNumber/"+extid+"/promise-payment?finAccountSysInst=DSV.PRM.STR&contactId=1212124&finAccountTZ=%2B03:00"
        , headers=ASR_config.headers_MC)
    return response



def t2():
    with open('fa_id_DSV_PRM.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________?????

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open("data_promise-payment_DSV_PRM.txt", "a") as file:

        #r=response.json()
        #r2 = r[1:0]
        a = json.dumps({extid:response.json()},ensure_ascii=False)
        b = a[1:-1]
        c=str(response.elapsed.total_seconds())
        file.write(c+b+',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())