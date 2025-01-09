#list of months:
months = ["January","February","March","April","May","June","July","August","September","October","November","December"]

while True:
#prompt user for a date, anno Domini, in month-day-year order,
#formatted like 9/8/1636 or September 8, 1636,
    date= input("Date: ").strip()

    try:
        if date[0].isdigit():
            month,day,year = date.split("/")
            if 1<=int(month)<=12 and 1<=int(day)<=31:
                 print(f"{year}-{int(month):02}-{int(day):02}")
                 break
    except ValueError:
        pass
    try:
        if not date[0].isdigit() and "/" not in date:
            month_day,year = date.split(",")
            month,day = month_day.split(" ")
            year=year.lstrip()

            if 1<=int(months.index(month)+1)<=12 and 1<=int(day)<=31:
                    print(f"{year}-{int(months.index(month)+1):02}-{int(day):02}")
                    break
    except (ValueError,IndexError) :
            pass

 #If the user’s input is not a valid date in either format, prompt the user again.
#output that same date in YYYY-MM-DD format


