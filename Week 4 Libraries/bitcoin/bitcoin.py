import sys
import requests
import json
def main():
    #Expect user to specify as a command-line argument the number of Bitcoins that they would like to buy
    bitcoin_num = sys.argv [1]
    #If that argument cannot be converted to a float, exit program via sys.exit with an error message
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument ")
    elif is_float(bitcoin_num) == False:
        sys.exit("Command-line argument is not a number")
    else:
        bitcoin_num=float(sys.argv[1])
        #Query the API for the CoinDesk Bitcoin Price Index
        try:
            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            bitcoin_dict = response.json()
            #Current price of Bitcoin as a float
            bitcoin_price = bitcoin_dict["bpi"]["USD"]["rate_float"]

            #Output the current cost of n Bitcoins, format USD to four decimal places with a thousands separator
            print(f"${bitcoin_num * bitcoin_price:,.4f}")
        except requests.RequestException:
            sys.exit(1)

#define function to check if input can be turned to float
def is_float(bitcoin_num):
    if bitcoin_num.replace(".", "").isnumeric():
        return True
    else:
        return False
    
if __name__ == "__main__":
    main()