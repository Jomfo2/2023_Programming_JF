# functions go here

# main routine goes here

# set maximum number of items here
MAX_ORDER = 5

# order loop
pizzas_sold = 0
while pizzas_sold < MAX_ORDER:
    name = input("Please enter your name or 'x' to quit: ")

    if name == 'x':
        break

    pizzas_sold += 1

# output number of items sold
print("You have sold {} item/s. There are now {} item/s remaining".format(pizzas_sold, MAX_ORDER - pizzas_sold))