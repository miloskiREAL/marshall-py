# Lesson 38
def isPal(prod):
    check = str(prod)
    if check == check[::-1]:
        return True
    else:
        return False
high = 0
factors = []
for n in range(100, 1000):
    for n2 in range(100, 1000):
        prod = n * n2
        if prod > high and isPal(prod):
            factors.clear()
            factors.append(n)
            factors.append(n2)
            high = prod
print(f"the highest possible palindromic number is {high} with the factors {factors}")

