# Lesson 20
n = 6
n2 = 1
check = 0
while n <= 10000:
    while n2 < n:
        if n % n2 == 0:
            check += n2
        n2 += 1
    if check == n:
        print(n)
    n += 1
    n2 = 1
    check = 0

            
