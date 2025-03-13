# Lesson 46
longChain = {}
def col(num):
    count = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            count += 1
        else:
            num = 3 * num + 1
            count += 1
    return count
for num in range(1, 1000000):
    longChain[col(num)] = num
print(f"the maximum chain is {max(longChain)} with a value of {longChain[max(longChain)]}")
