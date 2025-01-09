#prompt the user for a str of text
text = input("Input: ")

#omitt vowels whether inputted in uppercase or lowercase
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = ""
#iterate on each character of the input string
for char in text:
    if char not in vowels:
        result += char
#output text without vowels
print ("Output:",result)