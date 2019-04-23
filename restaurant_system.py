from food import *
from order import *
from inventory import *
from errors import *
import pickle
import copy

class RestaurantSystem():

    def __init__(self):
        self._orders = self.init_orders()
        self._staff_orders = self.init_staff_orders()
        self._inventory = self.init_inventory()
        self._order_amount = len(self._orders)

    def init_orders(self):
        orders = []
        try:
            with open("orders.pickle", "rb") as f:
                orders = pickle.load(f)
        except EOFError:
            orders = []
        return orders

    def init_staff_orders(self):
        staff_orders = []
        try:
            with open("staff_orders.pickle", "rb") as f:
                staff_orders = pickle.load(f)
        except EOFError:
            staff_orders = []
        return staff_orders

    def init_inventory(self):
        all = []
        try:
            with open("inventory.pickle", "rb") as f:
                all = pickle.load(f)
        except EOFError: # first time use
            # create inventory instances(initial value 0)
            sesame_bun = Inventory("sesame bun", 0)
            gluten_free_bun = Inventory("gluten free bun", 0)
            white_wrap = Inventory("white wrap", 0)
            gluten_free_wrap = Inventory("gluten free wrap", 0)
            beef_patty = Inventory("beef patty", 0)
            chicken_patty = Inventory("chicken patty", 0)
            veg_patty = Inventory("veg patty", 0)
            cheese_slice = Inventory("cheese slice", 0)
            pepper = Inventory("pepper", 0)
            salt = Inventory("salt", 0)
            ketchup = Inventory("ketchup", 0)
            nugget = Inventory("nugget", 0)
            fries = Inventory("fries", 0)
            chocolate_sundae = Inventory("chocolate sundae", 0)
            strawberry_sundae = Inventory("strawberry sundae", 0)
            cola_can = Inventory("cola can", 0)
            lemonade_can = Inventory("lemonade can", 0)
            water_bottle = Inventory("water bottle", 0)
            tea_bottle = Inventory("tea bottle", 0)
            orange_juice = Inventory("orange juice", 0)
            apple_juice = Inventory("apple juice", 0)

            # virtual items for testing only
            triple_patty = Inventory("triple patty", 0) # invalid patty amount for testing
            piece = Inventory("piece", 0) # for testing only

            # append instances to all[]
            all.append(sesame_bun)
            all.append(gluten_free_bun)
            all.append(beef_patty)
            all.append(chicken_patty)
            all.append(veg_patty)
            all.append(cheese_slice)
            all.append(pepper)
            all.append(salt)
            all.append(ketchup)
            all.append(nugget)
            all.append(fries)
            all.append(chocolate_sundae)
            all.append(strawberry_sundae)
            all.append(piece)
            all.append(cola_can)
            all.append(lemonade_can)
            all.append(water_bottle)
            all.append(tea_bottle)
            all.append(orange_juice)
            all.append(apple_juice)
            all.append(white_wrap)
            all.append(gluten_free_wrap)
            all.append(triple_patty)

        return all

    def inventory_copy(self): # make a copy of current inventory state
        copy = []

        for i in self.inventory:
            c = Inventory(i.name, i.quantity)
            copy.append(c)

        return copy

    def check_inventory(self, name): # staff use only
        for i in self._inventory:
            if i.name == name:

                return i.quantity

        return "Invalid name" # if not in inventory

    def refill_inventory(self, name, amount): # staff use only
        for i in self.inventory:
            if i.name == name:
                i.quantity = i.quantity + amount

                with open("inventory.pickle", "wb") as f:
                    pickle.dump(self.inventory, f)

                return

        return "Invalid name" # if not in inventory

    def use_inventory(self, name, amount): # staff use only
        for i in self.inventory:
            if i.name == name:
                i.quantity = i.quantity - amount

                with open("inventory.pickle", "wb") as f:
                    pickle.dump(self.inventory, f)

                return

        return "Invalid name" # if not in inventory

    def getid(self): # assign a unique orderid to a valid order
        self._order_amount = self._order_amount + 1

        return self._order_amount

    def check_fee(self, main, other): # customer use only
        subtotal = 0

        for item in main:
            subtotal = subtotal + item.getprice()

        for item in other:
            subtotal = subtotal + item.getprice()

        return subtotal

    def update_inventory(self, order):
        # main
        for item in order.main:
            self.use_inventory(item.containers.name, item.containers.quantity)
            self.use_inventory(item.contents.name, item.contents.quantity)
        with open("inventory.pickle", "wb") as f:
            pickle.dump(self.inventory, f)
        # other(side and drink)
        for item in order.other:
            self.use_inventory(item.name, item.quantity)
        with open("inventory.pickle", "wb") as f:
            pickle.dump(self.inventory, f)

    def make_order(self, main, other): # customer use only
        try: # validate items ordered
            inventory_copy = self.inventory_copy() # passing a copy to preserve system state
            check_order_error(main, other, inventory_copy)
        except OrderError as err: # reture error message
            return err.message
        else: # if items ordered are valid
            # assign an orderid and create order object instance
            orderid = self.getid()
            o = copy.deepcopy(Order(orderid, main, other))
            # append to orders and staff_orders
            self._orders.append(o)
            self._staff_orders.append(o)
            with open("orders.pickle", "wb") as f:
                pickle.dump(self.orders, f)
            with open("staff_orders.pickle", "wb") as f:
                pickle.dump(self.staff_orders, f)
            # update inventory
            self.update_inventory(o)
            return o

    # "The customer can check the status of their order at any point using order-id"
    def check_order_status(self, orderid): # customer use only
        for order in self._orders:
            if order.orderid == orderid:

                return order.status

        return "Invalid Order ID"

    def serve_order(self, orderid): # staff use only
        # update order_status to "your order is ready" in all orders list
        for order in self._orders:
            if order.orderid == orderid:
                order.status = "your order is ready"

                with open("orders.pickle", "wb") as f:
                    pickle.dump(self.orders, f)
        # remove order from staff_orders list
        for order in self._staff_orders:
            if order.orderid == orderid:
                self._staff_orders.remove(order)

                with open("staff_orders.pickle", "wb") as f:
                    pickle.dump(self.staff_orders, f)

    @property
    def orders(self):
        return self._orders

    @property
    def staff_orders(self):
        return self._staff_orders

    @property
    def inventory(self):
        return self._inventory
