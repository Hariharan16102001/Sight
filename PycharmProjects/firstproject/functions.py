#function
def new_function():
    print("Hi this is hariharan")
new_function()

#return value
def num(x):
    return x+x
print(num(3))


#default arguments
def new(x,y=50):
    print("value of x : ",x)
    print("value of y : ",y)
new(10)

#keyword arguments and positional arguments
def new2(firstname,lastname):
    print(firstname,lastname)
new2("hari","haran")

#multiple return value
def num(x,y):
    result = x+y
    return result
print(num(3,5))