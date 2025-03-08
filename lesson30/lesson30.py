# Lesson 30
n = int(input("enter a number: "))
output = ""
for i in range(n):
    if (i + 1) % 2 == 0:
        output += "0"
    else: 
        output += "1"
    print(output)
