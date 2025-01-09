#Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
#prompt the user to insert a coin, one at a time,
#only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
#ignore any integer that isn’t an accepted denomination.
#Once the user has inputted at least 50 cents output how many cents in change the user is owed.


amount_due = 50
coins = [25,10,5]
while amount_due > 0 :
    print (f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin not in coins:
        continue
    else:
        amount_due -= coin
print (f"Change Owed: {abs(amount_due)}")