
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

#vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
#No periods, spaces, or punctuation marks are allowed
#All vanity plates must start with at least two letters
    if s.isalnum() and 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
#Numbers cannot be used in the middle of a plate; they must come at the end.
#For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
#The first number used cannot be a ‘0’
        for item in s:
            if item.isdigit():
                index = s.index(item)
                if s[index:].isdigit() and int(item)!=0:
                    return True
                else:
                    return False
        return True


main()