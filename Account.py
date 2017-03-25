from RequestHandler import RequestHandler


class Account:


    def __init__(self, ):
        self.rh = RequestHandler()


    def get_accounts(self):

        return self.rh.get('accounts/prosper/')