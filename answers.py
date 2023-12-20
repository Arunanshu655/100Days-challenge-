# 1 Print Hello
def printHello() :
    print("Hello World");

printHello()

# 2 funtion to find sum of two numbers 

def sumOf2() :
    a = int(input("enter first number:"))
    b = int(input("enter second number:"))
    print("The sum is :",a+b)

sumOf2()

# 3 program to swap two values

def swap() :
    x = input("enter first number as x:")
    y = input("enter second number as y:")
    x,y = y,x 
    print("now the x is :",x)
    print("now the y is :",y)

swap()

# 4 Detect the is odd or even

a = int(input("Enter the number :- "))
if (a % 2 == 0 ):
    print("The given number is even")
else:
    print("The given number is odd")

# 5 simple calculator for (+,-,/,*)

    a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
op = input("Enter the operator(+,-,*,/) : ")
if (op == '+') :
    print("The answer is =",a+b)
elif (op == '-') :
    print("The answer is =",a-b)
elif (op == '*') :
    print("The answer is =",a*b)
elif (op == '/') :
    print("The answer is =",a/b)

# 6 print prime numbers from 1 to 100

for i in range(1,101):
    count = 0 
    for j in range(1,i+1) :
        if (i % j == 0) :
            count = count + 1
    if(count == 2 ):
        print(i)
             
            
    