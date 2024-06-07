import requests
import os
from dotenv import load_dotenv

load_dotenv()

BACKEND_URL = os.getenv('backend_url', default="http://localhost:3030")
SENTIMENT_ANALYZER_URL = os.getenv(
    'sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{BACKEND_URL}{endpoint}?{params}"

    print(f"GET from {request_url} ")
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e=}")
        return {"error": "h"}


def analyze_review_sentiments(text):
    request_url = f"{SENTIMENT_ANALYZER_URL}analyze/{text}"
    try:
        response = requests.get(request_url)
        print(f"\n{response}\n")
        return response.json()
    except Exception as e:
        print(f"Unexpected error: {e=}, {type(e)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = f"{BACKEND_URL}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e=}")
