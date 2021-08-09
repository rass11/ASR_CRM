import requests
import pytest

import json
from API import params_config_date
from API import params_config_date2
from API import ASR_config

def main(extid,param):
    response = requests.get(
        params_config_date.STR_VLG_CHV+extid+"/payments"
        , params=param, headers=ASR_config.headers)
    return response



def t2():
    with open('extid_VLG_CHV_psi.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open("data.txt", "a") as file:
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

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date_psi])
def test_date_200(extid,param):
    response = main(extid,param)
    with open("data_payments_VLG_CHV_0707_psi.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(c + params + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())
