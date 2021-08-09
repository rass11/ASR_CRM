
from datetime import datetime

def requestid():
    time = datetime.now()

    requestid = time.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    requestid = requestid.replace(":", "")
    requestid = requestid.replace("-", "")
    requestid = requestid.replace(" ", "")
    requestid = requestid.replace("Dec", "")
    requestid = requestid.replace("Jan", "")
    requestid = requestid.replace("Feb", "")
    requestid = requestid.replace("(", "")
    requestid = requestid.replace(")", "")
    requestid = requestid.replace(".", "")
    return requestid

#extid_list_VLG_UDM_STR = ['5988816004','5988816004','5992883624','5980884835','5980885317']
extid_list_VLG_UDM_STR = ['5980885317','5980885317','5980885317','5980885317','5980885317']
extid_list_VLG_MRD_STR = ['3844662569','3834985487','3511994149','1237883208','1237838969','3440581661','3844648838']
extid_list_VLG_KIR_STR = ['2396272149','2169422292','2176738108','955200','62889276','865878','1784779','912898']
extid_list_VLG_BAS_STR = ['400000321852','400000322538','132021503','407276312249']
extid_list_SIB_TMS_STR = ['9706229','9706285','9694245','10109119','221239475475','220780899260','220780937621','220781038374']
extid_list_SIB_NSK_STR = ['114271046','133410','316927','335268','168708173','168708116','114592794']
extid_list_DSV_KAM_STR = ['209388','209393','1531042769','206107','174756','1608283318','1779462415','1838653183','1692951509','1713104554']


url_VLG_UDM_STR = 'http://sks06ap569.ks.rt.ru:8088/apiman-gateway/adapters/start-plsql-adapter-vlg-udm/1.0-test/v1/finAccounts/'
url_VLG_MRD_STR = 'http://apiman.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-mrd/1.0-test/v1/finAccounts/'
url_VLG_KIR_STR = 'http://apiman.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-kir/1.0-test/v1/finAccounts/'
url_VLG_BAS_STR = 'http://apiman.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-vlg-bas/1.0-test/v1/finAccounts/'
url_SIB_TMS_STR = 'http://apiman.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-sib-tms/1.0-test/v1/finAccounts/'
url_SIB_NSK_STR = 'http://apiman.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-sib-nsk/1.0-test/v1/finAccounts/'
url_DSV_KAM_STR = 'http://apiman.south.rt.ru/apiman-gateway/adapters/start-plsql-adapter-dsv-kam/1.0-test/v1/finAccounts/'



params = {
        'dateStart': '2018-03',
        'dateEnd': '2021-02',
           }

headers = {
        'x-api-key': '6defbef3-e47c-4c34-a94a-2f9f359bfb5f',
        'x-request-id': requestid()
           }


params_list = [
        {
        'dateStart': '2020-07',
        'dateEnd': '2021-01',
           },
        {
        'dateStart': '2020-11',
        'dateEnd': '2021-02',
           }
]

params_list_long = [
 {
        'dateStart': '2018-12',
        'dateEnd': '2019-01',
           },


 {
        'dateStart': '2018-12',
        'dateEnd': '2020-01',
           },

{
        'dateStart': '2018-12',
        'dateEnd': '2019-12',
           },


{
        'dateStart': '2020-03',
        'dateEnd': '2020-07',
           },

{
        'dateStart': '2019-07',
        'dateEnd': '2021-02',
           },

 {
        'dateStart': '2021-01',
        'dateEnd': '2021-02',
           },


{
        'dateStart': '2019-02',
        'dateEnd': '2020-11',
           },


{
        'dateStart': '2018-09',
        'dateEnd': '2020-08',
           },


{
        'dateStart': '2020-01',
        'dateEnd': '2020-02',
           },


 {
        'dateStart': '2020-12',
        'dateEnd': '2020-12',
           },


{
        'dateStart': '2019-12',
        'dateEnd': '2019-12',
           },

{
        'dateStart': '2021-01',
        'dateEnd': '2021-01',
           },

{
        'dateStart': '2018-06',
        'dateEnd': '2018-06',
           },

{
        'dateStart': '2020-03',
        'dateEnd': '2021-02',
           },

{
        'dateStart': '2018-12',
        'dateEnd': '2019-04',
           },

{
        'dateStart': '2020-11',
        'dateEnd': '2021-02',
           },

{
        'dateStart': '2020-09',
        'dateEnd': '2021-02',
           },

{
        'dateStart': '2020-12',
        'dateEnd': '2021-02',
           },

 {
        'dateStart': '2020-11',
        'dateEnd': '2021-02',
           },

{
        'dateStart': '2020-07',
        'dateEnd': '2021-01',
           }

]