name = "Nicholas"
age = 28
country = "Kenya"
learning_python = True

# Print initial info
print(f"My name is {name}.")
print(f"I am {age} years old.")
print(f"I live in {country}.")
print(f"I am learning Python: {learning_python}")

# Get user input with clear prompts
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Hello {name}")
print(f"Next year you will be {age + 1}")

# Calculator section
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)