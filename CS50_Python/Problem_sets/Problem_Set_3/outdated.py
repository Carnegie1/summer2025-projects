def main():

    #loop until a valid date
    while True:
        userDate = input("Date: ").strip()
        format = findFormat(userDate)

        if(format != 0):
             date = validDate(userDate, format)
             if (date != False):
                 print(date)
                 break


def findFormat(userDate):
    splitString1 = userDate.split("/")
    if splitString1[0].isdigit() and splitString1[1].isdigit() and splitString1[2].isdigit():
        return 1
    else:
        splitString2 = userDate.split(" ")
        #Checks if the string is within the months list
        validMonth = splitString2[0].title() in months

        #Splits the "x," by the comma, to check if x is a digit, and vice verse for the comma
        try:
            dayNum = (splitString2[1].split(","))[0]
            validDay = dayNum.isdigit() and (splitString2[1].split(dayNum))[1] == ","

        # If there is no spaces in input, splitString2 has a length of 1
        except IndexError:
            return 0

        #Checks if the year is a digit
        validYear = splitString2[2].isdigit()
        if validMonth and validDay and validYear:
            return 2
        else:
            return 0


def validDate(userDate, dateFormat):
    if dateFormat == 1:
        splitString = userDate.split("/")
        month = splitString[0]
        day = splitString[1]
        year = splitString[2]

    else:
        splitString = userDate.split(" ")
        month = str(months.index(splitString[0].title()) + 1)
        day = splitString[1].split(",")[0]
        year = splitString[2]

    if (int(month) <= 12) and (int(day) <= 31):
        if (int(day) < 10):
            day = str(0) + day
        if (int(month) < 10):
            month = str(0) + month
        return(year + "-" + month + "-" + day)
    else:
        return False




months = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
]


main()
