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
    editing = 1
    while editing == 1:
        edit_num = num_check("Which item would you like to remove? ")
        # order_list.clear([int(edit_num) - 1])
        order_list.pop(edit_num - 1)
        new_order_list = order_list
        total_list.pop(edit_num - 1)
        new_total_list = total_list

        data_frame = indexing(new_order_list, new_total_list)
        print(data_frame)

        cont = input("Continue editing? (y/n) ")
        if cont != "y":
            editing = 0
        
    save = input("Do you want to save changes? (y/n) ")
    if save == "y":
        return data_frame
    else:
        data_frame = pizza_frame


item_list = ["cheese", "ham and cheese", "pepperoni", "hawaiian", "vegan", "meat lovers"]
price_list = [4, 5, 5, 5, 6, 6.5]
order_list = ["cheese", "ham and cheese", "cheese", "vegan", "cheese"]
total_list = [4, 5, 4, 6, 4]

pizza_frame = indexing(order_list, total_list)
print(pizza_frame)
# formatting currency
# item_frame['Price'] = item_frame['Price'].apply(currency)

edit = input("Would you like to edit your order? (y/n) ")
if edit == "y":
    order_edit()
