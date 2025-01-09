#implement a program that enables a user to place an order,
#prompting them for items, one per line, until the user inputs control-d
#Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.

menu= {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
total= 0
while True:
    try:
        item=input("Item: ").title()
        if item in menu:
            total+=menu[item]
            decimal_total= "{:.2f}".format(total)
            print(f"Totall: ${decimal_total}")
    except EOFError:
            print()
            break



#After each inputted item, display the total cost of all items inputted thus far,
#prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively
