def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Runs all Checks
def is_valid(s):
    if max_min_chars(s):
        if  starts_two_letter(s):
            if no_punctuation(s):
                if no_middle_numbers(s):
                    return True

#Checks if the string starts with 2 letters
def starts_two_letter(s):
    if s[0].isdigit() or s[1].isdigit():
        return False
    else:
        return True

#Checks if the string is larger than 2 chars but less than 6
def max_min_chars(s):
    if len(s) > 6 or len(s) < 2:
        return False
    else:
        return True

#Checks if the string contains any punctuation marks
def no_punctuation(s):
    valid = True
    for item in s:
        if item in {",","."," ","!","?","@",":","(",")","%","'"}:
            valid = False

    return valid

#Checks if the string has any numbers inbetween letters
def no_middle_numbers(s):
    valid = True
    found_digit = False
    for item in s:
        if item.isdigit() == True:
            if found_digit == False:
                if item == "0":
                    valid = False
                found_digit = True
        else:
            if found_digit == True:
                valid = False

    return valid


main()
