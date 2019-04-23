# Written by XJ

from inventory import *

class OrderError(Exception): # constructor that takes the name of the invalid field provided and an error message
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
        
def check_inventory(inventory, name):
    for i in inventory:
        if i.name == name:
            return i.quantity

def available(inventory, name): # check if a specific ingredient is in inventory
    result = False
    for i in inventory:
        if i.name == name:
            result = True
    return result

def use_inventory(name, amount, inventory): 
        for i in inventory:
            if i.name == name:
                i.quantity = i.quantity - amount

def change_inventory(main, other, inventory):
        # main
        for item in main:
            use_inventory(item.containers.name, item.containers.quantity, inventory)
            use_inventory(item.contents.name, item.contents.quantity, inventory)
        # other(side and drink)
        for item in other:
            use_inventory(item.name, item.quantity, inventory)

def check_order_error(main, other, inventory):
    ##### simultaneous errors are being handled first
    ### error group0: empty order
    if len(main) == 0 and len(other) == 0:
        raise OrderError("Your order is empty")
        return
    ### error group1: incomplete input(unlikely to happen since I'm using drop-down list at front end)
    if incomplete(main, other) == 3: # both "main" and "other" are incomplete
        raise OrderError("Please complete your main and side/drink")
        return
    for item in main:
        if incomplete(main, other) == 1:
            raise OrderError("Please complete your main")
            return
    for item in other:
        if incomplete(main, other) == 2:
            raise OrderError("Please complete your side/drink")
            return
    ### error group2: not available
    if unavailable(main, other, inventory) == 3:
        raise OrderError("Your main and side/drink are currently unavailable")
        return
    if unavailable(main, other, inventory) == 1:
        raise OrderError("Your main is currently unavailable")
        return
    if unavailable(main, other, inventory) == 2:
        raise OrderError("Your side/drink is currently unavailable")
        return
    ### error group3: invalid main
    for m in main:
        if m._containers._quantity <= m._contents._quantity or m._contents._quantity > 2: # exceed max allowance
            raise OrderError("Your main is invalid")
            return
    ### error group4: not enough inventory
    change_inventory(main, other, inventory) 
    if not_enough(main, other, inventory) == 3:
        raise OrderError("Your main and side/drink are out of stock")
        return
    if not_enough(main, other, inventory) == 1:
        raise OrderError("Your main is out of stock")
        return
    if not_enough(main, other, inventory) == 2:
        raise OrderError("Your side/drink is out of stock")
        return
    
def enough(inventory, name):
    for i in inventory:
            if i.name == name:
                if i.quantity >= 0:
                    return True
    return False

def not_enough(main, other, inventory):
    i1 = 0
    i2 = 0
    for item in main:
        if enough(inventory, item.containers.name) == False or enough(inventory, item.contents.name) == False:
            i1 = 1
    for item in other: 
        if enough(inventory, item.name) == False:
            i2 = 1
    if i1 == 0 and i2 == 0:
        return 0
    if i1 == 0 and i2 == 1:
        return 2
    if i1 == 1 and i2 == 0:
        return 1
    if i1 == 1 and i2 == 1:
        return 3

def unavailable(main, other, inventory):
    i1 = 0
    i2 = 0
    for item in main: 
        if available(inventory, item.containers.name) == False or available(inventory, item.contents.name) == False:
            i1 = 1
    for item in other: 
        if available(inventory, item.name) == False:
            i2 = 1
    if i1 == 0 and i2 == 0:
        return 0
    if i1 == 0 and i2 == 1:
        return 2
    if i1 == 1 and i2 == 0:
        return 1
    if i1 == 1 and i2 == 1:
        return 3

def incomplete(main, other):
    i1 = 0 
    i2 = 0
    for item in main:
        if item.containers == None or item.contents == None or item.containers.name == None or item.containers.price == None or item.containers.quantity == None or item.contents.name == None or item.contents.price == None or item.contents.quantity == None:
            i1 = 1
    for item in other:
        if item.price == None or item.quantity == None:
            i2 = 1
    if i1 == 0 and i2 == 0:
        return 0
    if i1 == 0 and i2 == 1:
        return 2
    if i1 == 1 and i2 == 0:
        return 1
    if i1 == 1 and i2 == 1:
        return 3
