import requests
import json


BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/updates/"

# GET data
def get_list():

    r = requests.get(BASE_URL + ENDPOINT)
    status_code = r.status_code
    print(r.status_code)
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


# POST data
def create_update():
    new_data = {
        'user': 1,
        'content': 'AAAAAAAAAAAAAAAAAAAAAAAA'
    }
    r = requests.post(BASE_URL + ENDPOINT, data=json.dumps(new_data))

    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text
# print(create_update())


# UPDATE data
def do_obj_update():
    new_data = {
        # 'content': 'Django + React is great combination for WEB Development'
        'content': 'BBBBBBBBBBBBBB'
    }
    r = requests.put(BASE_URL + ENDPOINT + "12" + "/", data=json.dumps(new_data)) # json.dumps(new_data))

    # new_data = {
    #     'id': 10,
    #     'content': 'Django is great content for WEB Development'
    # }
    # r = requests.put(BASE_URL + ENDPOINT, data=new_data)

    # print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text
# print(do_obj_update())


# DELETE data
def delete():
    new_data = {
        'user': 1,
        'content': 'another new cool update'
    }
    r = requests.delete(BASE_URL + ENDPOINT + "13" + "/") # , data=json.dumps(new_data)
    # r = requests.delete(BASE_URL + ENDPOINT, data=new_data)

    print(r.headers)
    print(r.status_code)
    if r.status_code == requests.codes.ok:
        # print(r.json())
        return r.json()
    return r.text
print(delete())

