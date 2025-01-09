import sys , csv
from tabulate import tabulate
table=[]
#expect exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format,
#If the user does not specify exactly one command-line argument,
#or if the specified file’s name does not end in .csv,
#or if the specified file does not exist, the program should instead exit via sys.exit.
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1],"r") as csvfile:
            for row in csv.reader(csvfile):
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")
#output a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate.
#Format the table using the library’s grid format.
    print(tabulate(table[1:], headers=table[0], tablefmt="grid"))