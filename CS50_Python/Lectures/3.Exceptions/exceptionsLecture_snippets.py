
def main():
    x = get_int()
    print(f"x is {x}")



    

def get_int():
    while True:
        # Try-catch block in python
        try:
            x = int(input("what is x? "))
        except ValueError:
            print("x is not an integer")
            # you could write 'pass' to do nothing
        else:
            return x



# Put code that may throw an error in 'try'
# Put what to do if an error is thwon in 'except'
# Put what to do if no error is thrown in 'else'
