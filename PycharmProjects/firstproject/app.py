import re
#
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

# search
result = re.search(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")

# find all
print( re.findall(pattern, test_string))

string1 = "Hi I am hari,hello hari"
pattern = r'hari'
string2 = re.sub(pattern,"haran",string1)
print(string2)


pattern = 'ha.i'
if re.match(pattern,"hari" ):
  print("Search successful.")
else:
  print("Search unsuccessful.")

pattern = '^ha.i$'
if re.match(pattern,"hari" ):
  print("Search successful.")
else:
  print("Search unsuccessful.")

# character class
pattern = "[A-Z[A-Z]][0-10]"

if re.search(pattern,"AG0"):
  print("successful")

# star metacharcter and groups
pattern = "hari(haran)*"

if re.search(pattern,"hariharan"):
  print("found")

