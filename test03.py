# Written by XJ

# virtual clients for back-end testing using pytest
from inventory import *
from restaurant_system1 import *
from order import *
from food import *
from construction import *
import pytest

####### Staff interface test2 - Maintain Inventory 
def test_maintain_inventory_1(): # refill single main component and use
    a1 = system.check_inventory("white wrap")
    system.refill_inventory("white wrap", 100)
    assert system.check_inventory("white wrap") == (a1+100)
    system.use_inventory("white wrap", 100)
    assert system.check_inventory("white wrap") == a1

def test_maintain_inventory_2(): # refill main components and use
    a1 = system.check_inventory("white wrap")
    a2 = system.check_inventory("beef patty")
    system.refill_inventory("beef patty", 4)
    system.refill_inventory("white wrap", 100)
    assert system.check_inventory("white wrap") == (a1+100)
    assert system.check_inventory("beef patty") == (a2+4)
    system.use_inventory("white wrap", 100)
    system.use_inventory("beef patty", 3)
    assert system.check_inventory("white wrap") == a1
    assert system.check_inventory("beef patty") == (a2+1)
    system.use_inventory("beef patty", 1)
    assert system.check_inventory("beef patty") == a2

def test_maintain_inventory_3(): # refill single side/drink and use
    a1 = system.check_inventory("nugget")
    system.refill_inventory("nugget", 3)
    assert system.check_inventory("nugget") == (a1+3)
    system.use_inventory("nugget", 3)
    assert system.check_inventory("nugget") == a1

def test_maintain_inventory_4(): # refill multiple side/drink and use
    a1 = system.check_inventory("nugget") 
    a2 = system.check_inventory("fries")
    system.refill_inventory("nugget", 3)
    system.refill_inventory("fries", 200)
    assert system.check_inventory("nugget") == (a1+3)
    assert system.check_inventory("fries") == (a2+200)
    system.use_inventory("nugget", 3)
    system.use_inventory("fries", 150)
    assert system.check_inventory("nugget") == a1
    assert system.check_inventory("fries") == (a2+50)
    system.use_inventory("fries", 50)
    assert system.check_inventory("fries") == a2

def test_maintain_inventory_5(): # refill complex items and use
    a1 = system.check_inventory("nugget") 
    a2 = system.check_inventory("fries") 
    a3 = system.check_inventory("white wrap") 
    a4 = system.check_inventory("beef patty")
    system.refill_inventory("nugget", 3)
    system.refill_inventory("fries", 200)
    system.refill_inventory("beef patty", 4)
    system.refill_inventory("white wrap", 100)
    assert system.check_inventory("white wrap") == (a3+100)
    assert system.check_inventory("beef patty") == (a4+4)
    assert system.check_inventory("nugget") == (a1+3)
    assert system.check_inventory("fries") == (a2+200)
    system.use_inventory("nugget", 3)
    system.use_inventory("fries", 150)
    system.use_inventory("white wrap", 100)
    system.use_inventory("beef patty", 3)
    assert system.check_inventory("white wrap") == a3
    assert system.check_inventory("beef patty") == (a4+1)
    assert system.check_inventory("nugget") == a1
    assert system.check_inventory("fries") == (a2+50)
    system.use_inventory("fries", 50)
    system.use_inventory("beef patty", 1)
    assert system.check_inventory("beef patty") == a4
    assert system.check_inventory("fries") == a2
