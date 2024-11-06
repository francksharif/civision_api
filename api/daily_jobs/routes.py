import requests 
from constants import *
from api.daily_jobs.utils import *
from datetime import datetime
from . import jobs 


@jobs.route('/', methods=['GET'])
def daily_job_offers():
    """ Serve the daily job offers according to current date """
    current_date = datetime.now().strftime("%Y-%m-%d")
    querystring = {"minCreationDate":f"{current_date}T00:00:01Z","maxCreationDate":f"{current_date}T23:59:59Z"}

    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Accept": "application/json"
    }

    response = requests.get(API_URL, headers=headers, params=querystring)
    if response.request:
        data = response.json()
        return {"resultats": data['resultats']}
    return response.raise_for_status