import requests
import pytest

import json
from API import params_config_date
from API import params_config_date2
from API import ASR_config

from jsonschema import validate,ValidationError

def main(extid,param,reqid):
    response = requests.get(
        params_config_date2.VLG_CHV+extid+"/detalization/mvno-fix"
        , params=param, headers=reqid)
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
    with open("data_MVNO_calls_DSV_PRM.txt", "a") as file:
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

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date.params_date3])
def test_date_200(extid,param):
    reqid = ASR_config.hex_uuid()
    response = main(extid,param,reqid)

    with open("data_MVNO_calls_VLG_CHV_2607.txt", "a") as file:

        # response = response.json()
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        time = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        # id = ASR_config.hex_uuid()
        request_id = reqid

        file.write(str(request_id) + " / resptime : " + time + " / " + params + " / extid : " + b + ',')
        file.write('\n')
        # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())
