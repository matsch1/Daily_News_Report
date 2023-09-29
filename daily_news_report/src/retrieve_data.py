import requests
import os
import pprint
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()


class APICollector():
    def __init__(self) -> None:
        newsapi_news_collector = NEWSAPI_NewsCollector()

        self.news_json = concatinate_news(
            [newsapi_news_collector.get_news_json()])

    def get_news_json(self):
        return self.news_json


class NEWSAPI_NewsCollector():
    def __init__(self) -> None:
        general_news = self._retreive_general_news()

        self.news_json = concatinate_news([general_news])

    def get_news_json(self):
        return self.news_json

    def _retreive_general_news(self):
        url = 'https://newsapi.org/v2/everything?'
        parameters = {
            'q': '-Wetter OR -Musik OR -Verkehr OR -Fußball OR -Kommunen OR -heise+ OR -Spiel',  # query phrase
            'pageSize': 20,  # maximum is 100
            'apiKey': os.getenv("NEWSAPI_API_KEY"),  # your own API key
            'sortBy': 'popularity',
            # 'from': datetime.now().date(), 'to': datetime.now().date(),
            'from': datetime.now().date()-timedelta(days=1), 'to': datetime.now().date(),
            'language': 'de',
            'domains': 'heise.de,stern.de,zeit.de,tagesschau.de',
            'excludeDomains': 'welt.de,waz.de'
        }
        response = requests.get(url, params=parameters)

        response_json = response.json()
        # pprint.pprint(response_json)

        return response_json


def retreive_news():
    api_collector = APICollector()

    return api_collector.get_news_json()


def concatinate_news(json_list):
    return json_list[0]  # first catch for only one news source
