# 문자
# single quotation 과 double quotation은 차이 없음

# single * 1
a = 'python\'s hello, world!'

print(a)

# single * 3
b = '''python's
hello, world!
            hello, python!!
'''
print(b)

# double * 1
c = "Hello, \"world!\""

print(c)

# double * 3
d = """
abc
def
"ghi"
"""
print(d)

# 혼합
e = 'abc"def"ghi\npython\'s string' #\n
print(e)

f = "abc'def'ghi\ttest" #\t
print(f)

g = r"C:\Workspaces\Workspace_Python\Python00" #r = raw sting (\를 문자로 인식)
print(g)

# 문자열 곱하기, 더하기
str01 = 'hello'
str02 = 'python!'
print(str01 + str02)
print(str01 * 3 + str02)
