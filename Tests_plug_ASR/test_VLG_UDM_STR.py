import requests
import pytest


from API import Plug_config



#_____________________Тесты
def main(extid):
    response = requests.get(Plug_config.url_VLG_UDM_STR+extid+"/infoFinance"
        ,params=Plug_config.params, headers=Plug_config.headers)
    return response


@pytest.mark.parametrize("extid, result",[(ext,200) for ext in Plug_config.extid_list_VLG_UDM_STR])
def test_200(extid,result):
    response = main(extid)
    assert response.status_code == result
    print(response)
    print(extid)
    print(Plug_config.requestid())

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in Plug_config.extid_list_VLG_UDM_STR for param in Plug_config.params_list_long])
def test_date_200(extid,param):
    response = main(extid)
    assert response.status_code == 200,response.json()
    print("_______________")
    print(response)
    print(extid)
    print(Plug_config.requestid())
