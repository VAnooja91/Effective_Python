from typedproperty import typedproperty


class Product:
    '''
    Class to represent a product consisting of name, quant and price
    '''

    name = typedproperty('name', str)
    quant = typedproperty('quant', int)
    price = typedproperty('price', float)

    # __slots__ = ('name', '_quant', 'price')

    def __init__(self, name, quant, price):
        '''
        :param name:
        :param quant:
        :param price:
        '''
        self.name = name
        self.quant = quant
        self.price = price

    def __repr__(self):
        return f'Product({self.name!r}, {self.quant}, {self.price!r})'

    @property
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


