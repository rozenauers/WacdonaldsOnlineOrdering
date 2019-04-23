# Written by XJ

# virtual clients for back-end testing using pytest
from inventory import *
from restaurant_system1 import *
from order import *
from food import *
from construction import *
import pytest
import pickle

####### Customer interface test - Online Ordering 
##### section1: test valid orders##########
def test_valid_order_1(): # order contains single main with extra, multiple side/drink
    system.refill_inventory("nugget", 3)
    system.refill_inventory("fries", 50)
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    other.append(three_nuggets)
    other.append(small_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 1
    assert cheeseburger in o.main
    assert three_nuggets in o.other
    assert small_fries in o.other
    assert o.subtotal == 12.5
    
def test_valid_order_2(): # order contains single main with extra, multiple side/drink
    system.refill_inventory("nugget", 6)
    system.refill_inventory("fries", 150)
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    other.append(six_nuggets)
    other.append(large_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 2
    assert cheeseburger in o.main
    assert six_nuggets in o.other
    assert large_fries in o.other
    assert o.subtotal == 21.5  

def test_valid_order_3(): # order contains single main with extra
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    o = system.make_order(main, other)
    #assert o.orderid == 3
    assert cheeseburger in o.main
    assert o.subtotal == 6.5  

def test_valid_order_4(): # order contains single main without extra
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    main = []
    other  = []
    main.append(hamburger)
    o = system.make_order(main, other)
    #assert o.orderid == 4
    assert hamburger in o.main
    assert o.subtotal == 5 

def test_valid_order_5(): # order contains multiple mains with extra
    system.refill_inventory("cheese slice", 2)
    system.refill_inventory("sesame bun", 5)
    system.refill_inventory("beef patty", 3)
    system.refill_inventory("pepper", 2)
    main = []
    other  = []
    main.append(cheeseburger)
    main.append(double_cheeseburger)
    o = system.make_order(main, other)
    #assert o.orderid == 5
    assert cheeseburger in o.main
    assert double_cheeseburger in o.main
    assert o.subtotal == 17 

def test_valid_order_6(): # order contains multiple mains without extra
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    main = []
    other  = []
    main.append(hamburger)
    o = system.make_order(main, other)
    #assert o.orderid == 6
    assert hamburger in o.main
    assert o.subtotal == 5 

def test_valid_order_7(): # order contains single main with extra, single side/drink
    system.refill_inventory("fries", 150)
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    other.append(large_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 7
    assert cheeseburger in o.main
    assert large_fries in o.other
    assert o.subtotal == 15.5  

def test_valid_order_8(): # order contains single main without extra, single side/drink
    system.refill_inventory("fries", 150)
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    main = []
    other  = []
    main.append(hamburger)
    other.append(large_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 8
    assert hamburger in o.main
    assert large_fries in o.other
    assert o.subtotal == 14

def test_valid_order_9(): # order contains single side/drink
    system.refill_inventory("fries", 150)
    main = []
    other  = []
    other.append(large_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 9
    assert large_fries in o.other
    assert o.subtotal == 9

def test_valid_order_10(): # order contains multiple side/drink
    system.refill_inventory("fries", 150)
    system.refill_inventory("nugget", 6)
    main = []
    other  = []
    other.append(large_fries)
    other.append(six_nuggets)
    o = system.make_order(main, other)
    #assert o.orderid == 10
    assert large_fries in o.other
    assert o.subtotal == 15

def test_valid_order_11(): # order contains multiple mains, multiple side/drink
    system.refill_inventory("cheese slice", 2)
    system.refill_inventory("sesame bun", 7)
    system.refill_inventory("beef patty", 4)
    system.refill_inventory("pepper", 2)
    system.refill_inventory("fries", 50)
    system.refill_inventory("nugget", 3)
    main = []
    other  = []
    main.append(cheeseburger)
    main.append(double_cheeseburger)
    main.append(hamburger)
    other.append(three_nuggets)
    other.append(small_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 11
    assert cheeseburger in o.main
    assert double_cheeseburger in o.main
    assert hamburger in o.main
    assert small_fries in o.other
    assert three_nuggets in o.other
    assert o.subtotal == 28  

def test_valid_order_12(): # order contains single wrap with extra
    system.refill_inventory("white wrap", 100)
    system.refill_inventory("chicken patty", 1)
    main = []
    other  = []
    main.append(chicken_wrap)
    o = system.make_order(main, other)
    #assert o.orderid == 12
    assert chicken_wrap in o.main
    assert o.subtotal == 4.5

def test_valid_order_13(): # order contains single wrap with extra
    system.refill_inventory("white wrap", 100)
    system.refill_inventory("chicken patty", 2)
    main = []
    other  = []
    main.append(double_chicken_wrap)
    o = system.make_order(main, other)
    #assert o.orderid == 13
    assert double_chicken_wrap in o.main
    assert o.subtotal == 7

def test_valid_order_14(): # a complex order
    system.refill_inventory("cheese slice", 2)
    system.refill_inventory("sesame bun", 7)
    system.refill_inventory("beef patty", 4)
    system.refill_inventory("pepper", 2)
    system.refill_inventory("fries", 50)
    system.refill_inventory("nugget", 3)
    system.refill_inventory("white wrap", 100)
    system.refill_inventory("chicken patty", 2)
    main = []
    other  = []
    main.append(cheeseburger)
    main.append(double_cheeseburger)
    main.append(hamburger)
    main.append(double_chicken_wrap)
    other.append(three_nuggets)
    other.append(small_fries)
    o = system.make_order(main, other)
    #assert o.orderid == 14
    assert cheeseburger in o.main
    assert double_cheeseburger in o.main
    assert hamburger in o.main
    assert double_chicken_wrap in o.main
    assert small_fries in o.other
    assert three_nuggets in o.other
    assert o.subtotal == 35

##### section2: test invalid orders########
def test_invalid_order_0(): # main and side/drink not in inventory
    main = []
    other  = []
    main.append(plastic_burger)
    main.append(cheeseburger)
    other.append(cider)
    o = system.make_order(main, other)
    assert o == "Your main and side/drink are currently unavailable"

def test_invalid_order_1(): # main not in inventory
    main = []
    other  = []
    main.append(plastic_burger)
    main.append(cheeseburger)
    o = system.make_order(main, other)
    assert o == "Your main is currently unavailable"

def test_invalid_order_2(): # side/drink not in inventory
    main = []
    other  = []
    other.append(cider)
    main.append(cheeseburger)
    o = system.make_order(main, other)
    assert o == "Your side/drink is currently unavailable"

def test_invalid_order_3(): # main incomplete
    main = []
    other  = []
    main.append(half_burger)
    main.append(cheeseburger)
    o = system.make_order(main, other)
    assert o == "Please complete your main"

def test_invalid_order_4(): # side/drink incomplete
    main = []
    other  = []
    other.append(empty)
    o = system.make_order(main, other)
    assert o == "Please complete your side/drink"

def test_invalid_order_5(): # main and side/drink incomplete
    main = []
    other  = []
    main.append(cheeseburger)
    main.append(half_burger)
    other.append(empty)
    o = system.make_order(main, other)
    assert o == "Please complete your main and side/drink"

def test_invalid_order_6(): # inventory not enough for main and side/drink
    system.refill_inventory("nugget", 1)
    system.refill_inventory("fries", 150)
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 1)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    other.append(six_nuggets)
    other.append(large_fries)
    o = system.make_order(main, other)
    # clear the inventory refilled above for further testing
    system.use_inventory("nugget", 1)
    system.use_inventory("fries", 150)
    system.use_inventory("cheese slice", 1)
    system.use_inventory("sesame bun", 1)
    system.use_inventory("beef patty", 1)
    system.use_inventory("pepper", 1)
    assert o == "Your main and side/drink are out of stock"

def test_invalid_order_7(): # inventory not enough for main
    system.refill_inventory("nugget", 6)
    system.refill_inventory("fries", 150)
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 1)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    other.append(six_nuggets)
    other.append(large_fries)
    o = system.make_order(main, other)
    # clear the inventory refilled above for further testing
    system.use_inventory("nugget", 6)
    system.use_inventory("fries", 150)
    system.use_inventory("cheese slice", 1)
    system.use_inventory("sesame bun", 1)
    system.use_inventory("beef patty", 1)
    system.use_inventory("pepper", 1)
    assert o == "Your main is out of stock"

def test_invalid_order_8(): # inventory not enough for side/drink
    system.refill_inventory("nugget", 1)
    system.refill_inventory("fries", 150)
    system.refill_inventory("cheese slice", 1)
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 1)
    system.refill_inventory("pepper", 1)
    main = []
    other  = []
    main.append(cheeseburger)
    other.append(six_nuggets)
    other.append(large_fries)
    o = system.make_order(main, other)
    # clear the inventory refilled above for further testing
    system.use_inventory("nugget", 1)
    system.use_inventory("fries", 150)
    system.use_inventory("cheese slice", 1)
    system.use_inventory("sesame bun", 2)
    system.use_inventory("beef patty", 1)
    system.use_inventory("pepper", 1)
    assert o == "Your side/drink is out of stock"

def test_invalid_order_9(): # empty order
    main = []
    other  = []
    o = system.make_order(main, other)
    assert o == "Your order is empty"

def test_invalid_order_10(): # invalid main
    system.refill_inventory("sesame bun", 2)
    system.refill_inventory("beef patty", 2)
    main = []
    other  = []
    main.append(bad_burger)
    o = system.make_order(main, other)
    system.use_inventory("sesame bun", 2)
    system.use_inventory("beef patty", 2)
    assert o == "Your main is invalid"

def test_invalid_order_11(): # invalid main
    system.refill_inventory("gluten free wrap", 100)
    system.refill_inventory("beef patty", 3)
    main = []
    other  = []
    main.append(big_wrap)
    o = system.make_order(main, other)
    system.use_inventory("gluten free wrap", 100)
    system.use_inventory("beef patty", 3)
    assert o == "Your main is invalid"

def test_invalid_order_12(): # invalid main
    system.refill_inventory("gluten free wrap", 100)
    system.refill_inventory("beef patty", 3)
    system.refill_inventory("fries", 50)
    main = []
    other  = []
    main.append(big_wrap)
    other.append(small_fries)
    o = system.make_order(main, other)
    system.use_inventory("gluten free wrap", 100)
    system.use_inventory("beef patty", 3)
    system.use_inventory("fries", 50)
    assert o == "Your main is invalid"