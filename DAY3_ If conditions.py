#Check whether a number is even or odd
"""n = int(input("Enter a number:"))
if n % 2 == 0:
    print("even")
else:
    print("odd")"""

#Check a number 3 and 5 divisible are not
"""n = int(input("Enter a number:"))
if(n%5 == 0) and (n%3 == 0):
    print("Divisible")
else:
    print("Not divisible")"""

"""#print 10 numbers
for i in range(1,11):
    print(i)"""

#Sum of numbers
"""total = 0
for i in range(1 , 6):
    total = total + i
print(total)"""

"""#print a number is even 
n = int(input("Enter a number: "))
for i in range(1, n+1):
    if(i % 2 == 0):
        print(i)"""
#Find whether the number is positive even,negative even,positive odd,negative odd
"""n = int(input())
if (n % 2 == 0 and n >= 0):
    print("positive Even")
elif (n % 2 == 0 and n < 0):
    print("negative Even")
elif (n % 2 != 0 and n > 0):
    print("positive Odd")
else:
    print("Negative odd")"""
#using Nested if
#Find whether the number is positive even,negative even,positive odd,negative odd
"""if n >= 0:
    if n%2 == 0:
        print("positive even")
    else:
        print("positive odd")
else:
    if n%2 == 0:
        print("negative even")
    else:
        print('negative odd")"""
# Find Bigest number among three numbers
"""n,m,k = map(int,input().split())
if(n >= m and n >= k):
    print("Greatest number is",n)
elif(m >= k and m >= n):
    print("Greatest number is",m)
elif(n == m == k):
    print("All are equal")
else:
    print("Greatest number is",k)"""

#Nested if practice questions
#Voting + citizenship
"""age = int(input())
citizen = input("Are you citizen(yes/No)")
if age >= 18:
    if citizen == "yes":
        print("You can vote")
else:
    print("You cannot vote")"""

#Password + OTP
"""password = input()
if password == "python123":
    otp = input("Enter OTP:")
    if otp == "4567":
        print("login sucessful")
    else:
        print("wrong OTP")
else:
    print("wrong password")"""

#Student marks >= 35 and attendance >= 75 then pass Else fail       
"""marks = int(input())
attendance = int(input())
if marks >= 35:
    if attendance >= 75:
        print("Pass")
    else:
        print("Fail")
else:
    print("Fail")"""
#Greatest among 4 numbers using nested if
"""a,b,c,d = map(int,input().split())
if(a>b and a>c):
    if(a>d):
        print("a is greater")
elif(b>c and b>d):
    print("b is greater")
elif(c>d):
    print("c is greater")
else:
    print("d is greater")"""

#Print a even or odd
"""n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")"""

#print a number Negative/positive/Zero
"""n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")"""

#Voting Eligibility
"""n = int(input("Enter a number: "))
if n >= 18:
    print("Eligible")
else:
    print(" Not eligible")"""

#Greatest 3 numbers
"""a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(" a is greater")
elif b > c:
    print("b is greater")
else:
    print("c is greater")"""

"""n = input("Enter a password: ")
if n == "python123":
    print("Correct password")
else:
    print("Incorrect password")"""

#pass / Fail
"""marks = int(input())
if marks >= 35:
    print("pass")
else:
    print("fail")"""
#
"""num = int(input("Enter a number: "))
if num % 5 == 0 and num % 3 == 0:
    print("Divisible by both 5 and 3")
elif num % 5 == 0:
    print("Divisible by 5")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible")"""
#
"""married = input()
age = input()
gender = input()
if married == "yes":
    print("insured")
elif married == "No" and gender == "male" and age >= 30:
    print("Insured")
elif married == "No" and gender == "female" and age >= 25:
    print("Insured")
else:
    print("Not Insured")"""

#Leap year check
"""year = int(input())
if year % 400 == 0: #divisible by 400
    print("leap year")
elif year % 4 == 0 and year % 100 != 0: #divisible by 4 but NOT by 100
    print("Leap year")
else:
    print("Not leap year")"""



