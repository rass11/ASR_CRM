import requests
import pytest

import json


from API import ASR_config

def main(extid):
    response = requests.get(
        ASR_config.url_UG+extid+"/infoFinance"
        , params=ASR_config.params, headers=ASR_config.headers)
    return response

#_____________________Тесты



@pytest.mark.parametrize("extid, result",[(ext,200) for ext in ASR_config.extid_list_UG])
def test_200(extid,result):
    response = main(extid)
    with open("data.txt", "a") as file:
        file.write(json.dumps({extid:response.json()}))
        file.write('\n')
    #assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in ASR_config.extid_list_UG for param in ASR_config.params_list])
def test_date_200(extid,param):
    response = main(extid)
    assert response.status_code == 200,response.json()
    print(response)
    print(extid)
    print(ASR_config.requestid())


