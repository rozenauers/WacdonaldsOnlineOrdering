from flask import render_template, request, redirect, url_for, abort
from datetime import datetime
from restaurant_system import *
from server import app, system
from food import Main
from inventory import Inventory
from menu import *
from errors import *
import copy

# Global Lists
# CLEAR THE LISTS WHEN ORDER IS DONE
mainlist = []       #Burger Main List
otherlist = []      #Drinks, Sides & Dessert List
extraslist = []     #Burger Extras List

mysystem = RestaurantSystem()
'''
LOOK AT MENU.PY FOR ITEMS
'''

'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):

    return render_template('404.html'), 404



'''
Search for Order
'''
@app.route('/', methods=["GET", "POST"])
def menu():
    if request.method == "POST":
        if request.form.get('custom') == 'Customised Main':

            return redirect(url_for('custom'))

        if request.form.get('premade') == 'Premade Main':

            return redirect(url_for('premade'))

        if request.form.get('other') == 'Sides/Drinks/Dessert':

            return redirect(url_for('other'))

        if request.form.get('staff') == 'Staff Options':

            return redirect(url_for('staffvalidate'))

        if request.form.get('cancel') == 'Cancel':
            # Clear everything as order is cancelled
            mainlist.clear()
            extraslist.clear()
            otherlist.clear()

            return render_template('menu.html', cancel="You have successfully cancelled your order!")

        if request.form.get('confirm') == 'Make Order':
            o2 = mysystem.make_order(mainlist, otherlist)
            if isinstance(o2, str): # invalid order

                return render_template('menu.html', cancel = o2)

            # if order is valid, display confirmation page
            o1 = copy.deepcopy(o2)
            mainlist.clear()
            otherlist.clear()
            extraslist.clear()

            return render_template('order_confirm.html', orderid = o1.orderid,
                                    main = o1.main, other = o1.other,
                                    status = o1.status,
                                    price = o1.subtotal)

    return render_template('menu.html')

'''
Choice for premade mains
'''
@app.route('/premade', methods=["GET", "POST"])
# Premade Mains Option Page
def premade():
    if request.method == "POST":
        # Checking if the "Add Main to Order" button is clicked
        if request.form.get('add') == 'Add Main to Order':
            input = request.form.get('main')
            # If the "None" button is selected
            if input == 'none':
                return render_template('premade_choice.html', error="You did not choose a meal!")

            elif input == 'cheeseburger':
                mainlist.append(cheeseburger)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'cheeseburger2':
                mainlist.append(double_cheeseburger)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'chickenburger':
                mainlist.append(chickenburger)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'chickenburger2':
                mainlist.append(double_chickenburger)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'veggieburger':
                mainlist.append(veggieburger)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'veggieburger2':
                mainlist.append(double_veggieburger)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'chickenwrap':
                mainlist.append(chicken_wrap)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'chickenwrap2':
                mainlist.append(double_chicken_wrap)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'beefwrap':
                mainlist.append(beef_wrap)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))

            elif input == 'beefwrap2':
                mainlist.append(double_beef_wrap)
                return redirect(url_for('menu', success="You successfully added a main to your order!"))


        elif request.form.get('cancel') == 'Cancel':
            return redirect(url_for('menu', cancel="You successfully cancelled your Premade Main Selection!"))

    return render_template('premade_choice.html')

'''
Choice for custom mains'function' object has no attribute 'append'

'''
@app.route('/custom', methods=["GET", "POST"])
def custom():
    if request.method == "POST":
        # Checking if the "Add Main to Order" button is clicked
        if request.form.get('add') == 'Add Main to Order':
            container = request.form.get('container')
            contents = request.form.get('contents')

            # Initialising the Inputs, I can do this because its must have no
            # errors when these inputs are used
            inputcontainer = two_sesame_buns
            inputcontent = single_beef_patty
            inputextra = extraslist

            # Checks If select is empty, if they are empty a error message will
            # appear below its respective drop menus
            if (container == 'none') or (contents == 'none'):

                return render_template('custom_choice.html',
                                        containercheck=container,
                                        contentscheck=contents,
                                        containererror="You did not choose your preferred Bun/Wrap!",
                                        contenterror="You did not choose your preferred Patty!")
            else:
                # Scrapping Data for Patties
                if contents == 'beef1':
                    inputcontent = single_beef_patty

                elif contents == 'beef2':
                    inputcontent = double_beef_patty

                elif contents == 'chicken1':
                    inputcontent = single_chicken_patty

                elif contents == 'chicken2':
                    inputcontent = double_chicken_patty

                elif contents == 'veg1':
                    inputcontent = single_veg_patty

                elif contents == 'veg2':
                    inputcontent = double_veg_patty


                # Scrapping Data for Containers
                if container == 'sesamebun2':
                    inputcontainer = two_sesame_buns

                elif container == 'sesamebun3':
                    inputcontainer = three_sesame_buns

                elif container == 'whitewrap':
                    inputcontainer = white_wrap

                elif container == 'glutenfree':
                    inputcontainer = gluten_free_wrap

                # Adding the Main into the main list
                inputextra = copy.deepcopy(extraslist)
                mainlist.append(Main(inputcontainer, inputcontent, inputextra))
                extraslist.clear()

                return redirect(url_for('menu', success="You successfully added a main to your order!"))

        # Checking if Cancel Button is clicked
        elif request.form.get('cancel') == 'Cancel':
            extraslist.clear()
            return redirect(url_for('menu', cancel="You successfully cancelled your Custom Main Selection!"))

        elif request.form.get('extras') == 'Add Extra Toppings':
            return redirect(url_for('burgerextras'))

    return render_template('custom_choice.html')

