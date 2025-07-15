#Global variable
globalVar = "Global"

# Python syntax for defining a function
# The ="world" is setting a default value for the parameter. The value it takes if none provided
def  hello(name="world"):
   return("Hello, " + name + "!")



# Defining the main function, allows function placement anywhere.
# (without this, functions must come before where they are used)
def main():
    #Line of code needed to specify when a function can modify a global variable
    global globalVar
    
    name = input("What is your name")
    print(hello(name))
    


main()

    
