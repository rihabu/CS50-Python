import sys

#expect exactly one command-line argument, the name (or path) of a Python file,
#If the user does not specify exactly one command-line argument,
# or if the specified file’s name does not end in .py,
# or if the specified file does not exist,
# the program should instead exit via sys.exit.
if len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")
if not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")
else:
    try:
        file = open(sys.argv[1],"r")
        lines = file.readlines()
        line_num = 0
        for line in lines:
#Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
#Assume that any line that only contains whitespace is blank.
            if not line.isspace() and not line.lstrip().startswith("#"):
                line_num +=1
#output the number of lines of code in that file, excluding comments and blank lines.
        print(line_num)
    except FileNotFoundError:
        sys.exit("File does not exist")

