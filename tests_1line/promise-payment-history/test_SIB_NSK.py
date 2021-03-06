import requests
import pytest

import json
from API import params_config_date2
from API import ASR_config

def main(extid,param):
    response = requests.get(
        "http://10.42.122.25/apiman-gateway/p1l/accounts-promise-payment/1.0-test/v1/finAccounts/finAccountNumber/"+extid+"/promise-payment?finAccountSysInst=SIB.NSK.STR&contactId=1212124&finAccountTZ=%2B07:00"
        ,params=param, headers=ASR_config.headers_MC)
    return response



def t2():
    with open('fa_id_SIB_NSK.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________?????

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_date_200(extid,param):
    response = main(extid,param)
    with open("data_payments_SIB_NSK_2604.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        file.write(c + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())