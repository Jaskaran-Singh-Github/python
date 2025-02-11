#Problem 1
n=int(input("Input:"))
squares=[]
for i in range(n):
    squares.append(i**2)
print("Output:",squares)

#Problem 2
n=(input("Enter a string:"))
result=""
for char in n:
    if char not in result:
        result+=char
print("string after removing duplicates:",result)

#Problem 3
numbers=[12,75,150,180,145,525,50]
result=[]
for num in numbers:
    if num>500:
        break
    if num>150:
        continue
    if num%5==0:
        result.append(num)
print(result)

#Problem 4
number=int(input("Enter a number:"))
count=0
while number !=0:
    number=number//10
    count+=1
print("Total number of digits:",count)

#Problem 5
n=int(input("Enter the number of terms:"))
current_term=0
total_sum=0
for i in range(n):
    current_term=current_term*10+2
    total_sum+=current_term
print("The sum of the series is:",total_sum)

#Problem 6
number=int(input("Enter a number:"))
reversed_number=0
while number>0:
    digit=number%10
    reversed_number=reversed_number*10+digit
    number=number//10
print("Reversed number:",reversed_number)

#Problem 7
numbers=[10,20,30,40,50,60,70,80,90,100]
odd_index_elements=[]
for i in range(1,len(numbers),2):
    odd_index_elements.append(numbers[i])
print("Output:",odd_index_elements)

#Problem 8
num1=int(input("Input a first number:"))
num2=int(input("Input a second number:"))
num3=int(input("Input a third number:"))
numbers=[num1,num2,num3]
numbers.sort()
median=numbers[1]
print("Output:",median)