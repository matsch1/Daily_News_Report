from daily_news_report.src.retrieve_data import retreive_news, NEWSAPI_NewsCollector
import pytest

# @pytest.fixture
# def NEWSAPI_NewsCollector() -> NEWSAPI_NewsCollector:
#     return NEWSAPI_NewsCollector()

def test_if_API_keys_exist() -> None:
    news_collector = NEWSAPI_NewsCollector()
    api_key_exist = news_collector._check_if_API_key_exists()
    assert api_key_exist
    
def test_retrieve_news_collect_data() -> None:
    news = retreive_news()
    assert len(news['articles']) > 1
