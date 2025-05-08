"""Write a python code to take 2 numbers and form a calculator
add
sub
mul
div
remainder
quotient
exponent
"""

number1 = 59
number2 = 79
enter = input("Enter: ")
if enter == "+":
    print(number1+number2)
elif enter == "-":
    print(number1-number2)
elif enter == "*":
    print(number1*number2)
elif enter == "/":
  print(number1/number2)
elif enter == "%":
  print(number1%number2)
elif enter == "**":
  print(number1**number2)
elif enter == "//":
  print(number1//number2)
else:
  print("Invalid Output")
