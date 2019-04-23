
# construct the system
from inventory import *
from restaurant_system import *
from order import *
from food import *
from errors import *
import pickle

# construction #
system = RestaurantSystem()

# Ingredients for the burger
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
extra1 = []
extra1.append(cheese_slice)
extra1.append(pepper)
no_extra = []

# Complete Menu Items
cheeseburger = Main(two_sesame_buns, single_beef_patty, extra1)
double_cheeseburger = Main(three_sesame_buns, double_beef_patty, extra1)
chickenburger = Main(two_sesame_buns, single_chicken_patty, extra1)
double_chickenburger = Main(three_sesame_buns, double_chicken_patty, extra1)
veggieburger = Main(two_sesame_buns, single_veg_patty, extra1)
double_veggieburger = Main(two_sesame_buns, single_veg_patty, extra1)
chicken_wrap = Main(white_wrap, single_chicken_patty, extra1)
double_chicken_wrap = Main(white_wrap, double_chicken_patty, extra1)
beef_wrap = Main(white_wrap, single_beef_patty, extra1)
double_beef_wrap = Main(white_wrap, double_chicken_patty, extra1)

# Sides
# nuggets
three_nuggets = Other("nugget", 1, 3)
six_nuggets = Other("nugget", 1, 6)
empty = Other("nugget", 1, None)

# fries
small_fries = Other("fries", 0.06, 50)
medium_fries = Other("fries", 0.06, 100)
large_fries = Other("fries", 0.06, 150)

# desserts
small_chocolate_sundae = Other("chocolate sundae", 0.01, 75)
medium_chocolate_sundae = Other("chocolate sundae", 0.01, 125)
large_chocolate_sundae = Other("chocolate sundae", 0.01, 175)
small_strawberry_sundae = Other("strawberry sundae", 0.01, 75)
medium_strawberry_sundae = Other("strawberry sundae", 0.01, 125)
large_strawberry_sundae = Other("strawberry sundae", 0.01, 175)

# drinks
cola_can = Other("cola can", 3, 1)
lemonade_can = Other("lemonade can", 3, 1)
water_bottle = Other("water bottle", 4, 1)
tea_bottle = Other("tea bottle", 5, 1)
small_orange_juice = Other("orange juice", 0.02, 250)
medium_orange_juice = Other("orange juice", 0.02, 450)
small_apple_juice = Other("apple juice", 0.02, 250)
medium_apple_juice = Other("apple juice", 0.02, 450)
