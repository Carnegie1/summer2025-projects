# Using E = mc^2 formula, user inputs the m

def einstein(number):
    result = int(number)*(300000000**2)
    return result


def main():
    userNum = input("Enter a number: ")
    userEinstein = einstein(userNum)
    print(userEinstein)

main()
