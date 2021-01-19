'''
price = 10 # 整数
rating = 4.9 #浮点数
name = 'mosh' #string
is_published = True #we use an underscore to spearate multiple words and variable name.
#True or False is boolean values.
# python is a case sensitive language, which means it is sensitive to lower case and upper case letters.
# when defining variables we should always use lowercase letters, but false and true
# are special keywords in the language, so if we spell it with a lowercase f, python
#does not understand it.
print(price)
'''


'''
#Excercise:
We check in a patient named john smith. He is 20 years old
and is a new patient

#Solution1:
full_name = 'John smith'
age = 20
is_new = True
'''

'''
#Receiving input
name = input('What is your name? ')
print('Hi ' + name)

#Receiving input practice
mosh likes blue
name = input('What is your name? ')
color = input('What is your favourite color? ')
print(name + ' likes ' + color)
'''

'''
#type conversion int() float()
birth_year = input('Brith year: ')
age = 2021 - int(brith_year)
print(age)

weight_lbs = input('what is your weight? ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
'''
'''
#String
name = 'Jennifer'
print(name[0:3])
'''

'''
#formatted strings
first = 'John'
last = 'Smith'
msg = f'{first} [{last}] is a coder'
print(msg)
msg = f'{first} [{last}] is a coder'
'''


#Srting method
course = 'Python for beginners'
print(len(course))
print(course)
print(course.upper())
print(course.find('P'))
print(course.lower())
# if we dont find any character in the string
#it will return -1 instead of the real index
print(course.replace('beginners', 'Absolute Beginners'))
print('Python' in course)
#对错判断, in operator is a booleean value. Do you have this or not?

#Arithmetic operations













































