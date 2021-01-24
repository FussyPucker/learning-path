#list
'''
zeros = [0] * 5
letters = ['a', 'b', 'c']
combined = zeros + letters
numbers = list(range(20))
chars = list('hello world')
print(combined)
print(numbers)
print(chars)
print(len(chars)) # length of the list
'''

#Accessing items
'''
letters = ['a', 'b', 'c', 'd']
print(letters)
letters[0] = 'A'
print(letters[0:3])

numbers = list(range(20))
print(numbers[::2]) # print list中的数字或字符等，每位之间相隔2

'''

#list unpacking
'''
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
#first, second, *other = numbers
first, *other, last = numbers
print(first, last)
print(other)
'''


#looping over lists
'''
letters = ['a', 'b', 'c']
items = [0, 'a']
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)
    #print(letter[0], letter[1]) 0 will get indexex, 1 will give the item at a given index
'''

#Adding or removing items
'''
letters = ['a', 'b', 'c']
#add
letters.append('d')
letters.insert(0, '-')
print(letters)
#remove
letters.pop(0) # pop() method will remove the item at the end of our list pop(0) will remove the item at the first of our lis
print(letters)
letters.remove('b')
print(letters)
del letters[0:3]
print(letters)
letters.clear()
print(letters)
'''


#Finding items
'''
letters = ['a', 'b', 'c']
print(letters.count('d')) # 计算list 中 ‘d’的数量
if 'd' in letters:
    print(letters.index('d'))
'''

#Sorting list
'''
numbers = [3, 51, 2, 8, 6]
numbers.sort()#this method will automatically sort these items in ascending order.
#numbers.sort() will also change the order of the items in the original list
#numbers.sort(reverse=True) this will make the items in our list to be sorted in descending order
print(sorted(numbers)) # will sorted the original list
#print(sorted(numbers, reverse=True))
print(numbers)

items = [
    ('product1', 10)
    ('product2', 20)
    ('product3', 30)
    ]
def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
'''

#Lambda Functions this can replace the def sort_item()
'''
items = [
    ('product1', 10)
    ('product2', 20)
    ('product3', 30)
    ]
items.sort(key=lambda item: item[1])
print(items)
'''

#Map function
'''
items = [
    ('product1', 10),
    ('product2', 2),
    ('product3', 30),
    ]
# x = map(lambda item: item[1], items)
#for item in x:
#    print(item)

price = list(map(lambda item: item[1]))
# map function taks a lambda function, and applies it to every item of this iterable
print(prices)    
'''


#filter function
'''
items = [
    ('product1', 10),
    ('product2', 2),
    ('product3', 30),
    ]
filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

'''
#list comprehensions
'''
items = [
    ('product1', 10),
    ('product2', 2),
    ('product3', 30),
    ]
prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]

print(prices)
print(filtered)

'''

#Zip function
'''
list1 = [1, 2, 3]
list2 = [10, 20, 30]
print(list(zip('abc', list1, list2)))
'''

#Stack
'''
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print('redirect', browsing_session[-1])
'''

#Queues first in first out
'''
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print('empty')
'''

#tuples 数组 tuple object does not support item assignment
'''
point = 1, 2
point(type(point))
'''

#Swapping variables
x = 10
y = 11
x, y = y, x
#x, y = (11, 10) the same as above


#Arrays
'''
from array import array

numbers = array('i', [1, 2, 3])
numbers[0]
'''


#Sets
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

print(first | second) #get union of two sets
print(first & second) #get intersection of two sets
print(first - second) #get differecee
print(first ^ second) #get semantic difference
# we have in a set are not in sequence so we can not access them. using an index.
#in other words, if we tried to print, first of 0, it will get a run time error
# set object does not support indexing.






















