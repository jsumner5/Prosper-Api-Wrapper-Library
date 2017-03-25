import requests, json


class AccessTokenGenerator:

    def __init__(self):
        self.url = "https://api.prosper.com/v1/security/oauth/token"
        self.client_id = '82d07266e857441b8236d4c55897374d'
        self.client_secret = 'b94e584dd3704beab4e7c9fa9b07bbc2'
        self.username = 'jeroldsumner@gmail.com'
        self.password = 'Bigboytim321!'

    def generate_token(self):
        payload = "grant_type=password&client_id=" + self.client_id + "&client_secret="+ self.client_secret + "&username="+ self.username +"&password="+ self.password
        headers = { 'accept': "application/json", 'content-type': "application/x-www-form-urlencoded" }
        response = requests.request("POST", self.url, data=payload, headers=headers)
        f = open('token','w')
        f.write(response.text)
        f.close()
        print(response.text)


    def refresh_token(self):

        refresh_token = self.get_refresh_token()
        url = "https://api.prosper.com/v1/security/oauth/token"
        payload = "grant_type=refresh_token&client_id=" + self.client_id + "&client_secret=" + self.client_secret + "&refresh_token=" + refresh_token
        headers = {'accept': "application/json", 'content-type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers)
        f = open('token', 'w')
        f.write(response.text)
        f.close()
        print(response.text)

    def get_refresh_token(self):
        f = open('token', 'r')
        tok = json.loads(f.read())
        return tok['refresh_token']