# print("Hello world!")
# print("Hey i am good boy\ni am jaskaran singh")
# print(2*3)
# hey this is comment
#VARIABLES AND DATA TYPE
# a=167
# print(a)
# b="Jaskaran singh"
# print(b)
# a_1=578
# print(a+a_1)
# print(type(a))
# print(type(b))
# c=complex(10,100)
# print(c,type(c))
# c_1=True
# print(c_1,type(c_1))
# c_2=False
# print(c_2,type(c_2))
# a=[1,2,3,4,5,6,7,8,9,10]
# print(a,type(a))
# b=(1,2,3,4,5,6,7)
# print(b,type(b))
# c={"Name":"Jaskaran","age":20,"canvote":True}
# print(c,type(c))


#IMPORTANT POINT
#PYTHON MAIN SUB KUCH OBJECT HAI
#Typecasting
# a="1"
# b="2"
# print(int(a)+int(b))
# print(float(a)+float(b))
# c=18.77
# d=88
# print(c+d)

#USER INPUT
# a=input("Enter a name:")
# print(a)

# x=input("Enter a number:")
# y=input("Enter a number:")
# print(x+y)
# print(float(x)+int(y))

#STRINGS IN PYTHON IMMUTABLE
# name='Jaskaran singh'
# friend="Gurleen kaur"
# anotherfriend="Tajinder kaur"
# print("hi,"+friend)
# print(name[0])
# print("Let use for loop\n")
# for character in anotherfriend:
#     print(character)

#STRING SLICING
# names="jaskaran,tajinder"
# print(names[0:5])
# nm="Harry"
# # print(nm[-4:-2])
# print(nm[::-1])
#STRINGS OPERATIONS.

#STRINGS ARE IMMUTABLE.
# a="!!Tajinder kaur!!!!!!!!! Tajinder kaur"
# print(len(a))
# print(a)
# print(a.upper())
# print(a.lower())
# print(a.rstrip('!'))
# print(a.replace("Tajinder kaur","Jaskaran Singh"))
# print(a.split(" "))
# a="i am a goOd Boy"
# print(a.capitalize())
# a="Welcome to a new python course"
# print(len(a))
# print(len(a.center(50)))
# b="Harry Harry Harry"
# print(b.count("Harry"))
# b="Welcome!!!!"
# print(b.endswith("!"))
#st="Hello This Is A New Programming Course And It Is Very Helpful."
# print(st.find("it"))
# print(st.index("very"))
# a="WelcomeToTheConsole"
# print(a.isalnum())
# b="welcome"
# print(b.isalpha())
# print(b.islower())
# c="    "
# print(c.isspace())
# a="hello\n"
# print(a.isprintable())
# c="Hello"
# print(c.istitle())
# print(c.isupper())
# print(c.startswith("Hello"))
# print(c.swapcase())
# print(c.title())
# IF-ELSE STATEMENTS
#conditional statement
# <,>,<=,>=,==,!=
# a=int(input("Enter your age:"))
# print("Your age is:",a)
# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a!=18)
# if(a>18):
#     print("Right to Vote")
# else:
#     print("Not Vote") 
# print("Yay!")
# pen=20
# rup=5
# if(pen<rup):
#     print("Buy")
# else:
#     print("Not Buy")    
#ELIF STATEMENT
# num=int(input("Enter a number:"))
# if(num<0):
#     print("Negative")
# elif(num==0):
#     print("Zero")
# elif(num==999):
#     print("Special Number")    
# else:
#     print("Positive")       
# print("I am happy now")
#NESTED IF STATEMENT
# num=int(input("Enter a number:"))
# if(num<0):
#     print("Negative")
# elif(num>0):
#     if(num<=10):
#         print("1 to 10")
#     elif(num>10 and num<=20):
#         print("11 to 20")
#     else:
#         print("Greater than 20")
# else:
#     print("Number is zero")  
# MATCH CASE STATEMENTS
# x=int(input("Enter the value of x:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 1:
#         print("x is 1")
#     case 2:
#         print("x is 2")     
     
 #FOR LOOPS
