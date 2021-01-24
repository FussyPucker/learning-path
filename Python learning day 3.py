#for loop
'''
for number in range(3):
    print('Attempt', number + 1, (number + 1)* '.')
'''

'''
successful = False
for number in range(3):
    print('Attempt')
    if successful:
        print('Successful')
        break
else:
    print('Attempt 3 times and failed')
        
'''


#Nesteed Loops
'''
for x in range(5):
    for y in range(3):
        print(f'({x}, {y})')
'''
    

#While loops
'''
number = 100
while number > 0:
    print(number)
    number = number // 2
'''
'''
command = ''
while command != 'quit' and command != 'QUIT':
    command = input('>')
    print('echo', command)
'''
'''
while True:
    command = input('>')
    print('Echo', command)
    if command.lower() == 'quit':
        break
'''
'''
count = 0
for number in range(1, 20):
    if number % 2 == 0:
        print(number)
        count += 1
print(f'we have {count} even number')
'''


#defining function
'''
def greet(first_name, last_name):
    print(f'Hi there {first_name} {last_name}')
    print('Welcome aboard')


greet('Ren', 'Guan')
'''

#Types of Functions
'''
def greet(name):
    print(f'hi {name}')

def get_greeting(name):
    return f'hi {name}'

message = get_greeting('Mosh')
'''

#Keyword arguments
'''
def increment(number, by):
    return number + by

print(increment(2, by=1))
'''

#Default arguments
'''
def increment(number, by=1):
    return number + by

all the required arguments should always in front of the optional parameters
'''

#Xargs
'''
def multiply(*numbers):
    
    total = 1
    for number in numbers:
        total *= number

    return total


print(multiply(2, 3, 4, 5))
'''

#Xxargs
'''
def save_user(**user):
    print(user)

save_user(id=1, namee='John', age=22)    
'''

#Scope
'''
message = 'a'

def greet(name):
    global message
    message = 'b'

greet('Mosh')
print(message)
this is a very bad practice
'''

#Fizz Buzz
def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5) == 0:
        return 'FizzBuzz'
    if input % 3 == 0:
        result = 'Fizz'
    if input % 5 == 0:
        result = 'Buzz'
    
    return input


print(fizz_buzz(15))
















































































    

        
  
