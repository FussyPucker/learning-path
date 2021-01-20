#Arithmetic operations
'''
print(10 // 3) #get integer
print(10 / 3) # might get a float
print(10 % 3) # get reminder of divison
print(10 ** 3) # get 10's power of 3
'''

#Math function
'''
print(abs(-2.9))
'''

#if statements
'''
is_hot = False
is_cold = False

if is_hot:
    print('it is a hot day')
    print('drink plenty of water')
elif is_cold:
    print('it is a cold day')
    print('wear warm clothes')
else:
    print('it is a lovely day')

print('enjoy your day')

price = 1000000
is_goodcredit = True
is_badcredit = False

if is_goodcredit:
    down_payment = 0.1 * price
elif is_badcredit:
    down_payment = 0.2 * price
print(f'down payment: {down_payment}' )
'''

#Logical operators
'''
has_high_income = True
has_good_credit = False
has_criminal_record = False

if has_high_income and has_good_credit:
    print('Eligible for loan')

if has_high_income or has_good_credit:
    print('Eligiblee for loan')

if has_high_income and not has_criminal_record:
    print('good')
'''

#Comparison Operatiors
'''
name = input('what is your name?: ')
if len(name) < 3:
    print('name must be at least 3 characters!')
elif len(name) > 50:
    print('name can be a maximum of 50 characters!')
else:
    print('name looks good!')
'''


#Weight Converter Program
'''
weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight * 0.45
    print(f'you are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'you are {converted} pounds')
'''

#While loop
'''
i = int(input('i= ? '))
while i <= 5:
    print('*' * i)
    i = i + 1
print('Done')
'''

#Guessing game
'''
collect_answer = 9
guess_count = 0
guess_limit = 3
while guess_count< guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == collect_answer:
        print('You win!')
        break
else:
    print('you have no chance!')
'''

#For loops
'''
prices = [10, 20, 30]
total = 0
for price in prices: # in range(5, 10, 2)从5数到9, 每个跳2数
    total += price
print(f'total: {total}')
'''
'''
#Nested loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')
'''        

    

    

    

    











































    

