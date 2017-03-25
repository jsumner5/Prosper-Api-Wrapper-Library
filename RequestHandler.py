import requests
import json
from AccessTokenGenerator import AccessTokenGenerator


class RequestHandler:

    def __init__(self):

        self.access_token = self.get_access_token()
        self.token_type = 'bearer'
        self.base_url = 'https://api.prosper.com/v1/'
        self.headers = { 'Authorization': "bearer " + self.access_token, 'Accept': "application/json" }

    def get(self, uri):
        uri = self.base_url+uri
        response = requests.get(uri, headers=self.headers)
        response = json.loads(response.text)
        print("|| Request handler request-> " + uri)
        if ('message' in response):
            token_gen = AccessTokenGenerator()
            token_gen.refresh_token()
        else:
            return response



    def get_access_token(self):

        f = open('token', 'r')
        tok = json.loads(f.read())
        return tok['access_token']





