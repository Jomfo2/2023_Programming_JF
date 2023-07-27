# functions go here

def order_loop(sold, maximum, question):
    while sold < maximum:
        response = input(question).lower()

        if response == "x" or response == "exit":
            break
        elif response == "menu":
            pass
        elif response == "a" or response == "1":
            item = 0
        elif response == "b" or response == "2":
            item = 1
        elif response == "c" or response == "3":
            item = 2
        elif response == "d" or response == "4":
            item = 3
        elif response == "e" or response == "5":
            item = 4
        else:
            print("input a valid item or id: ")
            pass

        amount = int(input("How many of this item would you like to order? "))

        if amount <= 5:
            while amount > 0:
                order_list.append(item)
                amount -= 1
            print(order_list)
        else:
            print("Please order less than 5 items at a time")
            pass


# main routine goes here
pizzas_sold = 0
MAX_ORDER = 5
order_list = []
item_list = ["a", "b", "c", "d", "e"]

order_loop(pizzas_sold, MAX_ORDER, "Input: ")
