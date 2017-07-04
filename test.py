print("hello world")

def compareAB(a, b):
    if b > a:
        print("b > a")
    else:
        print("a > b")

if 1: #no true constant? weird.
    print ("true")
    
a = 10
b = 20

compareAB(a, b)

a = a * b

compareAB(a, b)
    