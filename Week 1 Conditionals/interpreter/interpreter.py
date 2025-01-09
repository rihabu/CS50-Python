#prompts the user for an arithmetic expression
expression = input("Expression: ").strip()

#Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z,
#x is an integer y is +, -, *, or / z is an integer

x_, y, z_ = expression.split(" ")
x = int (x_)
z = int (z_)

#calculates
if y == ("+"):
    f = x + z
elif y == ("-"):
    f = x - z
elif y == ("*"):
    f = x * z
elif y == ("/"):
    f = x / z

#outputs the result as a floating-point value formatted to one decimal place.
print("{:.1f}".format(f))


#if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.