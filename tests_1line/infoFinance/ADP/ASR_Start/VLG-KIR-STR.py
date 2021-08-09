import requests
import pytest


from API import ASR_config

def main(extid):
    response = requests.get(
        ASR_config.url_VLG_KIR_STR+extid+"/infoFinance"
        , params=ASR_config.params, headers=ASR_config.headers)
    return response

#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in ASR_config.extid_list_VLG_KIR_STR])
def test_200(extid,result):
    response = main(extid)
    assert response.status_code == result,response.json()
    print(response)
    print(extid)
    print(ASR_config.requestid())

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in ASR_config.extid_list_VLG_KIR_STR for param in ASR_config.params_list])
def test_date_200(extid,param):
    response = main(extid)
    assert response.status_code == 200,response.json()
    print(response)
    print(extid)
    print(ASR_config.requestid())
