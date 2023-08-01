import pandas


# functions go here
# function to get info from input
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
    print("Instructions go here...")


# function to get order
def order_loop(sold, maximum, question):
    valid = 0
    while sold < maximum:
        response = input(question).lower()

        if response == "x" or response == "exit":
            break
        elif response == "instructions":
            show_instructions()
        elif response == "menu":
            pass
        if response in item_list:
            item = response
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
                        order_list.append(item)
                        amount -= 1
                    print(order_list)
                else:
                    print("Please order no more than {} items at a time".format(maximum))
            except ValueError:
                print("Please input a valid item or id: ")


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
item_list = ["a", "b", "c", "d", "e"]
price_list = [4, 5, 5, 5, 6]
order_list = []

# set number of items here
MAX_ORDER = 5
pizzas_sold = 0

# e
item_dict = {
    "Item": item_list,
    "Price": price_list,
}

item_frame = pandas.DataFrame(item_dict)
item_frame = item_frame.set_index('Item')

# formatting currency
item_frame['Price'] = item_frame['Price'].apply(currency)

# asks if users want to see menu
want_instructions = string_checker("Do you want to read the instructions? (y/n): ", 1, yes_no_list)
if want_instructions == "yes":
    show_instructions()
else:
    print("continues...")

want_menu = string_checker("Do you want to view the menu? (y/n): ", 1, yes_no_list)
if want_menu == "yes":
    print(item_frame)
else:
    print("continues...")

# order loop
order_loop(pizzas_sold, MAX_ORDER, "Input: ")

# asks users for payment method
pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)
print("You chose", pay_method)

# output number of items sold
print("You have sold {} item/s. There are now {} item/s remaining".format(pizzas_sold, MAX_ORDER - pizzas_sold))
