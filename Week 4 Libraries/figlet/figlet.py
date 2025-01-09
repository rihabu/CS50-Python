import sys,random
from pyfiglet import Figlet

figlet = Figlet()
#get a list of available fonts:
figlet.getFonts()
#Expect zero or two command-line arguments:
#Zero if the user would like to output text in a random font.
if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
#Two if the user would like to output text in a specific font,
#first of the two should be -f or --font,and the second should be the name of the font.
elif sys.argv[1]=="-f" or sys.argv[1]=="--font":
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("Invalid")
#Prompt the user for a str of text.
text=input("Input: ")
print(f"Output: {figlet.renderText(text)}")

