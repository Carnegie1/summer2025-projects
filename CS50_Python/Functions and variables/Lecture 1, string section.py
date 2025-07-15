# --- LECTURE ONE --- String section

# Taking user input, storing as variable
name = input("What is your name?")

# 'name = name.strip()' removes the whitespace from a string - input sanitisation

# 'name = name.capitalize()' Put a capital letter on the first letter of a string

# 'name = name.title()' Capitalises the first letter of each word that is seprated by a space


# Combining string methods - work the same as previous order. 
name = name.strip().capitalize().title()


#Setting 2 varibles at the same time. Split works the same as java
first, last = name.split(" ")

#printing variable with text - using comma to seperate (Note: adds a space after first argument)
print("Hello," ,first)

# Alternate way of including a variable in a print function. - format string
print(f"Hello, {name}")

#Changing value of end parameter of the print function
print("Test,", " Test2", sep="SEPERATOR", end="???")



