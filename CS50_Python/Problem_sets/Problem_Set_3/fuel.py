
def main():
    #loop until 'valid_valie' returns correctly
    while True:
        userfuel = input("Fraction: ")
        try:
            valid_input = valid_value(userfuel)
            if valid_input != "wrong":
                if valid_input >= 0.99:
                    print("F")
                elif valid_input <= 0.01:
                    print("E")
                else:
                    # round number to 2dp and convert to string
                    valid_input = int(round(valid_input,2)*100)
                    print(str(valid_input) + "%")
                break
            else:
                #continue loop
                pass

        except ValueError:
            print("ValueError")
        except ZeroDivisionError:
            print("ZeroDivisionError")


def valid_value(userInput):
    user_value1, user_value2 = userInput.split("/")
    user_value1 = int(user_value1)
    user_value2 = int(user_value2)


    if user_value2 == 0:
        raise ZeroDivisionError("Attempted divide by 0")
    elif user_value1 < 0:
        raise ValueError

    if (user_value1 > user_value2):
        return "wrong"
    else:
        return user_value1/user_value2




main()
