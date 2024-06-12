
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
multiplication_result = num1 * num2

if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "undefined (division by zero)"

print(f"The result of multiplying {num1} and {num2} is: {multiplication_result}")
print(f"The result of dividing {num1} by {num2} is: {division_result}")
