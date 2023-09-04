import pandas


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


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
    edit_num = num_check("Which item would you like to remove? ")
    # order_list.clear([int(edit_num) - 1])
    order_list.pop(edit_num - 1)
    new_order_list = order_list
    total_list.pop(edit_num - 1)
    new_total_list = total_list

    pizza_frame = indexing(new_order_list, new_total_list)

    print(pizza_frame)
    print(new_total_list)
    print(new_order_list)


item_list = ["cheese", "ham and cheese", "pepperoni", "hawaiian", "vegan", "meat lovers"]
price_list = [4, 5, 5, 5, 6, 6.5]
order_list = ["cheese", "ham and cheese", "cheese", "vegan", "cheese"]
total_list = [4, 5, 4, 6, 4]

pizza_frame = indexing(order_list, total_list)
# formatting currency
# item_frame['Price'] = item_frame['Price'].apply(currency)

edit = input("Would you like to edit your order? (y/n) ")
if edit == "y":
    order_edit()
