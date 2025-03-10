# Lesson 40
num = int(input("enter a number: "))
def factors():
    factorList = []
    for n in range(1, i + 1):
        if i % n == 0:
            factorList.append(n)
    return factorList
def isPrime():
    return len(factors()) == 2
primeFact = []
for i in range(1, num + 1):
    if num % i == 0 and isPrime():
        primeFact.append(i)
print(primeFact)