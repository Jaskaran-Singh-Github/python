# import gradio as gr

# def greet(name, intensity):
#     return "Hello, " + name + "!" * int(intensity)

# demo = gr.Interface(
#     fn=greet,
#     inputs=["text", "slider"],
#     outputs=["text"],
# )

# demo.launch()


import gradio as gr
import numpy as np

def predict_weather(temperature, humidity, pressure):
    """Dummy weather prediction function."""
    if humidity > 80 and temperature < 20:
        return "Rainy"
    elif temperature > 30:
        return "Sunny"
    else:
        return "Cloudy"

with gr.Blocks() as demo:
    gr.Markdown("## Weather Prediction App")
    
    with gr.Row():
        temperature = gr.Slider(minimum=-10, maximum=50, label="Temperature (°C)")
        humidity = gr.Slider(minimum=0, maximum=100, label="Humidity (%)")
        pressure = gr.Slider(minimum=900, maximum=1100, label="Pressure (hPa)")
    
    predict_button = gr.Button("Predict Weather")
    output = gr.Textbox(label="Predicted Weather")
    
    predict_button.click(predict_weather, inputs=[temperature, humidity, pressure], outputs=output)

demo.launch()




# import time

# # Decorator to convert output to uppercase
# def uppercase_decorator(func):
#     def wrapper(name):
#         return func(name).upper()
#     return wrapper

# # Function to return a greeting
# def say_hello(name):
#     return f"Hello, {name}!"

# # Applying the decorator
# greet = uppercase_decorator(say_hello)

# # Testing the decorated function
# print(greet("Alice"))  # Output: HELLO, ALICE!

# # Decorator to measure execution time
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Execution time: {end_time - start_time:.5f} seconds")
#         return result
#     return wrapper

# # Applying the timing decorator
# timed_greet = timing_decorator(greet)

# # Testing the timed function
# print(timed_greet("Bob"))

# # Decorator to log function calls
# def logging_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f"Function '{func.__name__}' called with arguments {args} → Result: {result}")
#         return result
#     return wrapper

# # Class with methods decorated with logging
# class Math:
#     @logging_decorator
#     def add(self, a, b):
#         return a + b

#     @logging_decorator
#     def subtract(self, a, b):
#         return a - b

# # Testing the decorated class methods
# math = Math()
# math.add(5, 3)
# math.subtract(10, 4)



# # Generator for Fibonacci sequence
# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         yield a
#         a, b = b, a + b

# print(list(fibonacci(10)))  # First 10 Fibonacci numbers

# # Generator for prime numbers up to n
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def prime_numbers(n):
#     for num in range(2, n + 1):
#         if is_prime(num):
#             yield num

# print(list(prime_numbers(100)))  # Primes up to 100

# # Generator for words in a string
# def word_generator(text):
#     for word in text.split():
#         yield word

# sentence = "The quick brown fox jumps over the lazy dog"
# print(list(word_generator(sentence)))  # Extracted words

# # Generator for unique words in a list
# def unique_words(words):
#     seen = set()
#     for word in words:
#         if word.lower() not in seen:
#             seen.add(word.lower())
#             yield word

# word_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
# print(list(unique_words(word_list)))  # Unique words

# # Generator for sublists of length n
# def sublists(lst, n):
#     for i in range(len(lst) - n + 1):
#         yield lst[i:i+n]

# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list(sublists(num_list, 3)))  # Sublists of length 3



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


