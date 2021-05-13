'''
*
**
***
****
*****

'''

for i in range(0, 5):
    for j in range(i + 1):
        print('*', end=" ")
    print()
print('----------')

for i in range(5):
        print('* ' * (i + 1))
        
print('----------')

'''
    *
   **
  ***
 ****
*****
'''

for i in range(0, 5):
    print('  ' * (5 - i) + ' *' * (i+1))

print('----------')

'''
*****
****
***
**
*
'''

for i in range(6, 0, -1):
    print('* ' * (i - 1))
print('----------')

'''
*****
 ****
  ***
   **
    *
'''

for i in range(5):
    print('  ' * (i) + '* ' * (5 - i))
    # print('  ' * i, end='')
    # print('* ' * (5 - i))
print('----------')

'''
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
'''

for i in range(5):
    print('  ' * (4 - i) + '* ' * (2 * i + 1))
    # print('  ' * (5 - i), end='')
    # print('* ' * (i * 2 + 1))

