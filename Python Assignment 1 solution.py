#Task-1 LISTS


#Solution 1
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
numbers = [2, 3, 4, 5]
print("Product of all elements:", multiply_list(numbers))

#Solution 2
def find_largest_number(numbers):
    if not numbers:
        return None
    return max(numbers)
num_list = [10, 25, 78, 34, 99, 15]
largest = find_largest_number(num_list)
print(f"The largest number is: {largest}")

#Solution 3
numbers = [5, 2, 8, 1, 9]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

#Solution 4
def sort_by_last_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[-1])
tuple_list = [(1, 3), (3, 2), (2, 4), (5, 1)]
sorted_list = sort_by_last_element(tuple_list)
print("Sorted List:", sorted_list)

#Solution 5
my_list = [1, 2, 2, 3, 4, 4, 5,8,9,10]
unique_list = list(set(my_list))
print(unique_list)

#Solution 6
my_list = []

if not my_list:
    print("The list is empty")
else:
    print("The list is not empty")

#Solution 7
def count_lowercase_letters(words):
    return sum(sum(1 for char in word if char.islower()) for word in words)
word_list = ["Hello", "world", "Python", "is", "Awesome"]
lowercase_count = count_lowercase_letters(word_list)
print("Total lowercase letters:", lowercase_count)

#Solution 8
from collections import Counter

def extract_consecutive_elements(lst, n):
    counts = Counter(lst)
    return [key for key, value in counts.items() if value >= n]

# Example usage
lst1 = [1, 1, 3, 4, 4, 5, 6, 7]
lst2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]

print(extract_consecutive_elements(lst1, 2))
print(extract_consecutive_elements(lst2, 4))

#Solution 9
def largest_odd_number(lst):
    odds = [num for num in lst if num % 2 != 0]
    return max(odds) if odds else None


print(largest_odd_number([0, 9, 2, 4, 5, 6]))
print(largest_odd_number([-4, 0, 6, 1, 0, 2]))
print(largest_odd_number([1, 2, 3]))
print(largest_odd_number([-4, 0, 5, 1, 0, 1]))

#Solution 10
def remove_elements(lst):
    return [lst[i] for i in range(len(lst)) if i not in (0, 4, 5)]
sample_list = ['A', 'B', 'C', 'D', 'E', 'F']
print(remove_elements(sample_list))


#Task-2 TUPLES
#Solution 1
my_tuple = (10, 3.14, "Hello", True, [1, 2, 3], (4, 5, 6), {'a': 1, 'b': 2})
print(my_tuple)
print([type(item) for item in my_tuple])

#Solution 2
numbers_tuple = (10, 20, 30, 40, 50)
print(numbers_tuple[0])

#Solution 3
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)
print(new_tuple)
#Solution 4
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80)
fourth_from_last = my_tuple[-4]
print(fourth_from_last)

#Solution 5
my_tuple = (("a", 1), ("b", 2), ("c", 3))
my_dict = dict(my_tuple)
print(my_dict)

#Solution 6
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
updated_list = [t[:-1] + (100,) for t in sample_list]
print(updated_list)


#Task-3 DICTIONARY
#Solution 1
my_dict = {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}
asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Ascending order:", asc_sorted)
print("Descending order:", desc_sorted)


#Solution 2
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Solution 3
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

#Solution 4
my_dict = {'a': 10, 'b': 20, 'c': 30}
total_sum = sum(my_dict.values())
print("Sum of all values:", total_sum)

#Solution 5
my_dict = {'a': 2, 'b': 3, 'c': 4}
product = 1
for value in my_dict.values():
    product *= value
print("Product of all values:", product)

#Solution 6
my_dict = {'b': 3, 'a': 1, 'c': 2}
sorted_dict = dict(sorted(my_dict.items()))
print("Sorted dictionary by key:", sorted_dict)

#Solution 7
my_dict = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 1}
unique_dict = {}
for key, value in my_dict.items():
    if value not in unique_dict.values():
        unique_dict[key] = value
print("Dictionary after removing duplicates:", unique_dict)

#Task 4 NUMPY
#1: Numpy array creation and manipulation
#Solution 1



