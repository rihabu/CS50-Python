from validator_collection import validators

def main():
    user_email=input("What's your email address? ")
    try:
        valid_email = validators.email(user_email)
        if valid_email:
            print("valid")
    except:
        print("invalid")
if __name__ == "__main__":
    main()