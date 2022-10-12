a = 5
print('The value of a is',a) #a space is added after "is" by default
print()
#original print statement-> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
print()
temp="\noutput formatting"
print(temp)
x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))
#The value of x is 5 and y is 10

"""
 Here, the curly braces {} are used as placeholders.
 We can specify the order in which they are printed by using numbers (tuple index).
"""
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))

print()
x = 12.3456789
print('The value of x is %3.2f' %x)
#The value of x is 12.35
print('The value of x is %3.4f' %x)
#The value of x is 12.3457