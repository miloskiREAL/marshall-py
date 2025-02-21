# Lesson 24
lName = ''
name = ''
while True:
    name = input("enter a name\n")
    if name == "x":
        break
    else:
        if len(name) > len(lName):
            lName = name
print(lName)