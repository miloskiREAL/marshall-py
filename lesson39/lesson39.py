# Lesson 39
def gcd(num, num2):
    for n in range(min(num, num2), 0, -1):
        if num % n == 0 and num2 % n == 0:
            return n
num = int(input(("enter a number: ")))
num2 = int(input(("enter a number: ")))
print(f"the gcd is {gcd(num, num2)}")