import requests
import json

class TinyURL:
    def shorten_url(self, url):
        self.url = url
        self.api_token = 'mr9Erv6cevg4bLXHmrtsuGtdRHitEKoIA2zHkrQek56qpPoGklUZCpm4vqH2'
        self.base_url = 'https://api.tinyurl.com/create'
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        payload = {'url': self.url}
        url_with_token = f'{self.base_url}?api_token={self.api_token}'

        response = requests.post(url_with_token, headers=self.headers, json=payload)

        if response.status_code == 200:
            json_data = response.json()
            tiny_url = json_data['data']['tiny_url']
            return tiny_url
        else:
            print('Error: Request failed')
            return None
