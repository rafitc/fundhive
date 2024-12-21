
import requests
from dotenv import dotenv_values
config = dotenv_values(".env")


def get_master_data():
    url = f"{config['RAPIDAPI_URL']}/master"

    querystring = { "AMC_Code": "HDFC", "RTA_Agent_Code": "CAMS" }

    headers = {
        "x-rapidapi-key": config['RAPIDAPI_KEY'],
        "x-rapidapi-host": config['RAPIDAPI_HOST']
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())