@app.route('/burgerextras', methods=["GET", "POST"])
def burgerextras():
    if request.method == "POST":
        # Checking if the "Add Main to Order" button is clicked
        if request.form.get('add') == 'Add Extras':
            extrasinput = request.form.get('extras')

            # Checks If select is empty, if they are empty a error message will
            # appear below its respective drop menus
            if (extrasinput == 'none'):

                return render_template('burger_extras.html',
                                        extrascheck=extrasinput,
                                        extraerror="You did not choose your preferred Extras!")
            else:
                # Scrapping Data for Containers

                # Scrapping Data for Extras and Appending it to the list
                if extrasinput == 'cheese':
                    extraslist.append(cheese_slice)
                elif extrasinput == 'pepper':
                    extraslist.append(pepper)
                elif extrasinput == 'salt':
                    extraslist.append(salt)
                elif extrasinput == 'ketchup':
                    extraslist.append(ketchup)

                return redirect(url_for('custom'))

        # Checking if Cancel Button is clicked
        elif request.form.get('cancel') == 'Cancel':
            return redirect(url_for('custom'))

    return render_template('burger_extras.html')


@app.route('/other', methods=["GET", "POST"])
# Sides/Drinks/Dessert Option Page
def other():
    if request.method == "POST":
        # Checking if the "Add Extras to Order" button is clicked
        if request.form.get('add') == 'Add Extras to Order':
            sides = request.form.get('sides')
            drinks = request.form.get('drinks')
            dessert = request.form.get('dessert')

            # Checks If select is empty, if they are empty a error message will
            # appear on the page
            if (sides == 'none') and (drinks == 'none') and (dessert == 'none'):

                return render_template('other.html',
                                        sidescheck=sides,
                                        drinkscheck=drinks,
                                        dessertcheck=dessert,
                                        othererror="You did not choose anything!")
            else:
                # Scrapping Data for Sides
                if sides == 'nugget3':
                    otherlist.append(three_nuggets)

                elif sides == 'nugget6':
                    otherlist.append(six_nuggets)

                elif sides == 'friessmall':
                    otherlist.append(small_fries)

                elif sides == 'friesmedium':
                    otherlist.append(medium_fries)

                elif sides == 'frieslarge':
                    otherlist.append(large_fries)

                # Scrapping Data for Drinks
                if drinks == 'colacan':
                    otherlist.append(cola_can)

                elif drinks == 'lemonadecan':
                    otherlist.append(lemonade_can)

                elif drinks == 'waterbottle':
                    otherlist.append(water_bottle)

                elif drinks == 'teabottle':
                    otherlist.append(tea_bottle)

                elif drinks == 'orangesmall':
                    otherlist.append(small_orange_juice)

                elif drinks == 'orangemedium':
                    otherlist.append(medium_orange_juice)

                elif drinks == 'applesmall':
                    otherlist.append(small_apple_juice)

                elif drinks == 'applemedium':
                    otherlist.append(medium_apple_juice)

                # Scrapping Data for Desserts
                if dessert == 'chocsundsmall':
                    otherlist.append(small_chocolate_sundae)

                elif dessert == 'chocsundmedium':
                    otherlist.append(medium_chocolate_sundae)

                elif dessert == 'chocsundlarge':
                    otherlist.append(large_chocolate_sundae)

                elif dessert == 'strawsundsmall':
                    otherlist.append(small_strawberry_sundae)

                elif dessert == 'strawsundmedium':
                    otherlist.append(medium_strawberry_sundae)

                elif dessert == 'strawsundlarge':
                    otherlist.append(large_strawberry_sundae)

                return redirect(url_for('menu', success="You successfully added Extras to your order!"))

        # Checking if Cancel Button is clicked
        elif request.form.get('cancel') == 'Cancel':

            return redirect(url_for('menu', cancel="You successfully cancelled your Extras Selection!"))

    return render_template('other.html')

