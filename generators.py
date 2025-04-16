# Generator for Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(list(fibonacci(10)))  # First 10 Fibonacci numbers

# Generator for prime numbers up to n
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    for num in range(2, n + 1):
        if is_prime(num):
            yield num

print(list(prime_numbers(100)))  # Primes up to 100

# Generator for words in a string
def word_generator(text):
    for word in text.split():
        yield word

sentence = "The quick brown fox jumps over the lazy dog"
print(list(word_generator(sentence)))  # Extracted words

# Generator for unique words in a list
def unique_words(words):
    seen = set()
    for word in words:
        if word.lower() not in seen:
            seen.add(word.lower())
            yield word

word_list = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(list(unique_words(word_list)))  # Unique words

# Generator for sublists of length n
def sublists(lst, n):
    for i in range(len(lst) - n + 1):
        yield lst[i:i+n]

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(sublists(num_list, 3)))  # Sublists of length 3