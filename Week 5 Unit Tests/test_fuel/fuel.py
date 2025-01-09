def main():

    print(gauge(convert(fraction = input("Fraction: "))))

def convert(fraction):
    fraction = fraction.split("/")
    x=int(fraction[0])
    y=int(fraction[1])
    if (x/y)<=1:
        return round((x/y)*100)
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        raise ValueError

def gauge(per):
    if per>=99:
        return"F"
    elif per<=1:
        return"E"
    else:
        return f"{per}% ")


if __name__ == "__main__":
    main()
