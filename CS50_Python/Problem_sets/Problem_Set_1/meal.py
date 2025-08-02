def main():
    time = input("What time is it? ").strip()
    integerTime = convert(time)

    if  8 >= integerTime >= 7:
        print("breakfast time")
    elif 13 >= integerTime >= 12:
        print("lunch time")
    elif 19 >= integerTime >= 18:
        print("dinner time")




# Converts #:## or ##:## to decimal (e.g 7.30 --> 7.5)
def convert(time):
    if len(time) == 4:
        hours = float(time[0])
        minutes = float(time[2] + time[3])/0.6
    elif len(time) == 5:
        hours = float(time[0] + time[1])
        minutes = float(time[3] + time[4])/0.6

    return(hours + minutes/100)




if __name__ == "__main__":
    main()
