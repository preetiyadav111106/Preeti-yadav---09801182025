#Create a function to print first 10 natural numbers.
def print_natural_numbers():
    for i in range(1,11):
        print(i)

# Create a function to calculate sum of first N natural numbers.
def find_sum(n):
    return n*(n+1)//2
n = int(input("Enter the value of N:"))
print("sum of first",n,"natural numbers =", find_sum(n))

# Create a function to reverse a number.
def reverse_number(num):
    return(int(str(num)[::-1]))

n = int(input("Enter a number:"))
print("Reversed number:",reverse_number(n))

#create a function to count digits in a number.
def count_digits(n):
    return len(str(n))
n = int(input("Enter a number:"))
print("Number of digits:",count_digits(n))

#Create a function to check palindrome number.
def is_palindrome(num):
    rev = int(str(num)[::-1])
    return num == sum
n = int(input("Enter a number:"))
if is_palindrome(n):
    print("Palindrome number")
else:
    print("Not a palindrome number")

#Create a function to generate Fibonacci series.
def fibonacci(n):
    a,b = 0,1
    for i in range(n):
        print(a,end="")
        a,d = b,a+b
n = int(input("Enter a number of terms:"))
fibonacci(n)

#Calculator using Functions that contains the following features.
#user selects operation
#program performs calculations 
#display result

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def devide(a,b):
    return a/b
print("Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter your choice(1-4): "))
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if choice == 1:
    print("Result=",add(num1,num2))
elif choice == 2:
    print("Result=",subtract(num1,num2))
elif choice == 3:
    print("Result=",multiply(num1,num2))
elif choice == 4:
    print("Result=",divide(num1,num2))
else:
    print("invalid choice")

# Create a text file and store student details.
name = input("Enter your name:")
roll_no = int(input("Enter your roll number:"))
course = input("Enter course:")
file = open("student.txt","w")

file.write("Student Details\n")
file.write("Name:"+ name +"\n")
file.write("Roll No:"+ roll_no +"\n")
file.write("Course:"+ course + "\n")
file.close()
print("student details saved successfully")

#Read data from a file.
file = open("student.txt", "r")
data = file.read()
print(data)
file.close()

# Handle division by zero using exception handling.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 / num2
print("Result =", result)

exceptZeroDivisionError:
print("Error: Division by zero is not allowed.")

#Create a student class with name and marks.
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("preeti", 95)
s1.display()



          


