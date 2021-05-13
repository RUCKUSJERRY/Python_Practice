import random

def lotto():
    
    res = set()
    
    # len() : length -> 객체의 길이를 리턴
    while len(res) < 6:
        a = random.randint(1, 45)   
        
        res.add(a)
    lst = sorted(res)

    print(lst)
    

if __name__ == '__main__':
    lotto()
    