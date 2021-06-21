#python program fibonic
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci seies: ",end= " ")
while(count <= n):
    print(sum, end = " ")
    count += 1
    a = b
    b = sum
    sum = a+b

#Explain Armstrong number and write a code with a function
num = int(input('Enter a number: '))
num_original = num2 = num
sum1 = 0
cnt = 0
while num2>0:
    rem = num2% 10
    sum1 += rem ** cnt
    num2//=10
if(num_original==sum1):
    print('Armstrong!!')
else:
    print('Not Armstrong!')

#3 Write a program to print the Mulitiple table 9
num = int(input('Enter the number : '))
print("Multiplication Table of : ")
for i in range(1,11):
    print(num,'x',i,'=',num*i)

#4,Check if a progrram is neegative or positive
num = float(input("Enter a number: "))
if(num > 0):
    print("Positive number")
elif (num == 0):
    print("Zero")
else:
    print("Negative number")

#6,Write a program to convert the number of days to ages
Days = 365
years = Days / 365
print("Number of years is: ");
print(years);

#5,Slove Trigonomentry problems using with fuction write a program to solve using math function
import math
x = 0.75
print("math.cos(",x,"): ",math.cos(x));
print("math.sin(",x,"): ",math.sin(x));
print("math.tan(",x,"): ",math.tan(x));
print("math.acos(",x,"): ",math.acos(x));
print("math.asin(",x,"): ",math.asin(x));
print("math.atan(",x,"): ",math.atan(x));
y = 2
print("math.atan2(",y,",",x,"): ",math.atan2(y,x))
print("math.hypot(",x,",",y,"): ",math.hypot(x,y))

#7,create a calculator only on a code level by using if condition (BAsic arithmetic)
num_one = int(input("Enter 1st number: "))
op = input("Enter operator: ")
num_two = int(input("Enter the 2nd number: "))
if op == "+":
    print(num_one + num_two)
elif op == "-":
    print(num_one - num_two)
elif op == "*" or op == "x":
    print(num_one * num_two)
elif op == "/":
    print(num_one / num_two)