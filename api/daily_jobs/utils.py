import os
import requests
from constants import *


def get_access_token():
    """ Get Bearer token for authentication """
    payload = {
        "grant_type": "client_credentials",
        "client_id": os.getenv('CLIENT_ID'),
        "client_secret": os.getenv('SECRET_KEY'),
        "scope": "api_offresdemploiv2 o2dsoffre"
    }

    params = {
        "realm": "/partenaire"
    }
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(AUTH_URL,headers=headers, data=payload, params=params)
    acces_token = response.json().get("access_token")
    if acces_token:
        return acces_token
    response.raise_for_status()




