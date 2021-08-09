import requests
import pytest

import json

from API import ASR_config

def main(extid):
    response = requests.get(
        ASR_config.url_VLG_CHV_STR+extid+"/final-payment"
        , headers=ASR_config.headers)
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
    with open("data_finalPayment_VLG_CHV_0408.txt", "a") as file:
        #r=response.json()
        #r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        file.write(c + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())

