# Lesson 25
lPrime = 0
num = int(input("enter num: "))
n = 2
n2 = 1
primeCheck = 0
while n <= num:
    if num % n == 0:
        while n2 <= n:
            if n % n2 == 0:
                primeCheck += 1        
            if primeCheck > 2:
                break
            n2 += 1    
        if primeCheck <= 2:
            lPrime = max(lPrime, n)
    n2 = 1
    primeCheck = 0
    n += 1
print(lPrime)