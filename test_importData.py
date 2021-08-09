import requests
import pytest

import json
from API import ASR_config

def main(extid):
    response = requests.get(
        ASR_config.url_DSV_KAM_STR+extid+"/infoFinance"
        , params=ASR_config.params, headers=ASR_config.headers)
    return response



def t2():
    with open('extid_data.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open("data2.txt", "a") as file:
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

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in ASR_config.extid_list_DSV_KAM_STR for param in ASR_config.params_list_long])
def test_date_200(extid,param):
    response = main(extid)
    assert response.status_code == 200,response.json()
    print(response)
    print(extid)
    print(ASR_config.requestid())
