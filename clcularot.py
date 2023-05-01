
# Simple calculator in Python

# Define a function to perform addition
def add(x, y):
  return x + y

# Define a function to perform subtraction
def subtract(x, y):
  return x - y

# Define a function to perform multiplication
def multiply(x, y):
  return x * y

# Define a function to perform division
def divide(x, y):
  return x / y

# Print a welcome message and instructions
print("Welcome to the simple calculator!")
print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("Enter / for division")
print("Enter q to quit")

# Start a while loop to keep the calculator running
while True:
  # Get the user's choice of operation
  choice = input("Enter your choice: ")

  # Check if the user wants to quit
  if choice == 'q':
    break # Exit the loop

  # Check if the user entered a valid operation
  elif choice in ['+', '-', '*', '/']:
    # Get the first number from the user
    num1 = float(input("Enter the first number: "))
    # Get the second number from the user
    num2 = float(input("Enter the second number: "))

    # Perform the operation and print the result
    if choice == '+':
      print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '-':
      print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '*':
      print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '/':
      print(num1, "/", num2, "=", divide(num1, num2))

  # If the user entered an invalid operation, print an error message
  else:
    print("Invalid choice. Please try again.")

# Print a goodbye message
print("Thank you for using the simple calculator. Goodbye!")
