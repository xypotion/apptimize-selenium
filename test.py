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
    
##########
    
class Thing:
    def __init__(self, size = "big", color = "blue"):
        self.size = size
        self.color = color
        
    def describeSelf(self):
        print("i am " + self.size + " and " + self.color + ".")
        
myThing = Thing()
myThing.describeSelf()

otherThing = Thing("small", "red")
otherThing.describeSelf()