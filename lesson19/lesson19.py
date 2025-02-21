# Lesson 19
num = int(input("enter a number\n"))
fCount = 0
n = 1
while n <= num:
    if fCount > 2:
        break
    elif num % n == 0:
        fCount += 1
    n += 1
if fCount == 2:
    print("prime")
else :
    print("not prime")