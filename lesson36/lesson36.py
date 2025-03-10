# Lesson 36
num = int(input("enter a number: "))
def factors():
    factorList = []
    for n in range(num):
        if num % (n + 1) == 0:
            factorList.append(n + 1)
    return factorList
def isPrime():
    return len(factors()) == 2
factorList = factors()
prime = isPrime()
print(f"the factors are {factorList} is this number prime? {prime}")



