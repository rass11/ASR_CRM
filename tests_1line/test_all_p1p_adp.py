import requests
import pytest

import json
from API import ASR_config


headers_adp = {
        'x-api-key': '6defbef3-e47c-4c34-a94a-2f9f359bfb5f',
        'x-request-id': ASR_config.requestid()
           }


extid_VLG_UDM_STR ='5988816004'
extid_VLG_MRD_STR = '3834985487'
extid_VLG_KIR_STR ='2176738108'
extid_VLG_BAS_STR = '400000322538'
extid_SIB_TMS_STR = '10109119'
extid_SIB_NSK_STR = '335268'
extid_DSV_KAM_STR = '174756'


extid_UTK_ASH_KRS = '851930404487243'
extid_UTK_RST_KRS = '863930019279366'

extid_SZT_ALL_BIS = '205049'


url_ADP_VLG_UDM_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-udm/1.0-test/v1/finAccounts/'
url_ADP_VLG_MRD_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-mrd/1.0-test/v1/finAccounts/'
url_ADP_VLG_KIR_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-kir/1.0-test/v1/finAccounts/'
url_ADP_VLG_BAS_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-bas/1.0-test/v1/finAccounts/'
url_ADP_SIB_TMS_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-sib-tms/1.0-test/v1/finAccounts/'
url_ADP_SIB_NSK_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-sib-nsk/1.0-test/v1/finAccounts/'
url_ADP_DSV_KAM_STR = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-dsv-kam/1.0-test/v1/finAccounts/'

url_ADP_UG = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/kurs-soap-adapter/1.0-test/v1/finAccounts'


url_ADP_PeterService = 'http://crm-test-lb.south.rt.ru/apiman-gateway/adapters/nexign-rest-adapter-sz/1.0-test/v1/finAccounts'




def test_STR_ADP_infoFinance_VLG_UDM_STR():
    response = requests.get(
        url_ADP_VLG_UDM_STR+extid_VLG_UDM_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_VLG_UDM_STR)
    print(ASR_config.requestid())

def test_STR_ADP_infoFinance_VLG_MRD_STR():
    response = requests.get(
        url_ADP_VLG_MRD_STR+extid_VLG_MRD_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_VLG_MRD_STR)
    print(ASR_config.requestid())


def test_STR_ADP_infoFinance_VLG_KIR_STR():
    response = requests.get(
        url_ADP_VLG_KIR_STR+extid_VLG_KIR_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_VLG_KIR_STR)
    print(ASR_config.requestid())

def test_STR_ADP_infoFinance_VLG_BAS_STR():
    response = requests.get(
        url_ADP_VLG_BAS_STR+extid_VLG_BAS_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_VLG_BAS_STR)
    print(ASR_config.requestid())


def test_STR_ADP_infoFinance_SIB_TMS_STR():
    response = requests.get(
        url_ADP_SIB_TMS_STR+extid_SIB_TMS_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_SIB_TMS_STR)
    print(ASR_config.requestid())


def test_STR_ADP_infoFinance_SIB_NSK_STR():
    response = requests.get(
        url_ADP_SIB_NSK_STR+extid_SIB_NSK_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_SIB_NSK_STR)
    print(ASR_config.requestid())


def test_STR_ADP_infoFinance_DSV_KAM_STR():
    response = requests.get(
        url_ADP_DSV_KAM_STR+extid_DSV_KAM_STR+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_DSV_KAM_STR)
    print(ASR_config.requestid())



##############КУРС

def test_KURS_ADP_infoFinance_UTK_ASH_KRS():
    response = requests.get(
        url_ADP_UG+extid_UTK_ASH_KRS+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_UTK_ASH_KRS)
    print(ASR_config.requestid())


def test_KURS_ADP_infoFinance_UTK_RST_KRS():
    response = requests.get(
        url_ADP_UG+extid_UTK_RST_KRS+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_UTK_RST_KRS)
    print(ASR_config.requestid())


    #####ПетерСервис


def test_PeterService_ADP_infoFinance_SZT_ALL_BIS():
    response = requests.get(
        url_ADP_PeterService+extid_SZT_ALL_BIS+"/infoFinance?dateStart=2018-09&dateEnd=2021-03"
        , headers=headers_adp)
    assert response.status_code == 200, response.json()
    print(response)
    print(extid_SZT_ALL_BIS)
    print(ASR_config.requestid())

    #Краткая
 #################################################################################
#################################################################################
#################################################################################
#################################################################################


