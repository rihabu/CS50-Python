#prompt the user for a time
#Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
def main():
    time = input("what time is it? ")
    converted_time = convert(time)

#assume that each meal’s time range is inclusive.
#output whether it’s breakfast time, lunch time, or dinner time.
    if  7 <= converted_time <= 8 :
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
#not time for a meal, don’t output anything at all.
    else :
        print("")

#convert is a function that converts a str in 24-hour format,to the corresponding number of hours as a float.
#For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
#Keep in mind that there are 60 minutes in 1 hour.
def convert(time):
    hours, minutes = time.split(":")
    time_f = float(hours) + float(minutes) / 60
    return time_f

if __name__ == "__main__":
    main()

