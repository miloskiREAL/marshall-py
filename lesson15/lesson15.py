# Lesson 15
conditionVar = True
password = "hello"
while conditionVar:
    userIn = input("guess the password ")
    
    if userIn == password:
        print("CORRECT")
        conditionVar = False
    else:
        print("INCORRECT")

print("\n")

userIn = input("search for fruits: ")

fruits = ["apple", "banana", "orange", "pineapple"]

found = False

for fruit in fruits:
    if fruit == userIn:
        print(f"{userIn} was found!")
        found = True

if not found:
    print(f"{userIn} was not found")