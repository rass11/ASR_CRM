import requests
import pytest

from API import ASR_config
from API import MC_config
import json

params = {
         'finAccountSysInst': 'UTK.ASH.KRS'
           }


def main(extid):
    response = requests.get("http://apiman.south.rt.ru/apiman-gateway/p1l/final-payment/1.0-test/v1/finAccounts/"+extid+"/final-payment",
   params=params,headers=MC_config.headers)
    return response


def t2():
    with open('tests_parse/final-payment/KURS/extid_final-payment.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums


@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open("tests_parse/final-payment/KURS/MC_final-payment.txt", "a") as file:
        #r=response.json()
        #r2 = r[1:0]
        a = json.dumps({extid:response.json()})
        b = a[1:-1]
        file.write(b+',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())