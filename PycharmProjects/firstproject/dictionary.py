capitals = { "india": "new delhi",
             "africa" : "new delhi",
            "england" : "london"
}
print(capitals)
print(capitals["india"])

#get method
print(capitals.get("india","none"))

#fromkeys(),12
week = ("mon","tue","wed")
print (dict.fromkeys(week))

#item()
print(capitals.items())

#keys()
print(capitals.keys())

#values()
print(capitals.values())

#pop()
(capitals.pop("india"))
print(capitals)

#popitem
capitals.popitem()
print(capitals)

#update()
capitals.update({"dubai":"abu dhabi"})
print(capitals)

#copy
x = capitals.copy()
print(x)

#clear
capitals.clear()
print(capitals)

