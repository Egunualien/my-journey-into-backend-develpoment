my_name = 'gozie'
age = 59
hobbies = "i love games"
sex = 'male'
status = 'married'

num1 = 10
num2 = 4
print(num1 + num2)
sum = num1 + num2
minus = num1 - num2
mul = num1 * num2
div = num1 / num2
modulus = num1 % num2
round = num1 // num2
print(sum)
print(minus)
print(mul)
print(modulus)
print(round)

float_num = 20.9 #number with decimal point
print(float_num)

string_value = 'my name is gozie'
print(string_value)
s = "and favour"
print(s + string_value)
print( "my name is gozie" + s)
#methods in strings
print(string_value)
print(string_value.count('a'))#counts the number of a in the string
print(string_value.replace("j", "m"))#replaces the letter j with m
print(string_value.upper())
print(string_value.lower())
print(string_value.islower())
print(string_value.__len__())#length of string


#inputs
#name = input("what is your name?")
#print("your name is" + name)

#simple calculator to get addition and substraction
number1 = int(input("input any number"))
number2 = int(input("input another number"))
add = number1 + number2
sub = number2 - number1
print(f"the sum of your numbers are  + {add}")
print(f"the subtraction of your number is {sub} ")

#import function for number operation
from math import * #import all math function
