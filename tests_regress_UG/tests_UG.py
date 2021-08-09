import io
import requests
import pytest

from jsonschema import validate,ValidationError
import json

from API import params_config_date2
from API import params_config_date4
from API import MC_config

SysInst = "UTK.ASH.KRS"

def main_finalpayment(extid):
    response = requests.get(
        MC_config.url_MC_final+extid+"/final-payment?finAccountSysInst="+SysInst
        , params=MC_config.params, headers=MC_config.headers)
    return response

def main_receivable(extid):
    response = requests.get(
        MC_config.url_MC_receivable+extid+"/receivable?finAccountSysInst="+SysInst
        , params=MC_config.params, headers=MC_config.headers)
    return response

def main_instalments(extid):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/instalments?finAccountSysInst="+SysInst
        , params=MC_config.params, headers=MC_config.headers)
    return response

def main_promise_payment(extid):
    response = requests.get(
        MC_config.url_MC_promise_payment+extid+"/promise-payment?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00&contactId=__"
        , params=MC_config.params, headers=MC_config.headers)
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

def main_ContentInformation(faid,param):
    response = requests.get(
        MC_config.url_MC_detalization+faid+"/ContentInformation?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00&finAccountNumber="+faid
        , params=param, headers=MC_config.headers)
    return response


def main_mvno_fix(extid,param):
    response = requests.get(
        MC_config.url_MC_detalization+extid+"/detalization/mvno-fix?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00"
        , params=param, headers=MC_config.headers)
    return response

def main_promise_payment_history(extid,param):
    response = requests.get(
        MC_config.url_MC_promise_payment+extid+"/promise-payment-history?finAccountSysInst="+SysInst+"&finAccountTZ=%2B03:00&contactId=__"
        , params=param, headers=MC_config.headers)
    return response

def main_calculations(extid,param):
    response = requests.get(
        MC_config.url_MC_oif+extid+"/infoFinance?finAccountSysInst="+SysInst
        , params=param, headers=MC_config.headers)
    return response


def t2():
    with open('extid_UG_PSI.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums


def fa_id():
    with open('fa_id_UG_PSI.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums

#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_finalpayment(extid,result):
    response = main_finalpayment(extid)
    with open(r"./regress/finalPayment.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_receivable(extid,result):
    response = main_receivable(extid)
    with open(r"./regress/receivable.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)

@pytest.mark.parametrize("extid, result", [(ext, 200) for ext in t2()])
def test_instalments(extid, result):
    response = main_instalments(extid)
    with open(r"./regress/instalments.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)

@pytest.mark.parametrize("extid, result", [(ext, 200) for ext in fa_id()])
def test_promise_payment(extid, result):
    response = main_promise_payment(extid)
    with open(r"./regress/promise-payment.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()})
        b = a[1:-1]
        file.write(b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)




@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date4.params_date])
def test_promise_payment_history(extid,param):
    response = main_promise_payment_history(extid,param)
    with open(r"./regress/promise_payment_history.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(c + params + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)


@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_accruals(extid,param):
    response = main_accruals(extid,param)
    with open(r"./regress/accruals.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(c + params + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)


@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_payments(extid,param):
    response = main_payments(extid,param)
    with open(r"./regress/payments.txt", "a") as file:
        # r=response.json()
        # r2 = r[1:0]
        a = json.dumps({extid: response.json()}, ensure_ascii=False)
        b = a[1:-1]
        c = str(response.elapsed.total_seconds())
        params = json.dumps(param)
        file.write(c + params + b + ',')
        file.write('\n')
    # assert response.status_code == result
    print(response)
    print(extid)



@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_penalties(extid,param):
    with io.open('schema_peni_kurs_null.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main_penalties(extid,param)
    with open(r"./regress/penalties.txt", "a") as file:
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
        # assert response.status_code == result
    print(response)
    print(extid)

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
def test_calculations(extid,param):
    with io.open('schema_calculations_kurs.txt', encoding='utf-8') as data_file:
        schema = json.load(data_file)

    response = main_calculations(extid,param)
    with open(r"./regress/calculations.txt", "a") as file:
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
        # assert response.status_code == result
    print(response)
    print(extid)


@pytest.mark.parametrize("faid, param",[(ext,param) for ext in fa_id() for param in params_config_date2.params_date])
def test_ContentInformation(faid,param):
     response = main_ContentInformation(faid,param)
     with open(r"./regress/ContentInformation.txt", "a") as file:
         # r=response.json()
         # r2 = r[1:0]
         a = json.dumps({faid: response.json()}, ensure_ascii=False)
         b = a[1:-1]
         c = str(response.elapsed.total_seconds())
         file.write(c + b + ',')
         file.write('\n')
     # assert response.status_code == result
     print(response)
     print(faid)



# @pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_date2.params_date])
# def test_mvno_fix(extid,param):
#     response = main_mvno_fix(extid,param)
#     with open(r"./regress/mvno-fix.txt", "a") as file:
#         # r=response.json()
#         # r2 = r[1:0]
#         a = json.dumps({extid: response.json()}, ensure_ascii=False)
#         b = a[1:-1]
#         c = str(response.elapsed.total_seconds())
#         file.write(c + b + ',')
#         file.write('\n')
#     # assert response.status_code == result
#     print(response)
#     print(extid)