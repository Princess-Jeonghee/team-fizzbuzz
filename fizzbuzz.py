def fizz():
    print('fizz')

def buzz(): 
    print("buzz")


def fizzbuzz():
    print("fizzbuzz")
def play():
    for i in range(1,16):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz()
        elif i % 3 == 0:
            fizz()
        elif i % 5 == 0:
            buzz()

        else:
            print(i)
    return

play()