#print even or odd with diff conditions using nested if
"""n1,n2,n3 = map(int,input().split())
if(n1%2 == 0):
    print("n1 is even")
else:
    print("n1 is odd")
if(n2%2 == 0):
    print("n2 is even")
else:
    print("n2 is odd")
if(n3%2 == 0):
    print("n3 is even")
else:
    print("n3 is odd")"""
#FOR LOOPS
#print even or odd with diff conditions using for loop
"""lst = [1,2,3,4,5]
for ind in range(0,5,1):
    if lst[ind]%2 == 0 :
        print(lst[ind],"is even number")
    else:
        print(lst[ind],"is odd number")"""

#print even numbers between 20 to 40
"""for i in range(20,41,2):
    print(i)"""

#Now 2nd approch to print even numbers netween 20 to 40
"""for i in range(20,41,1):
    if(i%2 == 0):
        print(i,"is even")
    else:
        print(i,"is odd")"""
#print 1 to 100 numbers
"""for i in range(1,100):
    print(i, end = " ")"""
#find the sum of n natural numbers
"""n = int(input())
total = 0
for i in range(1,n+1):
    total = total + i
print(total)"""
#WHILE LOOPS
#print 1 to 100 numbers
"""n = 1
while n < 101:
    print(n ,end=" ")
    n = n+1"""
#print 100 to 1 numbers
"""n = 100
while n > 1:
    print(n,end=" ")
    n = n-1"""
#print even numbers between 10-40
"""i = 10
for i in range(10,41):
    while i%2 == 0:
        print(i,end=" ")
        i = i+1"""
#print odd numbers between 1-50
"""i = 1
for i in range(1,51):
    while i%2 != 0:
        print(i,end=" ")
        i = i+1"""
#find which even or odd numbers from list of numbers
"""i=[1,2,3,4,5]
ind = 0
while ind<len(i):
    if i[ind]%2 == 0:
        print(i[ind],"is even number")
    else:
        print(i[ind],"is odd number")
    ind = ind+1"""
#Find sum of even numbers upto 'n'
"""n = 10
total = 0
i = 0
while i<n:
    if i%2 == 0:
        total = total+i
    i = i+1
print(total)"""
#Find sum of even numbers between 10-21 using for loop
"""for i in range(10,22,2):
    if i%2 == 0:
        print(i)"""
#Find sum of even numbers between 10-21 using while loop
#this is for test case 10-21 here the '10' is even number
"""n = int(input())
m = int(input())
total = 0
while n < m:
    if n%2 == 0:
        total = total+n
    n+=1
print(total)"""
#this is for test case 11-21 here the '11' is odd number
"""if n%2 != 0:
    n = n+1
while n < m:
    if n%2 == 0:
        total = total+n
    n+=2
print(total)"""
#Sum of digits in a number(here we dont know the number of iterations so we used while loop
"""n = 156
sum = 0
while n > 0:
    rem = n%10
    n = n//10
    sum = sum+rem
print(sum)"""
#Find the length of number '4675'
"""n = 4675
count = 0
while n>0:
    n = n//10
    count = count+1
print(count)"""
#Sum of digits in a number '156'
"""n = 156
total = 0
while n>0:
    rem = n%10
    n = n//10
    total = total+rem
print(total)"""
#Reverse a number '126'
"""n = 126
rev = 0
while n>0:
    rem = n%10
    rev = rev*10+rem
    n = n//10
print(rev)"""
# check whether a number is palindrome or not
"""n = int(input())
temp = n
rev = 0
while n>0:
    rem = n%10
    rev = rev*10+rem
    n = n//10
if temp == rev:
    print("palindrome")
else:
    print("Not a palindrome")"""
#check perfect number
"""n = 28
total = 0
i = 1
while(i<n//2+1):
    if(n % i == 0):
        total = total + i
    i = i+1
if(total == n):
    print("perfect number")
else:
    print("Not perfect number")"""
