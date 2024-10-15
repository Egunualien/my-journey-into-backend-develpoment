'''operators'''
a = 5
b = 6
d = a + b
print(f'the addition of a and b is {d}')
f = a - b
print(f'the subtraction of a and b is {f}')

   #comparison operators
#equal
y = a == b
print(f'a and b are equal ...{y}')
g = a > b
print(f'is a greater than b... {g}')
#notequal
u = a != b
print(f'a is lesser than b..{u}')
o = a < b
print(f'a is greater than equal to b..{o}')
i = a >= b
print(f'a isgreater than egual to b..{i}')
j = a <= b
print(f'a is lesser than equal to b..{j}')


#conditional statement
'''if condition:
       code

'''
x = 7
if x < 6 :
    print('x is greater than 6')
else :
    print('na lie')

x = 10
if x < 10 :
    print('insufficient fund')
else :
    print('proceed to withdraw')

deposit = int(input('boss deposit your money '))
get_cash = int (input('get cash '))
if deposit >= get_cash:
    print('take your money')
else:
    print('guy you are broke')
balance = deposit - get_cash
print(f'your balance is now {balance}')


user_name = input('what is your name')
password1 = int(input('enter your password'))
password2 = int(input('confirm your password'))
if password1 == password2:
    print('log in successful')
else:
    print('input the same password')


    user_biodata = {}

    user_biodata['username'] = input('input your name ')
    user_biodata['state'] = input('input your state') 
    user_biodata['password1'] = int(input('enterany password'))
    user_biodata['password2'] = int(input('enter the same password'))
    print(user_biodata)
    if user_biodata['password1'] == user_biodata['password2']:
        print('your biodata has been collected')
    else:
        print('correct your password')

    #write a python code to check a student grade based on their score
    #write a python code to check if a number is positive,negative or zero
    #write a python programme to check if a year is a leap year
