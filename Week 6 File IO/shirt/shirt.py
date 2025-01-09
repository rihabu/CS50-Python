import sys
from os.path import splitext
from PIL import Image, ImageOps
extention =[".png", ".jpg", ".jpeg"]

path_input=splitext(sys.argv[1])
path_output=splitext(sys.argv[2])

#The program should exit via sys.exit:
    #if the user does not specify exactly two command-line arguments,
    #if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
    #if the input’s name does not have the same extension as the output’s name, or
    #if the specified input does not exist.
    
if len(sys.argv)>3:
    sys.exit("Too many command-line arguments")
if len(sys.argv)<3:
    sys.exit("Too few command-line arguments")

if not path_input[1].lower() in extention:
    sys.exit("Invalid input")
if not path_output[1].lower() in extention:
    sys.exit("Invalid output")

if path_input[1].lower() != path_output[1].lower():
    sys.exit("Input and output have different extensions")
else:
    try:
        image_file=Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt_file=Image.open("shirt.png")
#get the width and height, respectively, of that image as a tuple
    size =shirt_file.size
    muppet=ImageOps.fit(image_file,size)
#overlay that image on top of another
    muppet.paste(shirt_file,shirt_file)
    muppet.save(sys.argv[2])

