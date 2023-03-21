import requests
from io import BytesIO


def summarize_text(yt_link, lang):
    url = 'http://127.0.0.1:8000/summarize'

    data = {"yt_link": yt_link, "lang": lang}
    response = requests.post(url, json=data)
    response_dict = response.json()
    return response_dict["content"], response_dict["summarization"]
