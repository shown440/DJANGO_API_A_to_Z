import requests
import json
import os



image_path = os.path.join(os.getcwd(), "slack-logo.png")

######################################################
#####  djangorestframework-jwt Authentication
######################################################

##################################################
### User login and jwt return both combindly
#################################################
AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"   #jwt/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

headers = {
    "Content-Type": "application/json"
}
data = {
    "username": "shifullah",  #shifullah", shown440
    "password": "admin-12345"
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# print(r.json())
token = r.json()["token"]
# print(token)


END_POINT = "http://127.0.0.1:8000/api/status/41/"
headers2 = {
    # "Content-Type": "application/json",
    "Authorization": "JWT " + token
}
data2 = {
    "content": "Newwwwwwwwwwwww Contentttttttttttttttttt Postttttttttt"  #shifullah", shown440
}
with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    r2 = requests.put(END_POINT, data=data2, headers=headers2, files=file_data)
    print(r2.text)



# ####################################################
# ### User create and jwt return both combindly
######################################################
# END_POINT = "http://127.0.0.1:8000/api/status/"
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"   #jwt/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
# # token1 = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InNoaWZ1bGxhaCIsImV4cCI6MTU3NDE1NjYwMiwiZW1haWwiOiJhaG1lZC5zaGlmdWxsYWhAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1NzQxNTYzMDJ9.HdcuWs6DsArlYL-8K3am4J1CAeC8FCSxRs8N-rMyGAs"
# headers = {
#     "content-type": "application/json",
#     # "Authorization": "JWT " + token1
#     "Authorization": "JWT " + "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo2MywidXNlcm5hbWUiOiJzaGlmdWxsYWg3IiwiZXhwIjoxNTc0Nzc0ODI3LCJlbWFpbCI6InNoaWZ1bGxhaDVAZ21haWwuY29tIiwib3JpZ19pYXQiOjE1NzQ3NzQ1Mjd9.qCtiC64bVJH_DMG5DcacabCB0EdRCSbTX4e9CqmBOn4"
# }
# data = {
#     "username": "shifullah8",  #shifullah", shown440
#     "email": "shifullah5@gmail.com",
#     "password": "admin-12345",
#     "password2": "admin-12345"

# }
# r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# # print(r.json())
# token = r.json()#["token"]
# print(token)
######################################################################################################

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
