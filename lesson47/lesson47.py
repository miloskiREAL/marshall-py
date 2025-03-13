# Lesson 47
def recSum(num):
    if num <= 0:
        return 0
    nSum = num + recSum(num - 1)
    return nSum
num2 = int(input("enter a number: "))
print(recSum(num2))