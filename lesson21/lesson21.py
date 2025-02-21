# Lesson 21
maxF = 0
nMax = 0
factors = 0
n = 1
n2 = 1
num = int(input("enter a number "))
while n <= num:
    while n2 <= n:
        if n % n2 == 0:
            factors += 1
        n2 += 1
    if maxF < factors:
        nMax = n
        maxF = factors
    n += 1
    n2 = 1
    factors = 0
print(nMax)