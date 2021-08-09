
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

stand = 'dev'

url_MC_receivable = 'http://10.42.122.25/apiman-gateway/p1l/accounts-receivable/1.0-'+stand+'/v1/finAccounts/'
url_MC_promise_payment = 'http://10.42.122.25/apiman-gateway/p1l/accounts-promise-payment/1.0-test/v1/finAccounts/finAccountNumber/'
url_MC_final = 'http://10.42.122.25/apiman-gateway/p1l/final-payment/1.0-'+stand+'/v1/finAccounts/'
url_MC_oif = 'http://10.42.122.25/apiman-gateway/p1l/obtaining-information-finance/1.0-'+stand+'/v1/finAccounts/'
url_MC_detalization = 'http://10.42.122.25/apiman-gateway/p1l/detalization/1.0-'+stand+'/v1/finAccounts/'




params = {
        'dateStart': '2018-03',
        'dateEnd': '2021-02',
           }

headers = {
        'x-api-key': '0a060e3a-86dd-41cb-9748-be71802109c6',
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