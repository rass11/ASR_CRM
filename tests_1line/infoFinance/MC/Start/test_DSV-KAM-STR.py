import requests
import pytest


from API import MC_config

def main(extid):
    response = requests.get(
        MC_config.url_MC+extid+"/infoFinance?finAccountSysInst=DSV.KAM.STR"
        , params=MC_config.params, headers=MC_config.headers)
    return response

#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in MC_config.extid_list_DSV_KAM_STR])
def test_200(extid,result):
    response = main(extid)
    assert response.status_code == result,response.json()
    print(response)
    print(extid)
    print(MC_config.requestid())

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in MC_config.extid_list_DSV_KAM_STR for param in MC_config.params_list_long])
def test_date_200(extid,param):
    response = main(extid)
    assert response.status_code == 200,response.json()
    print(response)
    print(extid)
    print(MC_config.requestid())

def test_json():
    response = main()
    assert response.status_code == 200,response.json()