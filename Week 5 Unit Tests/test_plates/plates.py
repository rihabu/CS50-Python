def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s.isalnum() and 2 <= len(s) <= 6 and s[0].isalpha() and s[1].isalpha():
        for item in s:
            if item.isdigit():
                index = s.index(item)
                if s[index:].isdigit() and int(item)!=0:
                    return True
                else:
                    return False
        return True

if __name__ == "__main__":
    main()