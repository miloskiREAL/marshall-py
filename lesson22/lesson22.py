# Lesson 22
num = int(input("enter a number: "))
n = 2
fibn2 = 0
fibn1 = 1
fibNth = 0
if num == 1:
    print("1")
elif num == 0:
    print("0")
else:
    while n <= num:
        fibNth = fibn1 + fibn2
        fibn2 = fibn1
        fibn1 = fibNth
        n += 1
    print(fibNth)