import io
import uuid
import requests
import pytest

from jsonschema import validate,ValidationError

import json
from API import params_config_date2
from API import ASR_config


def main(extid,param,reqid):

    response = requests.get(
        params_config_date2.SAPRP_URL_ALL+extid+"/penalties"
        , params=param, headers=reqid)
    return response



def t2():
    with open('extid_PS_URL4.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums


@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_date_200(extid,param):
    reqid = ASR_config.hex_uuid()
    with io.open('schema_peni_SAPRP.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main(extid,param,reqid)

    with open("data_penalties_URL_ALL_0408.txt","a") as file:
        # r=response.json()
        # r2 = r[1:0]
        err_message =''
        response_sch = response.json()
        try:
            validate(instance=response_sch,schema=schema)

        except ValidationError as er:
            err_message = '!'*10+'ERROR'+'!'*10+er.message
        #else:
            #response = response.json()
        a = json.dumps({extid:(err_message or response_sch)},ensure_ascii=False)
        b = a[1:-1]
        time = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        #id = ASR_config.hex_uuid()
        request_id = reqid


        file.write(str(request_id)+" / resptime : "+time +" / "+ params +" / extid : "+ b + ',')
        file.write('\n')
    assert response.status_code == 200
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())
