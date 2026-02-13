"""#read input number from user
num = input()
print(type(num)) # Checking the type of number
print(num)"""


"""#implicit Type conversion
num1 = int(input())
val = float(input())
print(type(num1) , type(val)) # Checking the type of number
result = (num1 + val)
print(result)"""


"""num1 = (input()# read string type number
print(type(num1)) # Checking the type of number
res = num1 + 10 # TypeError:can only concatenate str (not "int") to str
print(res)"""

"""# To overcome the above problem by using Explicit Type Conversion

num1 = input()# read string type number
print(type(num1)) # Checking the type of number
res = int(num1) + 10 # TypeError:can only concatenate str (not "int") to str
print(res)"""


"""# Converting integer to float , string and boolean
num = 12
print(float(num))
print(str(num))
print(bool(num))"""
