# 1번 문제
x = input('숫자 입력 : ')

a, b = 0, 1

while a < int(x):
    print(a, end=" ")
    a, b = b, a+b
print()

# 2번 문제  
def fibo1(x):
    a, b = 0, 1
    while a < int(x):
        print(a, end=" ")
        a, b = b, a+b
    print()
    
# 3번 문제
x = input('숫자 입력 : ')
res = []
a, b = 0, 1

while a < int(x):
    res.append(a)
    a, b = b, a+b
print(res)
print()

# 4번 문제
def fibo2(x):
    res = []
    a, b = 0, 1

    while a < int(x):
        res.append(a)
        a, b = b, a+b
    print(res)
    print()

# 5번 문제  
if __name__ == '__main__':
    x = input('level 입력 : ')
    fibo1(x)
    x = input('level 입력 : ')
    fibo2(x)