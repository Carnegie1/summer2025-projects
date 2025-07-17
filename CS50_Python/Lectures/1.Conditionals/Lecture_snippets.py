x = int(input("What is x ?"))
t = int(input("What is t ?"))


# If statements work using :
if x < t:
    print("X is less than t")
elif x > y: #else if
    print("X is greater than t")
else:
    print("X is equal to t")


if x < t or x > t: # or operator. Not ||
    print("x greater than or less than y")

if x< t and x >t: #and operator. Not &&
    print("Something strange has happened")
# "x< t and x >t" could also be "x < t < x"


#Match works similar to switch
match name:
    case "banana" | "Strawberry"| "Apple":
        print("fruit")
    case "lettuce":
        print("not fruit")
    case _:
        print("I am not sure")


    





