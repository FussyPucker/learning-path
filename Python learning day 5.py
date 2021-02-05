
#Dictionary comprehensions
'''
values = []
for x in range(5):
    values.append(x * 2)

values = [x * 2 for x in range(5)]
print(values)

values = [x: x * 2 for x in range(5)]
'''


#Generator Expressions
'''
generator object is iterable
'''

'''
from sys import getsizeof

values = (x * 2 for x in range(100000))
print('gen:', getsizeof(values))
values = [x * 2 for x in range(100000)]
print('list:', getsizeof(values))
'''


#unpacking operator
'''
numbers = [1, 2, 3]
print(numbers)
print(*numbers)

values = list(range(5))
values = [*range(5), *'hello']
print(values)



first = {'x': 1}
second = {'x': 10, 'y': 2}
combined = {**first, **second, 'z': 1}
print(combined)
'''

#Exercise
'''
write a program to find the most repeateeed character in this text

'''

'''
from pprint import pprint
sentence = 'This is a common interview question'
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

pprint(char_frequency, width=1)
print(sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True))
char_frequency_sorted = sorted(char_frequency.items(), key=lambda kv: kv[1], reverse=True)
print(char_frequency_sorted[0])
'''


#Exceptions
numbers = [1, 2]
print(numbers[3])









































