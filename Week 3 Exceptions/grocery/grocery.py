#prompt the user for items, one per line, until the user inputs control-d
#output the user’s grocery list in all uppercase, sorted alphabetically by item,
#prefixing each line with the number of times the user inputted that item.
#No need to pluralize the items. Treat the user’s input case-insensitively.
grocery_list={}
while True:
    try:
        item=input().upper()
        if item in grocery_list:
            grocery_list[item]+=1
        else:
            grocery_list[item]=1
    except EOFError:
        for key in sorted(grocery_list.keys()):
            print(grocery_list[key],key)
        break