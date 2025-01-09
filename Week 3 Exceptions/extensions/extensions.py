#prompts the user for the name of a file
file = input("File name: ").lower().strip()

#output that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:
#.gif
if file.endswith(".gif"):
    print("image/gif")
#.jpg or.jpeg
elif file.endswith(".jpeg") or file.endswith(".jpg"):
    print("image/jpeg")
#.png
elif file.endswith(".png"):
    print("image/png")
#.pdf
elif file.endswith(".pdf"):
    print("application/pdf")
#.txt
elif file.endswith(".txt"):
    print("text/plain")
#.zip
elif file.endswith(".zip"):
    print("application/zip")

#If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead
else:
    print("application/octet-stream")