import requests
import pytest
import time
import html.parser
import xml.sax.saxutils as saxutils
import json

from API import params_config_STUB
from API import ASR_config


headers = {
        'x-api-key': '6defbef3-e47c-4c34-a94a-2f9f359bfb5f',
           }




def main(extid,param):
    xml = '<?xml version="1.0" encoding="utf-8"?><soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"><soap-env:Body><ns0:getAccountPaymentsDetailedRequest xmlns:ns0="http://south.rt.ru/WsProvider/"><PersonalAccountId>'+extid+'</PersonalAccountId><DateStart>'+param["dateStart"]+'</DateStart><DateEnd>'+param["dateEnd"]+'</DateEnd><TypeGroup>NO</TypeGroup></ns0:getAccountPaymentsDetailedRequest></soap-env:Body></soap-env:Envelope>'

    response = requests.post(
        "http://10.42.122.25/apiman-gateway/MRF-UTK/kurs-soap/1.0-test"
        , headers=headers,auth=('crm_b2c_tz', 'crm_b2c_tz#'),data=xml)
    return response
    return param



def t2():
    with open('extid_UG_PSI.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums

#_____________________Тесты

@pytest.mark.parametrize("extid, param",[(ext,param) for ext in t2() for param in params_config_STUB.params_date1])
def test_date_200(extid,param):
    response = main(extid,param)
    with open(r"./data/STUB_jmeter/MRF_UTK_payments.txt", "a") as file:
        r = response.text
        r = html.parser.HTMLParser().unescape(r)
        xml = r.replace('"',r'\"')
        xml = " ".join(xml.split())
        file.write('"'+extid+'/'+param["dateStart"][0:-18]+'/'+param["dateEnd"][0:-18]+'" : '+'"'+xml+'",')
        file.write('\n')
        time.sleep(0.3)
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())

