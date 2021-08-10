import requests
import pytest

import json

from API import ASR_config

def main(extid):
    response = requests.get(
        "http://10.42.122.25/apiman-gateway/p1l/accounts-promise-payment/1.0-test/v1/finAccounts/finAccountNumber/"+extid+"/promise-payment?finAccountSysInst=SIB.NSK.STR&contactId=1212124&finAccountTZ=%2B07:00"
        , headers=ASR_config.headers_MC)
    return response



def t2():
    with open('fa_id_SIB_NSK1307.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    reqid = ASR_config.hex_uuid()
    response = main(extid)
    with open("data_promise-payment_SIB_NSK_1008.txt", "a") as file:

        #r=response.json()
        #r2 = r[1:0]
        a = json.dumps({extid:response.json()},ensure_ascii=False)
        b = a[1:-1]
        time = str(response.elapsed.total_seconds())

        request_id = reqid

        file.write(str(request_id) + " / resptime : " + time + " / " + " / extid : " + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())