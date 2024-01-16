new = {"hari",16,10.03,"haran",2001}
print(new)

#set()
x = [10,15,16,33,45]
y = tuple(x)
print(y)

#remove()
new.remove(16)
print(new)

#discard()
new.discard(2001)
print(new)

#pop()
print(new.pop())
print(new)


new2={2001,"hari",333,56.64,"fox"}
new3 = new.union(new2)
print(new3)

new4=new.intersection(new2)
print(new4)

new5 = new.difference(new2)
print(new5)

#clear
new.clear()
print(new)