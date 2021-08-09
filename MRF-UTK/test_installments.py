import requests
import pytest
import time
import json

from API import ASR_config

import html.parser
headers = {
        'x-api-key': '6defbef3-e47c-4c34-a94a-2f9f359bfb5f',
           }




def main(extid):
    xml = '<?xml version="1.0" encoding="utf-8"?><soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"><soap-env:Body><ns0:getInstalmentPaymentsRSO3Request xmlns:ns0="http://south.rt.ru/WsProvider/"><ExternalAccountId>'+extid+'</ExternalAccountId><InstalmentClosed>false</InstalmentClosed></ns0:getInstalmentPaymentsRSO3Request></soap-env:Body></soap-env:Envelope>'

    response = requests.post(
        "http://10.42.122.25/apiman-gateway/MRF-UTK/kurs-soap/1.0-test"
        , headers=headers,auth=('crm_b2c_tz', 'crm_b2c_tz#'),data=xml)
    return response



def t2():
    with open('extid_UG_PSI.txt', 'r') as f:
        nums = f.read().splitlines()
    print(nums)
    return nums

#_____________________Тесты

@pytest.mark.parametrize("extid, result",[(ext,200) for ext in t2()])
def test_import_200(extid,result):
    response = main(extid)
    with open(r"./data/STUB_jmeter/MRF_UTK_installments.txt", "a",encoding='utf-8') as file:
        #r=response.json()
        #r2 = r[1:0]
        r = response.text
        r = html.parser.HTMLParser().unescape(r)
        xml = r.replace('"',r'\"')
        xml = " ".join(xml.split())
        file.write('"'+extid+'" : '+'"'+xml+'",')
        file.write('\n')
        time.sleep(0.3)
    # assert response.status_code == result
    print(response)
    print(extid)
    print(ASR_config.requestid())

