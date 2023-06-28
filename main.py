import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
user = "tamunorr"
toke = "ajjsjdiaiid"
user_params = {
    "token":toke,
    "username": user,
    "agreeTermsOfservice": "yes",
    "notMinor": "yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint= f"{pixela_endpoint}/{user}/graphs"

graph_id = "graph1"
graph_config = {
    "id":graph_id,
    "name":"my coding Graph",
    "unit": "S",
    "type": "float",
    "color": "sora"
}
header = {
    "X-USER-TOKEN": toke
}

#https://pixe.la/v1/users/tamunorr/graphs/graph1.html
# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_create = f"{pixela_endpoint}/{user}/graphs/{graph_id}"

today = datetime.now()

pixel_data = {
    "date": "20230627",
    "quantity": "10000",
}
#
response = requests.post(url=pixel_create, json=pixel_data, headers=header)
print(response.text)