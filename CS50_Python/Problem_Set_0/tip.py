#Takes in an input in dollars like %50.00, converts to float and integer and prints
# an appripriate tip
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    Dnew = d.replace("$","")
    Dnum = float(Dnew)
    return Dnum

def percent_to_float(p):
    Pnew = p.replace("%","")
    Pnum = (float(Pnew))
    Pnum = Pnum/100
    return Pnum


main()
