#Task 1:Creating a class (Abstraction)
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def __str__(self):
        return f"Name: {self.name},Age:{self.age},Gender:{self.gender},Address:{self.address}"
    def greet(self,other_person):
        if isinstance(other_person,Person):
            return f"Hello {other_person.name}! My name is {self.name}."
        return "Invalid person object." 
    @abstractmethod
    def introduce(self):
        pass
    @staticmethod
    def is_adult(age):
        return age >= 18           
#Example child class
class Student(Person):
    def __init__(self,name,age,gender,address,student_id):
        super(). __init__(name,age,gender,address)
        self.student_id=student_id
    def introduce(self):
        return f"Hi,I'm {self.name},a student. My student ID is {self.student_id}."  
#Example usage
john=Student("John",20,"Male","123 Street,City","S12345") 
jane=Student("Jane",19,"Female","456 Avenue,City","S67890")
print(john) # Display basic info
print(jane.greet(john)) # Greeting Example 
print(john.introduce()) # Introduce method from Student class
print(Person.is_adult(20))  # Static method check

#Task 2:Single inheritance ,Encapsulation
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def __str__(self):
        return f"Name: {self.name},Age:{self.age},Gender:{self.gender},Address:{self.address}"
    def greet(self,other_person):
        if isinstance(other_person,Person):
            return f"Hello {other_person.name}! My name is {self.name}."
        return "Invalid person object." 
    @abstractmethod
    def introduce(self):
        pass
    @staticmethod
    def is_adult(age):
        return age >= 18           
#Example child class
class Student(Person):
    def __init__(self,name,age,gender,address,student_id):
        super(). __init__(name,age,gender,address)
        self.student_id=student_id
    def introduce(self):
        return f"Hi,I'm {self.name},a student. My student ID is {self.student_id}."  
class Employee(Person):
    counter=0
    def __init__(self,name,age,gender,address,salary):
        super(). __init__(name,age,gender,address)
        Employee.counter += 1
        self._employee_id=f"EMP{Employee.counter:02d}"
        self._salary=salary
    @property
    def employee_id(self):
        return self._employee_id    
    @property
    def get_counter(cls):
        return cls._counter
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,amount):
        if amount>0:
            self._salary=amount
    def increase_salary(self,amount):
        if amount>0:
            self._salary += amount
    def decrease_salary(self,amount):
        if amount>0 and self._salary-amount>=0:
            self._salary -=amount
    def introduce(self):
        return f"Hi,I'm {self.name},a employee. My Employee ID is {self.employee_id}."
    def delete_employee(self):
        Employee.counter -=1                                   
#Example usage
john=Student("John",20,"Male","123 Street,City","S12345") 
jane=Student("Jane",19,"Female","456 Avenue,City","S67890")
emp1=Employee("Alice",30,"Female","789 Road City",50000)
emp2=Employee("Bob",40,"Male","101 Blvd City",60000)
print(john) # Display basic info
print(jane.greet(john)) # Greeting Example 
print(john.introduce()) # Introduce method from Student class
print(Person.is_adult(20))  # Static method check
print(emp1.introduce()) #Employee introduction
print(emp2.salary) # Access salary
emp2.increase_salary(5000)
print(emp2.salary) #Updated salary

#Task 3:Multiple Inheritance,Polymorphism
from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def __str__(self):
        return f"Name: {self.name},Age:{self.age},Gender:{self.gender},Address:{self.address}"
    def greet(self,other_person):
        if isinstance(other_person,Person):
            return f"Hello {other_person.name}! My name is {self.name}."
        return "Invalid person object." 
    @abstractmethod
    def introduce(self):
        pass
    @staticmethod
    def is_adult(age):
        return age >= 18           
#Example child class
class Student(Person):
    def __init__(self,name,age,gender,address,student_id):
        super(). __init__(name,age,gender,address)
        self.student_id=student_id
    def introduce(self):
        return f"Hi,I'm {self.name},a student. My student ID is {self.student_id}."  
class Employee(Person):
    counter=0
    def __init__(self,name,age,gender,address,salary):
        super(). __init__(name,age,gender,address)
        Employee.counter += 1
        self._employee_id=f"EMP{Employee.counter:02d}"
        self._salary=salary
    @property
    def employee_id(self):
        return self._employee_id    
    @property
    def get_counter(cls):
        return cls._counter
    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,amount):
        if amount>0:
            self._salary=amount
    def increase_salary(self,amount):
        if amount>0:
            self._salary += amount
    def decrease_salary(self,amount):
        if amount>0 and self._salary-amount>=0:
            self._salary -=amount
    def introduce(self):
        return f"Hi,I'm {self.name},a employee. My Employee ID is {self.employee_id}."
    def delete_employee(self):
        Employee.counter -=1
class Teacher(Employee):
    _counter=0
    def __init__(self,name,age,gender,address,salary,subjects=None):
        super(). __init__(name,age,gender,address,salary)
        Teacher._counter +=1
        self._teacher_id=f"TEC{Teacher._counter:02d}"
        self.subjects=subjects if subjects is not None else []
    @property
    def teacher_id(self):
        return self._teacher_id
    @classmethod
    def get_counter(cls):
        return cls._counter
    def add_subject(self,subject):
        if subject not in self.subjects:
            self.subjects.append(subject)   
    def remove_subject(self,subject):
        if subject in self.subjects:
            self.subjects.remove(subject)               
    def introduce(self):
        return f"Hi,I'm {self.name},a teacher. My Teacher ID is {self._teacher_id},and I teach:{', '.join(self.subjects)}."
    @property
    def employee_id(self):
        raise AttributeError("Teacher object has no attribute 'employee_id'. ")    
#Example usage
john=Student("John",20,"Male","123 Street,City","S12345") 
jane=Student("Jane",19,"Female","456 Avenue,City","S67890")
emp1=Employee("Alice",30,"Female","789 Road City",50000)
emp2=Employee("Bob",40,"Male","101 Blvd City",60000)
teach1=Teacher("Eve",35,"Female","202 Lane City",70000,["Maths","Physics"])
print(john) # Display basic info
print(jane.greet(john)) # Greeting Example 
print(john.introduce()) # Introduce method from Student class
print(Person.is_adult(20))  # Static method check
print(emp1.introduce()) #Employee introduction
print(emp2.salary) # Access salary
emp2.increase_salary(5000)
print(emp2.salary) #Updated salary 
print(Teacher.get_counter())   # Get current counter value 
print(teach1.introduce()) # Teacher introduction   