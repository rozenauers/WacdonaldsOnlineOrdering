# Written by XJ
# THIS FILE CONSTRUCTS THE SYSTEM FOR TESTING ONLY
# TO CONSTRUCT A REAL SYSTEM, USE MENU.PY

# construct the system
from inventory import *
from restaurant_system1 import *
from order import *
from food import *
from errors import *
import pickle

# construction #
system = RestaurantSystem1()
# basic items
two_sesame_buns = Main_Component("sesame bun", 1, 2)
three_sesame_buns = Main_Component("sesame bun", 1, 3)
white_wrap = Main_Component("white wrap", 0.02, 100) # since a wrap can hold multiple patties, make the "visible quantity" large, ie: 100 -> 1 wrap
gluten_free_wrap = Main_Component("gluten free wrap", 0.03, 100)
single_beef_patty = Main_Component("beef patty", 3, 1)
double_beef_patty = Main_Component("beef patty", 3, 2)
single_chicken_patty = Main_Component("chicken patty", 2.5, 1)
double_chicken_patty = Main_Component("chicken patty", 2.5, 2)
single_veg_patty = Main_Component("veg patty", 2, 1)
double_veg_patty = Main_Component("veg patty", 2, 2)
cheese_slice = Main_Component("cheese slice", 1.5, 1)
pepper = Main_Component("pepper", 0, 1)
salt = Main_Component("salt", 0, 1)
ketchup = Main_Component("ketchup", 0, 1)
plastic = Main_Component("plastic", 1.2, 1) # not available in inventory
piece = Main_Component("piece", 1.2, 1) # incomplete item
extra1 = []
extra1.append(cheese_slice)
extra1.append(pepper)
no_extra = []
triple_patty = Main_Component("triple patty", 3, 3) # invalid patty amount
# build some complete items for testing
cheeseburger = Main(two_sesame_buns, single_beef_patty, extra1)
double_cheeseburger = Main(three_sesame_buns, double_beef_patty, extra1)
hamburger = Main(two_sesame_buns, single_beef_patty, no_extra)
chicken_wrap = Main(white_wrap, single_chicken_patty, no_extra)
double_chicken_wrap = Main(white_wrap, double_chicken_patty, no_extra)
bad_burger = Main(two_sesame_buns, double_beef_patty, no_extra)
plastic_burger = Main(plastic, plastic, no_extra) # not available in inventory
half_burger = Main(piece, None, None) # incomplete item
big_wrap = Main(gluten_free_wrap, triple_patty, no_extra)
# nuggets pack 
three_nuggets = Other("nugget", 1, 3)
six_nuggets = Other("nugget", 1, 6)
empty = Other("nugget", 1, None)
# fries 
small_fries = Other("fries", 0.06, 50)
medium_fries = Other("fries", 0.06, 100)
large_fries = Other("fries", 0.06, 150)
cider = Other("cider", 5, 1) # not available in inventory
# drinks
cola_can = Other("cola can", 3, 1)
lemonade_can = Other("lemonade can", 3, 1)
water_bottle = Other("water bottle", 4, 1)
tea_bottle = Other("tea bottle", 5, 1)
small_orange_juice = Other("orange juice", 0.02, 250)
medium_orange_juice = Other("orange juice", 0.02, 450)
small_apple_juice = Other("apple juice", 0.02, 250)
medium_apple_juice = Other("apple juice", 0.02, 450)
