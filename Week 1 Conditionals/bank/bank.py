#prompt the user for a greeting
#Ignore any leading whitespace in the user’s greeting,
#and treat the user’s greeting case-insensitively
greeting = input("greeting: ").lower().strip()

#If the greeting starts with “hello”, output $0.
#give $0 for also “hello there”, “hello, Newman”, and the like
if "hello" in greeting or greeting.startswith("hello"):
    print("$0")

#If the greeting starts with an “h” (but not “hello”), output $20.
elif greeting.startswith("h") and greeting != "hello":
    print("$20")

#Otherwise, output $100.
else:
    print("$100")
