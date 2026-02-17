import requests
from datetime import datetime
#¬¬¬¬CREATE USER ACCOUNT¬¬¬¬¬¬¬
TOKEN =";efkfepjgr-39gi402gkre"
USERNAME = "jada-tish"
GRAPH_ID = "graph1"
    
#get pixela endpint from pixela.com
pixela_endpoint = "https://pixe.la/v1/users"

#set user parameters (check the pixela API on their website)
user_params = {
    
    "token": ";efkfepjgr-39gi402gkre",
    "username" :"jada-tish" ,
    "agreeTermsOfService" : "yes" ,
    "notMinor" : "yes"
}
#post your request
#response = requests.post(url = pixela_endpoint, json =user_params)
#print(response.text)

#¬¬¬¬¬¬CREATING GRAPH DEFINITION ¬¬¬¬¬¬¬¬¬¬
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "hr",
    "type": "int",
    "color": "ajisai"
}
headers ={
    "X-USER-TOKEN":TOKEN
}

#response = requests.post(url = graph_endpoint , json = graph_config, headers = headers)
#print(response.text)

pixela_creation_endpoint =f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data ={
    "X-USER-TOKEN":TOKEN , 
    "date": "20251215",
    "quantity": "3"
}
print(today)
#response = requests.post(url = pixela_creation_endpoint ,json = pixel_data, headers = headers )
#print(response.text)












