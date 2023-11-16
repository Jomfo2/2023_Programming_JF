import pandas
from datetime import date


# functions go here
# checks if input is string then compares with valid responses
def string_checker(question, num_letters, valid_responses):

    error = "Please choose {} or {}".format(valid_responses[0], valid_responses[1])

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item

        print(error)


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


# prints instruction on how to use program
def show_instructions():
    print("""
        *****
        Instructions to order pizzas:
        1. Input the ID of the pizza you want from the menu. The ID's are ordered based on where the item is on the menu, e.g. Cheese is 1
        2. Input the amount you want of each pizza. Note that a maximum of 5 pizzas can be purchased at once
        3. If you have completed your order, input "x" or "exit" to proceed to editing and payment
        4. If you wish to remove a pizza from your order you can choose to do so after ordering
        5. You will be asked to input all details needed to complete the order
           You can choose between pickup and delivery, delivery is free
           You can choose to pay with cash or card, please note that payments by credit will add a 5% surcharge
        6. Your receipt will be printed and order will be processed
        *****
        """)


# function to get order
def order_loop(sold, maximum, question):
    item = 0
    while sold < maximum:
        valid = 0
        response = input(question).casefold()

        if response == "x" or response == "exit":
            if len(total_list) > 0:
                break
            else:
                print("Please order at least one item ")
        elif response == "instructions":
            show_instructions()
        if response.capitalize() in item_list:
            item = response.lower()
            valid = 1
        else:
            try:
                if int(response) > 0:
                    item = item_list[int(response) - 1]
                    valid = 1
                else:
                    print("input a valid item or id")
            except ValueError:
                print("input a valid item or id")

        if valid == 1:
            amount = input("How many of this item would you like to order? ")

            try:
                amount = int(amount)
                if (sold + amount) <= maximum:
                    sold += amount
                    while amount > 0:
                        order_list.append(item.capitalize())

                        total_index = item_list.index(item)
                        item_cost = int(price_list[total_index])
                        item_cost = currency(item_cost)
                        total_p.append(price_list[total_index])
                        total_list.append(item_cost)
                        amount -= 1
                    print(order_list)
                    print(total_list)
                else:
                    print("Please order no more than {} items at a time".format(maximum))
            except ValueError:
                print("Please input a valid item or id: ")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# function to index data frames
def indexing(i_list, p_list):
    data_dict = {
        "Item": i_list,
        "Total": p_list
    }
    data_frame = pandas.DataFrame(data_dict)
    data_frame = data_frame.set_index('Item')
    return data_frame


# function to edit order list
def order_edit():
    editing = "yes"
    while editing == "yes":
        edit_num = num_check("Which item would you like to remove? ")
        # order_list.clear([int(edit_num) - 1])
        total_p.pop(edit_num - 1)
        order_list.pop(edit_num - 1)
        new_order_list = order_list
        total_list.pop(edit_num - 1)
        new_total_list = total_list

        pizza_frame = indexing(new_order_list, new_total_list)
        print(pizza_frame)
        editing = string_checker("Do you want to continue editing? (y/n) ", 1, yes_no_list)


# print to file
def document(to_print, frame):
    # *** get today's date ***
    today = date.today()

    # get dd, mm, yy as individual strings
    day = today.strftime("%d")
    month = today.strftime("%m")
    year = today.strftime("%y")

    heading = "The current date is {}/{}/{}".format(day, month, year)
    filename = "MMF_{}_{}_{}".format(year, month, day)

    # *** open file here ***
    write_to = "{}.txt".format(filename)
    text_file = open(write_to, "w+")

    # *** sort and print ***

    # change frame to a string, so it can be exported to file
    frame_string = pandas.DataFrame.to_string(frame)

    # *** write and close ***
    text_file.write(heading + "\n")
    text_file.write(frame_string + "\n\n")

    for item in to_print:
        text_file.write(str(item))
        text_file.write("\n")

    # close file
    text_file.close()


# main routine starts here
# setting variables here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
location_list = ["delivery", "pickup", "pick up"]
item_list = ["Cheese", "Ham and cheese", "Pepperoni", "Hawaiian", "Vegan", "Meat lovers"]
price_list = [4, 5, 5, 5, 6, 6.5]
order_list = [""]
total_list = [""]
total_p = [0]
print_list = []

MAX_ORDER = 5
pizzas_sold = 0

item_frame = indexing(item_list, price_list)

# formatting currency
item_frame['Total'] = item_frame['Total'].apply(currency)

# asks if users want to see menu
want_instructions = string_checker("Do you want to read the instructions? (y/n): ", 1, yes_no_list)
if want_instructions == "yes":
    show_instructions()
else:
    pass

want_menu = string_checker("Do you want to view the menu? (y/n): ", 1, yes_no_list)
if want_menu == "yes":
    print(item_frame)
else:
    pass

# order loop
order_list.clear()
total_list.clear()
order_loop(pizzas_sold, MAX_ORDER, "Input: ")
pizza_frame = indexing(order_list, total_list)
# pizza_frame['Total Price'] = pizza_frame['Total Price'].apply(currency)

print(pizza_frame)

edit = string_checker("Would you like to edit your order? (y/n) ", 1, yes_no_list)
if edit == "yes":
    order_edit()

# delivery?
delivery_method = string_checker("Choose pickup or delivery: ", 2, location_list)
# print_list.append(delivery_method)

if delivery_method == "delivery":
    d_address = input("What is the address to deliver the order to? ")
    print_list.append("Delivery address: " + d_address)
else:
    d_address = "N/A"
    print_list.append("Delivery address: " + d_address)

# name input
order_name = input("What is the name for the order? ")
print_list.append("Name for order: " + order_name)

# asks users for payment method
pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)
# print_list.append(pay_method)

if pay_method == "cash":
    total_price = sum(total_p)
    card_num = "N/A"
    print_list.append("Card Number: " + card_num)
    surcharge = "None"
    print_list.append("Total price of order: " + str(currency(total_price)))
    print_list.append("Surcharge: " + str(surcharge))
else:
    while True:
        card_num = num_check("Please provide the card number for payment ")
        if card_num < 999999999999999:
            print_list.append("Card Number: " + str(card_num))
            break
        else:
            print("Card number too long ")

    surcharge = (sum(total_p) * 1.05) - sum(total_p)
    total_price = sum(total_p) + surcharge
    surcharge = currency(surcharge)
    total_price = currency(total_price)
    print_list.append("Total price of order: " + str(total_price))
    print_list.append("Surcharge: " + str(surcharge))

print(pizza_frame)
print(total_price)

print(print_list)
document(print_list, pizza_frame)
