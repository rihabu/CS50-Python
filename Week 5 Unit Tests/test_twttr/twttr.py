def main():
    #prompt user text
    text = input("Input: ")
    #output text without vowels
    output = shorten(text)
    print ("Output:",output)

def shorten(text):
    #omitt vowels whether inputted in uppercase or lowercase
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    #iterate on each character of the input string
    for char in text:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    main()





