import pandas


# functions go here
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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


def show_menu():
    print(""
          "***** Menu *****"
          "{} - {}"
          "{} - {}"
          "{} - {}"
          "{} - {}"
          "{} - {}".format(item_list[0], currency(int(price_list[0])), item_list[1], currency(int(price_list[1])),
                           item_list[2], currency(int(price_list[2])), item_list[3], currency(int(price_list[3])),
                           item_list[4], currency(int(price_list[4]))))


# main routine goes here
yes_no_list = ["yes", "no"]
item_list = ["a", "b", "c", "d", "e"]
price_list = [4, 5, 5, 5, 6]
order_list = []

pizza_dict = {
    "Item": item_list,
    "Price": price_list,
}

pizza_frame = pandas.DataFrame(pizza_dict)
pizza_frame = pizza_frame.set_index('Item')

# formatting currency
pizza_frame['Price'] = pizza_frame['Price'].apply(currency)

want_menu = string_checker("Do you want to read the instructions? (y/n): ", 1, yes_no_list)
if want_menu == "yes":
    print(pizza_frame)
else:
    print("continues...")
