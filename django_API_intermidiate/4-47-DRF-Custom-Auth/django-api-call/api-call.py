import requests
import json
import os



END_POINT = "http://127.0.0.1:8000/api/status/"

image_path = os.path.join(os.getcwd(), "slack-logo.png")


######################################################
#####  djangorestframework-jwt Authentication
######################################################

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"   #jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers = {
    "content-type": "application/json"
}
data = {
    "username": "shown440x",  #shifullah", shown440
    "password": "admin-12345"
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# print(r.json())
token = r.json()#["token"]
print(token)

# refresh_data = {
#     "token": token
# }
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# # print(r.json())
# new_token = new_response.json()["token"]
# print(new_token)

# headers = {
#     # "content-type": "application/json",
#     "Authorization": "JWT " + token
# }
# with open(image_path, 'rb') as image:
#     file_data = {
#         'image': image
#     }
#     # post_data = json.dumps({"content": "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"})
#     data = {
#         "content": "yyyyyyyyyyyyyyyyyyyyyyyyyy  zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
#     }
#     json_data = json.dumps(data)
#     # posted_response = requests.post(END_POINT, data=data, files=file_data, headers=headers)
#     # print(posted_response.text)
#     putted_response = requests.put(END_POINT+str(26)+"/", data=data, files=file_data, headers=headers)
#     print(putted_response.text)


######################################################
#####  Test GET and POST with session Authentication
######################################################

# get_endpoint = END_POINT + str(11)
# post_data = json.dumps({"content": "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"})

# r2 = requests.get(END_POINT)
# print(r2.status_code)

# r = requests.get(get_endpoint)
# print(r.text)

# post_headers = {
#     "content-type": "application/json"
# } 
# post_response = requests.post(END_POINT, data=post_data, headers=post_headers)
# print(post_response.text)


##################################
### Image upload/ POST method
##################################
def is_json(json_data):
    try:
        real_data = json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False
    return is_valid

image_path = os.path.join(os.getcwd(), "slack-logo.png")

def do_img(method="get", data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers["content-type"] = "application/json" 
        data = json.dumps(data)

    if img_path is not None:
        with open(img_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, END_POINT, data=data, files=file_data, headers=headers)  
    else:
        r = requests.request(method, END_POINT, data=data, headers=headers)

    print(r.text)
    print(r.status_code)
    return r

# do_img(method="post", data={"content": "yyyyyyyyyyyyy zzzzzzzzzzzzz", "user":1}, is_json=False, img_path=image_path)
# do_img(method="put", data={"id": 26, "content": "yzzzzzzzzz zyyyyyyyyyyyyyy", "user":1}, is_json=False, img_path=image_path)



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

# do(method="delete", data={"id": 15})

# do(method="put", data={"id": 15, "content": "New Cooooooooooooooooooooooooooool update", "user":1})

# do(method="put", data={"content": "Cooooooooooooooooooooooooooool is coming sooooooooooooooon", "user":1})
