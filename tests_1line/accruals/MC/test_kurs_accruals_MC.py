import requests
import pytest

import json
from API import params_config_date2
from API import MC_config

def main(extid,param):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/accruals?finAccountSysInst=UTK.ASH.KRS"
        , params=param, headers=MC_config.headers)
    return response



def t2():
    with open('extid_kurs_ASH.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums
#_____________________Тесты


@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_date_200(extid,param):
    response = main(extid,param)
    with open(r"./retest_kurs/accruals.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        file.write(c + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)
