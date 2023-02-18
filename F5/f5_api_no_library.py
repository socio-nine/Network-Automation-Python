# https://loadbalancing.se/f5-rest-api-getting-started/

import requests, json

username = 'admin'
password = 'eve'
ltm = '10.100.116.200'

body = {
    "username": username,
    "password": password,
    "loginProviderName": "tmos"
}

token_response = requests.post(
    f'https://{ltm}/mgmt/shared/authn/login',
    verify=False,
    auth=(username, password),json=body)\
    .json()

token = token_response['token']['token']

headers = {
    "X-F5-Auth-Token": token
}

pools = requests.get(
    f'https://{ltm}/mgmt/tm/ltm/pool',
    headers=headers,
    verify=False).json()


requests.post(
   f'https://{ltm}/mgmt/tm/ltm/node',
   headers=headers,
   json={"name":"myNode","address":"10.1.1.1"}
)