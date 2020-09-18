import json
import requests

from settings import *

def request_summary_api(input_text):
    post_json = {
        "text": input_text
    }

    response = requests.post(SUMMARY_SERVICE_API, data=json.dumps(post_json))
    try:
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(e)
        return None


def request_emotion_api(input_text):
    post_json = {
        "text": input_text
    }

    response = requests.post(EMOTION_ANALYSIS_API, data=json.dumps(post_json))
    try:
        response.raise_for_status()
        response_dict = response.json()
        return response_dict["pos_num"], response_dict["neg_num"], response_dict["bias"]
    except Exception as e:
        print(e)
        return None
