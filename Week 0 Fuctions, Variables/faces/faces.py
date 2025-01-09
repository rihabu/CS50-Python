#implement main function
def main():
    #prompt user for input
    text = input("what's in your mind? ")
    #calls convert on user input
    converted_text = convert(text)
    #prints the result
    print(converted_text)

#implement convert function
def convert(text):
    #replace imojis
    converted_text = text.replace(':)', '🙂').replace(':(', '🙁')
    #return string
    return converted_text

main()