import requests
import json


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updatess/"

def get_list():

    r = requests.get(BASE_URL + ENDPOINT)
    status_code = r.status_code
    if status_code == 404:
        print("Page not found")
    else:
        data = r.json() 
        # print(type(data))
        id=1
        for obj in data:
            # print(obj)
            # print(id)
            if id == 5:
                r2 = requests.get(BASE_URL + ENDPOINT + str(id) + "/")
                print(r2.json())
            id = id+1
        return data

# print(get_list())
get_list()