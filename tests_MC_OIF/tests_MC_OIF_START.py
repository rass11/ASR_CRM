import io
import requests
import pytest

from jsonschema import validate,ValidationError
import json

from API import params_config_date2
from API import params_config_date4
from API import MC_config

SysInst = "VLG.CHV.STR"



def main_instalments(extid):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/instalments?finAccountSysInst="+SysInst
        , headers=MC_config.headers)
    return response


def main_accruals(extid,param):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/accruals?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00"
        , params=param, headers=MC_config.headers)
    return response


def main_payments(extid,param):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/payments?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00"
        , params=param, headers=MC_config.headers)
    return response


def main_penalties(extid,param):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/penalties?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00"
        , params=param, headers=MC_config.headers)
    return response


def main_calculations(extid,param):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/infoFinance?finAccountSysInst="+SysInst
        , params=param, headers=MC_config.headers)
    return response

def main_shortFinance(extid):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/shortFinance?finAccountSysInst="+SysInst
        , headers=MC_config.headers)
    return response


def t2():
    with open('extid_VLG_CHV_psi.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums

#_____________________Тесты



@pytest.mark.parametrize("extid, result", [(ext, 200) for ext in t2()])
def test_shortFinance(extid, result):
    response = main_shortFinance(extid)
    with open(r"./MC_OIF/shortFinance.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    assert response.status_code == 200
    print(response)
    print(extid)


@pytest.mark.parametrize("extid, result", [(ext, 200) for ext in t2()])
def test_instalments(extid, result):
    response = main_instalments(extid)
    with open(r"./MC_OIF/instalments.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    assert response.status_code == 200
    print(response)
    print(extid)

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_accruals(extid,param):
    response = main_accruals(extid,param)
    with open(r"./MC_OIF/accruals.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(c + params + b + ',')
        file.write('\n')
    assert response.status_code == 200
    print(response)
    print(extid)


@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_payments(extid,param):
    response = main_payments(extid,param)
    with open(r"./MC_OIF/payments.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(c + params + b + ',')
        file.write('\n')
    assert response.status_code == 200
    print(response)
    print(extid)



@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_penalties(extid,param):
    with io.open('schema_peni_kurs_null.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main_penalties(extid,param)
    with open(r"./MC_OIF/penalties.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        err_message = ''
        response_sch = response.json()
        try:
            validate(instance=response_sch, schema=schema)

        except ValidationError as er:
            err_message = '!' * 10 + 'ERROR' + '!' * 10 + er.message
        # else:
        # response = response.json()

        a = json.dumps({extid: (err_message or response_sch)}, ensure_ascii=False)
        b = a[1:-1]
        time = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(time + params + b + ',')
        file.write('\n')
    assert response.status_code == 200
    print(response)
    print(extid)

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_calculations(extid,param):
    with io.open('schema_calculations_kurs.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main_calculations(extid,param)
    with open(r"./MC_OIF/calculations.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        err_message = ''
        response_sch = response.json()
        try:
            validate(instance=response_sch, schema=schema)

        except ValidationError as er:
            err_message = '!' * 10 + 'ERROR' + '!' * 10 + er.message
        # else:
        # response = response.json()

        a = json.dumps({extid: (err_message or response_sch)}, ensure_ascii=False)
        b = a[1:-1]
        time = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(time + params + b + ',')
        file.write('\n')
    assert response.status_code == 200
    print(response)
    print(extid)


