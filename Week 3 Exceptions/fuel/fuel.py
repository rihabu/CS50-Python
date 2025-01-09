#prompt the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer
#If, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
#It is not necessary for Y to be 4
#Be sure to catch any exceptions like ValueError or ZeroDivisionError.
while True :
    fraction = input("Fraction: ")
    try:
        fraction = fraction.split("/")
        x=int(fraction[0])
        y=int(fraction[1])
        if (x/y)<=1:
            break
    except (ValueError, ZeroDivisionError, AttributeError, NameError):
        pass
#output, as a percentage rounded to the nearest integer, how much fuel is in the tank.
if x<=y:
    per = round((x/y)*100)
#if 99% or more remains, output F instead to indicate that the tank is essentially full.
    if per>=99:
        print("F")
#If, 1% or less remains, output E instead to indicate that the tank is essentially empty.
    elif per<=1:
        print("E")
    else:
        print(f"{per}% ")


