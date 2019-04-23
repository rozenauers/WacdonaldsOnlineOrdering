# Written by XJ

from inventory import *
from restaurant_system import *
from order import *

class Main():

    def __init__(self, containers, contents, extra):
        self._containers = containers # refer to buns/wraps
        self._contents = contents # refer to patties
        self._extra = extra # refers to extra choices, list object

    def getprice(self):
        price = 0 + self._containers.price * self._containers.quantity + self._contents.price * self._contents.quantity
        for item in self._extra:
            price = price + item.price * item.quantity
        return price
        
    @property
    def containers(self):
        return self._containers

    @property
    def contents(self):
        return self._contents

    @property
    def extra(self):
        return self._extra

    def __str__(self):
        return f'{self.containers.name} {self.contents.name} {self.ingredients.name} for ${self.price}'

class Main_Component(): # components of main, eg: containers contents and ingredients

    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

class Other(): # sides and drinks

    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        ''' Important Notice:
            quantity measures the basic unit
            eg: 100mL juice -> quantity = 100
                3 nuggets -> quantity = 3'''

    def getprice(self):
        return self._price * self._quantity

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def __str__(self):
        return f'{self.quantity} {self.name} for ${self.getprice(price, quantity)}'
