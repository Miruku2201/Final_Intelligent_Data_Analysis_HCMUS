import requests
import json

class APICrawling:
    def __init__(self, params, API_KEY, API_URL):
        self.params = params
        self.API_KEY = API_KEY
        self.API_URL = API_URL

    def __call__(self):
        self.params["apikey"] = self.API_KEY
        return requests.get(self.API_URL, params=self.params).json()