import json

from project.main import request_urls
import pytest


def test_not_found_urls():
    urls = ['Я просто строка']
    assert request_urls(urls) == '{}'


def test_not_str():
    urls = 1
    assert request_urls(urls) == 'Введите множество строк'


def test_url():
    urls = ['https://httpbin.org/']
    assert request_urls(urls) == json.dumps(
        {'https://httpbin.org/': {'GET': 200, 'OPTIONS': 200, 'HEAD': 200}},
        indent=4)
