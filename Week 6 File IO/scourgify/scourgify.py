import sys , csv

#Expects the user to provide two command-line arguments:

#If the user does not provide exactly two command-line arguments,
#or if the first cannot be read, the program should exit via sys.
#exit with an error message.
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<3:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    data=[]
    try:

#the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house,
        with open(sys.argv[1],"r") as before_file:
            for row in csv.DictReader(before_file):
                #splitting each name into a first name and last name.
                name=row["name"].split(",")
                data.append({"first":name[1].lstrip(),"last":name[0],"house":row["house"]})

#the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
        with open(sys.argv[2],"w") as after_file:
            #Convert that input to that output,
            writer = csv.DictWriter(after_file,fieldnames=["first","last","house"])
            writer.writeheader()
            for row in data:
                writer.writerow({"first":row["first"],"last":row["last"],"house":row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read{sys.argv[1]}")



