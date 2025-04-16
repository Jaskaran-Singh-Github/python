# Custom exception for negative numbers
class NegativeNumberError(Exception):
    pass

try:
    # Get input from user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Check for negative numbers
    if num1 < 0 or num2 < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")

    # Perform division
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")
except NegativeNumberError as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")  # Only runs if no exception occurs
finally:
    print("End of program.")  # Always runs


