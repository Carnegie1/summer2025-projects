equation = input("Expression: ")
equation_split = equation.split()

x = float(equation_split[0])
y = equation_split[1]
z = float(equation_split[2])

match y:
    case "+":
        output = x + z
    case "-":
        output = x - z
    case "/":
        output = x / z
    case "*":
        output = x*z

print(output)
