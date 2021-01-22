
class Product:
    '''
    Class to represent a product consisting of name, quant and price
    '''
    def __init__(self, name, quant, price):
        '''
        :param name:
        :param quant:
        :param price:
        '''
        self.name = name
        self.quant = quant
        self.price = price

    def cost(self):
        '''
        returns cost of the product
        :return: int of cost
        '''
        return self.quant * self.price

    def sell(self, sold_quantity):
        '''
        sell few units of the product
        :param sold_quantity:
        '''
        self.quant = self.quant - sold_quantity

