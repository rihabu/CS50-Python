#prompt the user for the name of a variable in camel case
#Assume that the user’s input will indeed be in camel case
camelCase = input("camelCase: ")

#outputs the corresponding name in snake case

for i in camelCase:
        if i.isupper():
                print("_" + (i.lower()), end ='')
        else:
                print(i, end='')


print()


