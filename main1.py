print("Jaskaran Singh")
#this is a python programming language

#Lists
colleges=['IIT','NIT','College of engineering']
print(colleges)
print(colleges[0])
colleges[2]="COE"
print(colleges)
print(colleges[1:3])
lis2=['table','car','fan','mobile']
#lis2.append('fridge')
#print(lis2)
#lis2.insert(4,'tube')
#print(lis2)
lis2.remove('fan')
print(lis2)
print(lis2+['bed','sofa','utensisls'])
print(lis2)
print(len(lis2))
print(max(lis2))
print(min(lis2))

#Tuples
tup1=(1,2,3)
print(tup1[0])
#dictionaries
dic1={'Ram':22,'Rohit':40,
      'Jas':21}
print(dic1['Jas'])


#if else statement
print("Input a number:")
number=int(input())
if(number>90 and number<100):
    grade='A'
elif(number>80 and number<100):
    grade='B'
else:
    grade='not exit'
print('the grade is equal to:',grade)

#loops
print('How many times your loop will be execute:')
st=int(input())
for i in range(0,st):
    print(i)
#while loops
print('Enter a number:')
print(int(input()))
while(number>4):
    print('number is greater than 4',)
    print(int(input()))
    #if(number==9):
        #break
    #if(number==8):
        #continue
    #print('loop ended')

#average
def average(num1,num2):
    return(num1+num2)/2
print(average(5,5))










