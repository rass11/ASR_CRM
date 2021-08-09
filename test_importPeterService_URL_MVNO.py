import requests
import pytest

import json
from API import ASR_config


headers = {
        'x-api-key': '6defbef3-e47c-4c34-a94a-2f9f359bfb5f',
           }
params = [
 {
        'dateStart': '2018-03-01T00:00:00+03:00',
        'dateEnd': '2021-03-01T23:59:59+03:00'
           }]

def main(extid):
    response = requests.get(
        "http://10.42.122.25/apiman-gateway/MRF-URL/nexign-integration-rest/1.0-test/v1/bis4crm-amdocs-rthq/customers/"+extid+"/calls?authtoken=AAADQQAAB8cK8y.xAUgpaq5NLQaOqX9_&dateStart=2018-03-01T00:00:00+03:00&dateEnd=2021-03-01T23:59:59+03:00"
        , headers=headers)
    return response



def t2():
    with open('extid_PS_URL.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open("data_MVNO_URL.txt", "a") as file:
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