# x="Jaskaran"
# for i in x:
#     print(i)
# for i in range(10):
#     print(i+1)

# for i in range(1,100):
#     print(i) 
# colors=['Red','Green','Blue','Pink','Orange']
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
# for i in range(1,15,3):
#     print(i)

#WHILE LOOPS
# i=0
# while(i<=3):
#     print(i)
#     i=i+1
# print("Hello")  
 

# i=int(input("Enter a number:"))
# while(i<=50):
#     i=int(input("Enter a number:"))
#     print(i)   
# print("Out of the loop") 

# count=1000
# while(count>0):
#     print(count)
#     count=count-1
# else:
#    print("Hello I am inside the else part")
#BREAK AND CONTINUE
# for i in range(12):
#     if(i==10):
#         break
#     print("5 X",i+1,"=",5*(i+1))
# print("Loop se bahar aajo")    

# for i in range(12):
#     if(i==10):
#         print("Skip the iteration")
#         continue
#     print("5 X",i,"=",5*i)
#DO-WHILE LOOP
# i=0
# while True:
#     print(i)
#     i=i+1
#     if(i%100==0):
#         break
#FUNCTIONS
#WITHOUT FUNCTIONS.
# a=9
# b=8
# gmean=(a*b)/(a+b)
# print(gmean)
# c=8
# d=7
# gmean=(c*d)/(c+d)
# print(gmean)
#WITH FUNCTIONS.
# def calculateGmean(a,b):
#     gmean=(a*b)/(a+b)
#     print(gmean)
# def isGreater(a,b):
#     if(a>b):
#         print("First number is Greater") 
#     else:
#         print("Second number is Greater or Equal")       
# def isLesser(a,b):
#     pass
# a=9
# b=8
# isGreater(a,b)
# calculateGmean(a,b)
# c=8
# d=76
# isGreater(c,d)
# calculateGmean(c,d)

#FUNCTION ARGUMENTS
# def average(a,b):
#     print("The Average of:",(a+b)/2)
# average(4,6)    
# def average(*numbers):
#     print(type(numbers))
#     for i in numbers:
#         sum=0
#         sum=sum+i
#     print("The average is",sum/len(numbers))
# average(10,10,10,10,10)  

# def average(a,b):
#     print("The Average of:",(a+b)/2)
# average(4,6)    
# def average(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum+i
#     #print("The average is",sum/len(numbers))
#     return sum/len(numbers)
# c=average(5,6,7,1)  
# print(c)
#LISTS            MUTABLE
# marks=[10,20,30,40,"Jaskaran Singh",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
#NEGATIVE INDEXING
# print(marks[-3])
# print(marks[6-3])
# print(marks[len(marks)-3])
# print(marks[3])
# if "Jaskaran Singh" in marks:
#     print("Yes")
# else:
#     print("No") 
# if "Jas" in "Jaskaran":
#     print("Yes")
# else:
#     print("No")    
#SLICING
# print(marks)
# print(marks[:])
# print(marks[1:6])
# print(marks[1:6:2])
#LIST COMPREHENSION
# lst=[i*i for i in range(10)]
# print(lst)
# lst=[i*i for i in range(10) if i%2==0]
# print(lst)
#LIST METHODS
# a=[1,2,3,4,5,6,7,57]
# print(a)
# a.append(8)
# a.sort()
# a.reverse()
# a.sort(reverse=True)
# print(a.index(1))
# print(a.count(1))
# m=a.copy()
# m[0]=0
# a.insert(1,90)
# m=[900,1000,1100]
# k=a+m
# print(k)
#a.extend(m)
# print(a)
# #TUPLES      IMMUTABLE
# tup=(1,2,3,"Gurleen",True)
# print(type(tup),tup)
# tup=(1,)
# print(type(tup),tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[3])
# print(tup[4])
# print(len(tup))
#print(tup[5])
#TUPLES OPERATIONS
# COUNT METHOD,INDEX METHOD,LENGTH METHOD
# tup=(1,1,1,2,3,4,5,6,6,7)
# a=tup.count(6)
# print("Count of 1 in tup is:",a)


