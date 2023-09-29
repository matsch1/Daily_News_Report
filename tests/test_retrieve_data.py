from daily_news_report.src.retrieve_data import retreive_news
import pytest


def test_function_runs() -> None:
    news = retreive_news()
    assert len(news['articles']) > 1
