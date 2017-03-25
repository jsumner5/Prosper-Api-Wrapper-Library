from RequestHandler import RequestHandler


class Loan:


    def __init__(self, ):
        self.rh = RequestHandler()


    def get_loans(self):
        loans = self.rh.get('loans/')
        return loans