import requests
import _json


url = "https://apiman.south.rt.ru/apiman-gateway/p1l/obtaining-information-finance/1.0-dev/v1/infoFinance"

params = {
        'dateStart': '2020-08',
        'dateEnd': '2020-08',
        'key': 'cs1'
           }

headers = {
        'x-api-key': '0a060e3a-86dd-41cb-9748-be71802109c6'
           }

class CalcApi():


    def response_get(self):
        response = requests.get(url, params=params, headers=headers)
        return response

    def resonseBody_get(self):
        response = requests.get(url, params=params, headers=headers)
        response_body = response.json()
        return response_body
