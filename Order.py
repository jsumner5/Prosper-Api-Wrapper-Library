from RequestHandler import RequestHandler


class Order:


    def __init__(self, ):
        self.rh = RequestHandler()


    def get_orders(self):
        orders = self.rh.get('orders/')
        return orders

    def get_orders_by_id(self, order_id):
        order = self.rh.get('orders/' + order_id)
        return order