import pandas
from datetime import date


# functions go here
# function to index data frames
def indexing(i_list, p_list):
    data_dict = {
        "Item": i_list,
        "Total": p_list
    }
    data_frame = pandas.DataFrame(data_dict)
    data_frame = data_frame.set_index('Item')
    return data_frame


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


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
    to_print.append(heading)

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
        text_file.write(item)
        text_file.write("\n")

    # close file
    text_file.close()


# main routine goes here
# example order lists
order_list = ["Cheese", "Ham and cheese", "Cheese", "Meat lovers"]
total_list = [4, 5, 4, 6.5]
pizza_frame = indexing(order_list, total_list)
pizza_frame['Total'] = pizza_frame['Total'].apply(currency)

print_list = ["delivery? ", "name: ", "card number: ", "surcharge: ", "total: "]
document(print_list, pizza_frame)
