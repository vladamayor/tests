import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import requests


def search_russia_city(geo_logs):

    rus_list = [el for el in geo_logs if 'Россия' in list(el.values())[0]]

    return rus_list


def search_unic_uds(ids):

    unic_ids = []
    for el in list(ids.values()):
        for e in el:
            if e not in unic_ids:
                unic_ids.append(e)

    return unic_ids


def search_max_sales_volume(stats):

    for el in stats.items():
        if  max(stats.values()) in el:
            return el[0]
        

def create_folder(folder):
    base_host = 'https://cloud-api.yandex.net/'
    token = os.getenv('TOKEN')
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {token}'
    }
    uri = 'v1/disk/resources'
    requests_url = base_host + uri
    params = {'path' : folder}
    response_create = requests.put(requests_url, params=params, headers=headers)
    response_get = requests.get(requests_url, params=params, headers=headers)
    return response_create, response_get