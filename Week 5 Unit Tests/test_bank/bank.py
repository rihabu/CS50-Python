def main():

    #prompt the user for a greeting, Ignore any leading whitespace and treat case-insensitively
    greeting = input("greeting: ").lower().strip()
    
    #output amount
    output=value(greeting)
    print(f"${output}")

def value(greeting):

    #If the greeting starts with “hello”, output $0. give $0 for also “hello there”, “hello, Newman”, and the like
    if "hello" in greeting or greeting.startswith("hello"):
        return 0

    #If the greeting starts with an “h” (but not “hello”), output $20.
    elif greeting.startswith("h") and greeting != "hello":
        return 20

    #Otherwise, output $100.
    else:
        return 100


if __name__ == "__main__":
    main()




