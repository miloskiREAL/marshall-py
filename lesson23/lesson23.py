# Lesson 23
num = 0
sumN = 0
counter = 0
while True:
    num = input("enter a number or x to exit\n")
    if num == 'x':
        break
    else:
        sumN += int(num)
        counter += 1
print(f"average is {sumN/counter}")
