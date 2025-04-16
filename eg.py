# def print_decreasing(n):
#     if n == 0:  # Base case: Stop when n reaches 0
#         return
#     print(n)  # Print the current number
#     print_decreasing(n - 1)  # Recursive call with n-1

# # Example usage
# N = int(input("Enter a number: "))
# print_decreasing(N)

# def print_increasing(n, current=1):
#     if current > n:  
#         return
#     print(current) 
#     print_increasing(n, current + 1) 

# # Example usage
# N = int(input("Enter a number: "))
# print_increasing(N)

# def fibonacci(n):
#     if n <= 1:
#         return n  
#     return fibonacci(n - 1) + fibonacci(n - 2) 

# N = int(input("Enter N: "))
# print(f"The {N}th Fibonacci number is:", fibonacci(N))

# def power(a, n):
#     if n == 0:  
#         return 1
#     return a * power(a, n - 1) 

# # Example usage:
# A = int(input("Enter base (A): "))
# N = int(input("Enter exponent (N): "))
# print(f"{A}^{N} =", power(A, N))
