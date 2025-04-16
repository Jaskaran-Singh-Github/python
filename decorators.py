import time

# Decorator to convert output to uppercase
def uppercase_decorator(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

# Function to return a greeting
def say_hello(name):
    return f"Hello, {name}!"

# Applying the decorator
greet = uppercase_decorator(say_hello)

# Testing the decorated function
print(greet("Jas"))  # Output: HELLO, ALICE!

# Decorator to measure execution time
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.5f} seconds")
        return result
    return wrapper

# Applying the timing decorator
timed_greet = timing_decorator(greet)

# Testing the timed function
print(timed_greet("Gur"))

# Decorator to log function calls
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' called with arguments {args} → Result: {result}")
        return result
    return wrapper

# Class with methods decorated with logging
class Math:
    @logging_decorator
    def add(self, a, b):
        return a + b

    @logging_decorator
    def subtract(self, a, b):
        return a - b

# Testing the decorated class methods
math = Math()
math.add(5, 3)
math.subtract(10, 4)