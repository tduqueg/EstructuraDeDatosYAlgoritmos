
d = {"Name" : "Kevin", "Age" : 34, "Gender" : "Male"}

print(d.items())

for key,value in d.items():
    print(value)
    print(key)

d.clear()
print(d.items())

