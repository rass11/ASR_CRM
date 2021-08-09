import requests
import pytest
import json

from API import MC_config

def main(extid):
    response = requests.get(
        MC_config.url_MC+extid+"/final-payment?finAccountSysInst=UTK.ASH.KRS"
        , params=MC_config.params, headers=MC_config.headers)
    return response

def t2():
    with open('extid_kurs_ASH.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums

#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_200(extid,result):
    response = main(extid)
    with open(r"./retest_kurs/finalPayment.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()})
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)

