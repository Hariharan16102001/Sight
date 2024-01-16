a = 30 #global variable
def new():
    a=20 #local variable
    print(a)
new()
print(a)

def outer():
    x = 33
    def inner():
        print(x)
    inner()
outer()


#modifying global variable
y=25
def modify():
    global y
    y = 60
    print(y)
modify()
