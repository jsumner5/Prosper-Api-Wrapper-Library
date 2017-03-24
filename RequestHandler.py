import requests
import json


class RequestHandler:

    def __init__(self, access_token):
        self.access_token = access_token
        self.token_type = 'bearer'
        self.base_url = 'https://api.prosper.com/v1/'
        self.headers = { 'Authorization': "bearer " + self.access_token, 'Accept': "application/json" }

    def get(self, uri):
        uri = self.base_url+uri
        response = requests.get(uri, headers=self.headers)
        response = json.loads(response.text)
        return response['result']









