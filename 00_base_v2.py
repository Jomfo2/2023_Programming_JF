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


# function to get order
def order_loop(sold, maximum, question):
    total = 0
    while sold < maximum:
        response = input(question).lower()

        if response == "x" or response == "exit":
            break
        elif response == "menu":
            pass
        elif response in item_list:
            item = response
        else:
            try:
                item = item_list[int(response) - 1]
            except ValueError:
                print("input a valid item or id: ")
                pass

        amount = int(input("How many of this item would you like to order? "))

        if (sold + amount) <= maximum:
            sold += amount
            while amount > 0:
                order_list.append(item)
                amount -= 1
            print(order_list)
        else:
            print("Please order no more than {} items at a time".format(maximum))
            pass


# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]
item_list = ["a", "b", "c", "d", "e"]
order_list = []

# set maximum number of items here
MAX_ORDER = 5
pizzas_sold = 0

# asks if users want to see menu
want_menu = string_checker("Do you want to read the instructions? (y/n): ", 1, yes_no_list)
if want_menu == 1:
    print("menu goes here...")
else:
    print("continues...")

# order loop
order_loop(pizzas_sold, MAX_ORDER, "Input: ")

# asks users for payment method
pay_method = string_checker("Choose a payment method (cash / credit): ", 2, payment_list)
print("You chose", pay_method)

# output number of items sold
print("You have sold {} item/s. There are now {} item/s remaining".format(pizzas_sold, MAX_ORDER - pizzas_sold))
