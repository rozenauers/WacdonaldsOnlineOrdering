# Written by XJ

# virtual clients for back-end testing using pytest
from inventory import *
from restaurant_system1 import *
from order import *
from food import *
from construction import *
import pytest
import pickle

####### Staff interface test1 - Serve Orders 
def test_serve_1(): # order has single main
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    main = []
    other  = []
    main.append(hamburger)
    o = system.make_order(main, other)
    assert system.check_order_status(o.orderid) == "preparing your order"
    assert o in system.staff_orders
    system.serve_order(o.orderid)
    assert o in system.orders
    assert (o in system.staff_orders) == False
    assert system.check_order_status(o.orderid) == "your order is ready"

def test_serve_2(): # order has single main and side/drink
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("fries", 150)
    main = []
    other  = []
    main.append(hamburger)
    other.append(large_fries)
    o = system.make_order(main, other)
    assert system.check_order_status(o.orderid) == "preparing your order"
    assert o in system.staff_orders
    system.serve_order(o.orderid)
    assert o in system.orders
    assert (o in system.staff_orders) == False
    assert system.check_order_status(o.orderid) == "your order is ready"

def test_serve_3(): # order has single main and multiple side/drink
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("fries", 150)
    system.refill_inventory("nugget", 3)
    main = []
    other  = []
    main.append(hamburger)
    other.append(large_fries)
    other.append(three_nuggets)
    o = system.make_order(main, other)
    assert system.check_order_status(o.orderid) == "preparing your order"
    assert o in system.staff_orders
    system.serve_order(o.orderid)
    assert o in system.orders
    assert (o in system.staff_orders) == False
    assert system.check_order_status(o.orderid) == "your order is ready"

def test_serve_4(): # order has single side/drink
    system.refill_inventory("fries", 150)
    main = []
    other  = []
    other.append(large_fries)
    o = system.make_order(main, other)
    assert system.check_order_status(o.orderid) == "preparing your order"
    assert o in system.staff_orders
    system.serve_order(o.orderid)
    assert o in system.orders
    assert (o in system.staff_orders) == False
    assert system.check_order_status(o.orderid) == "your order is ready"

def test_serve_5(): # order has mulitple side/drink
    system.refill_inventory("fries", 150)
    system.refill_inventory("apple juice", 450)
    main = []
    other  = []
    other.append(large_fries)
    other.append(medium_apple_juice)
    o = system.make_order(main, other)
    assert system.check_order_status(o.orderid) == "preparing your order"
    assert o in system.staff_orders
    system.serve_order(o.orderid)
    assert o in system.orders
    assert (o in system.staff_orders) == False
    assert system.check_order_status(o.orderid) == "your order is ready"

def test_serve_6(): # a complex order
    system.refill_inventory("fries", 150)
    system.refill_inventory("apple juice", 450)
    system.refill_inventory("cheese slice", 2)
    system.refill_inventory("sesame bun", 7)
    system.refill_inventory("beef patty", 4)
    system.refill_inventory("pepper", 2)
    system.refill_inventory("nugget", 3)
    system.refill_inventory("white wrap", 100)
    system.refill_inventory("chicken patty", 2)
    main = []
    other  = []
    main.append(cheeseburger)
    main.append(double_cheeseburger)
    main.append(hamburger)
    main.append(double_chicken_wrap)
    other.append(large_fries)
    other.append(three_nuggets)
    other.append(medium_apple_juice)
    o = system.make_order(main, other)
    assert system.check_order_status(o.orderid) == "preparing your order"
    assert o in system.staff_orders
    system.serve_order(o.orderid)
    assert o in system.orders
    assert (o in system.staff_orders) == False
    assert system.check_order_status(o.orderid) == "your order is ready"