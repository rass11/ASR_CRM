import requests
import pytest

from API import ASR_config
import json


def main(extid):
    response = requests.get("http://apiman.south.rt.ru/apiman-gateway/adapters/kurs-soap-adapter/1.0-dev/v1/finAccounts/"+extid+"/receivable"
   ,headers=ASR_config.headers)
    return response


def t2():
    with open('tests_parse/KURS/extid_receivable.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums


@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open("tests_parse/KURS/receivable.txt", "a") as file:
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