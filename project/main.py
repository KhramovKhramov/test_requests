import json

import httpx
import urlextract
from fake_headers import Headers


def request_urls(urls: list[str]) -> json:
    responces = {}
    extractor = urlextract.URLExtract()
    methods = ['get', 'options', 'post', 'put', 'delete', 'patch', 'head']
    try:
        for url in urls:
            is_url = extractor.find_urls(url)
            if is_url:
                for method in methods:
                    responces.setdefault(url, {})
                    headers = Headers(headers=True).generate()
                    try:
                        request = httpx.request(method, url, headers=headers)
                        if request.status_code != 405:
                            responces[url][method.upper()] = request.status_code
                    except (httpx.ReadTimeout, httpx.RequestError):
                        print(f'При запросе адреса {url} произошла ошибка')
            else:
                print(f'Cтрока {url!r} не является ссылкой')
    except TypeError:
        return 'Введите множество строк'
    print(responces)
    return json.dumps(responces, indent=4)


if __name__ == '__main__':
    urls = ['http://www.example.com',
            'Я просто строка']
    print(request_urls(urls))
