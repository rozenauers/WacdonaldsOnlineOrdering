from food import *
from restaurant_system import *
from inventory import *

class Order():

    def __init__(self, orderid, main, other):
        self._orderid = orderid
        self._main = main # list object
        self._other = other # list object
        self.status = "preparing your order" # accessible for staff
    
    def get_subtotal(self):
        subtotal = 0
        for item in self.main:
            subtotal = subtotal + item.getprice()
        for item in self.other:
            subtotal = subtotal + item.getprice()
        return subtotal
       
    def update_order(self): # staff use only
        self.status = 1
        
    @property
    def orderid(self):
        return self._orderid

    @property
    def main(self):
        return self._main

    @property
    def other(self):
        return self._other

    @property
    def subtotal(self):
        return self.get_subtotal()
    
        
