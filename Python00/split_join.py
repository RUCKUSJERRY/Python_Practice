import re

# split
str01 = 'Hello, world!\nHello, python!'
print(str01)

arr01 = str01.split(' ')

print(arr01)

arr02 = str01.split('\n')

print(arr02)

arr03 = str01.split(' ', 1)

print(arr03)

arr04 = re.split('[\s]|[,]', str01)
print(arr04)

#join
arr05 = ['1', '2', '3', '4']
print(arr05)
print('+'.join(arr05))
print(eval('+'.join(arr05)))
