import io
import requests
import pytest

import json

from jsonschema import validate,ValidationError
from API import params_config_date2
from API import ASR_config

def main(extid,param):
    response = requests.get(
        params_config_date2.VLG_CHV_rest+extid+"/infoFinance"
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
        a = json.dumps({extid:response.json()},ensure_ascii=False)
        b = a[1:-1]
        file.write(b+',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_date_200(extid,param):
    with io.open('schema_calculations_start.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main(extid, param, )

    with open("data_calculations_START_CHV_0408.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        err_message = ''
        response_sch = response.json()
        try:
            validate(instance=response_sch, schema=schema)

        except ValidationError as er:
            err_message = '!' * 10 + 'ERROR' + '!' * 10 + er.message
        # else:
        # response = response.json()

        a = json.dumps({extid: (err_message or response_sch)}, ensure_ascii=False)
        b = a[1:-1]
        time = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(time + params + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())