@app.route('/staffvalidate', methods=["GET", "POST"])
def staffvalidate():
    if request.method == "POST":
        if request.form['p'] == "":
            return render_template('staff_validate.html', error = "Please enter password")
        elif request.form['p'] != "Wacdonald's":
            return render_template('staff_validate.html', error = "Wrong password")
        else:
            return redirect(url_for('staff'))

    return render_template('staff_validate.html')

@app.route('/staff', methods=["GET", "POST"])
# Staff Options Page
def staff():
    if request.method == "POST":
        # Checking if the "Serve Order" button is clicked
        if request.form.get('serve') == 'Serve Order':

            return redirect(url_for('staffserve'))

        # Checking if the "View Active Orders" button is clicked
        elif request.form.get('view') == 'View Active Orders':

            return redirect(url_for('staffview'))

        # Checking if the "Check Inventory" button is clicked
        elif request.form.get('check') == 'Check Inventory':

            return redirect(url_for('staffcheck'))

        # Checking if the "Update Inventory" button is clicked
        elif request.form.get('update') == 'Update Inventory':

            return redirect(url_for('staffupdate'))

        # Checking if Cancel Button is clicked
        elif request.form.get('cancel') == 'Cancel':

            return redirect(url_for('menu', cancel="You successfully cancelled your changes!"))

    return render_template('staff.html')

@app.route('/staffview')
# Serve Order Page
def staffview():
    olist = mysystem.staff_orders
    return render_template('staff_view_orders.html', olist = olist)

@app.route('/staffserve', methods=["GET", "POST"])
# Serve Order Page
def staffserve():
    Os = None
    if request.method == "POST":
        # Checking if Cancel Button is clicked
        if request.form.get('cancel') == 'Cancel':
            return redirect(url_for('staff', cancel="You successfully cancelled your changes!"))
        elif request.form.get('serve') == 'Serve Order':
            if request.form['orderID'] == "":
                return render_template('staff_serve.html', serveerror = "Please enter a valid Order ID", os = None)
            else:
                oid = request.form['orderID']
                c = int(oid)
                ostatus = mysystem.serve_order(c)
                Os = "Order has been updated"

    return render_template('staff_serve.html', serveerror = None, os = Os)

@app.route('/staffcheck', methods=["GET", "POST"])
# Check Inventory Page
def staffcheck():
    if request.method == "POST":
        if request.form.get('check') == 'Check Inventory':
            itemName = request.form['itemName']

            if not itemName:
                return render_template('staff_check.html', nameerror="You must enter a valid item!")

            checkInventory = mysystem.check_inventory(itemName)

            if isinstance(checkInventory, str):
                return render_template('staff_check.html', nameerror=checkInventory)

            return render_template('staff_check.html', inv=checkInventory, name=itemName)


        # Checking if Cancel Button is clicked
        if request.form.get('cancel') == 'Cancel':

            return redirect(url_for('staff', cancel="You successfully cancelled your changes!"))

    return render_template('staff_check.html')

@app.route('/staffupdate', methods=["GET", "POST"])
# Update Inventory Page
def staffupdate():
    if request.method == "POST":
        if request.form.get('refill') == 'Refill Inventory':
            itemName = request.form['itemName']
            itemAmount = request.form['itemAmount']
            c = int(itemAmount, 10)

            if not itemName:
                return render_template('staff_update.html', nameerror="You must enter a valid item!")

            if not c:
                return render_template('staff_update.html', amounterror="You must enter a valid amount!")

            refillInventory = mysystem.refill_inventory(itemName, c)
            checkInventory = mysystem.check_inventory(itemName)

            return render_template('staff_update.html', inv=checkInventory, name=itemName)

        # Checking if Cancel Button is clicked
        elif request.form.get('cancel') == 'Cancel':

            return redirect(url_for('staff', cancel="You successfully cancelled your changes!"))

    return render_template('staff_update.html')

'''
Order Detail Page (After Confirmation)
'''
@app.route('/orderdetails', methods=["GET", "POST"])
def order_details():
    if request.method == 'POST':
        if request.form['orderid'] == "":
            return render_template('order_details.html', error = "Please enter a valid Order ID")
        else: # valid input
            oid = request.form['orderid']
            c = int(oid,10)
            ostatus = mysystem.check_order_status(c)
            return render_template('order_status.html', orderid = oid, status = ostatus)

    return render_template('order_details.html')
