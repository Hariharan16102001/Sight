keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
myDict = { k:v for (k,v) in zip(keys, values)}
print (myDict)

#using dictionary comprehension dictionary
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)


#sorting a dictionary

new = {'z': 26, 'd': 4, 'm': 13, 'w': 23}
new2 = dict(sorted(new.items()))
print(new2)


my = {'b': 2, 'a': 1, 'c': 3}
var = dict(sorted(my.items(), key=lambda item: item[1]))
print(var)

one = {'a': 1, 'b': 2}
two = {'b': 3, 'c': 4}
one.update(two)
print(one)

