import requests
import json

def is_json(json_data):
    try:
        real_data = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

END_POINT = "http://127.0.0.1:8000/api/status/"

# def do(method="get", data={}, id=13, is_json=True):
#     if is_json:
#         data = json.dumps(data)
#     r = requests.request(method, END_POINT+"?id="+str(id), data=data)
#     print(r.text)
#     return r

# do()
# do(data={"id": 13})

def do(method="get", data={}, is_json=True):
    headers = {}
    if is_json:
        headers["content-type"] = "application/json" 
        data = json.dumps(data)
    r = requests.request(method, END_POINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do()
# do(data={"id": 15})

do(method="delete", data={"id": 15})

# do(method="put", data={"id": 15, "content": "New Cooooooooooooooooooooooooooool update", "user":1})

# do(method="put", data={"content": "Cooooooooooooooooooooooooooool is coming sooooooooooooooon", "user":1})
