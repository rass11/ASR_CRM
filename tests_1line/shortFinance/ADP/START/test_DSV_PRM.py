import io
import requests
import pytest

import json

from jsonschema import validate,ValidationError
from API import params_config_date2
from API import ASR_config

def main(extid):
    response = requests.get(
        params_config_date2.DSV_PRM_rest+extid+"/shortFinance"
        , headers=ASR_config.headers)
    return response



def t2():
    with open('extid_DSV_PRM_STR1407.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    with io.open('schema_shortFinance.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main(extid)

    with open("data_shortFinance_DSV_PRM_1407.txt", "a") as file:
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
        file.write(time + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())
