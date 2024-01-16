#list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x * 2 for x in numbers]
print(squared)


#sorting the list
new = [12,15,5,7,33,23]
new.sort(reverse=True)
print(new)
new.sort()
print(new)



#filtering the list
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon"]
filtered_words = [word for word in words if 'a' in word]
print(filtered_words)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 != 0]
print(even_numbers)


