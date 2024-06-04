def fizz():
    print('fizz')

def buzz(): 
    print("buzz")

def fizzbuzz(): #주송
    # 15의 배수에서 fizz 를 출력하는 함수를 작성해주세요.
    print("fizzbuzz")
    pass

def play():
    for i in range(1,16):
        if i % 3 == 0 and i % 5 != 0:
            fizz()
        elif i % 5 == 0 and i % 3 != 0 :
            buzz()
        elif i % 3 == 0 and i % 5 == 0:
            fizzbuzz()
        else:
            print(i)
    return

play()