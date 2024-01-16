age = (16,20,30,28,18,23,25,35) 
print(age)
print (age[3])
print(age[:4:-1])

#example for all the list methods :
#append
age.append(45)
print(age)

#extend
age.extend([10,20])
print(age)

#insert
age.insert(3,33)
print(age)

#remove
age.remove(16)
print(age)

#pop
age.pop(6)
print(age)

#index
newage = age.index(23)
print(newage)

#count
age2= age.count(20)
print(age2)

#sort
age.sort(reverse=True)
print(age)

#reverse
age.reverse()
print(age)