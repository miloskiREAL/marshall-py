# Lesson 16
for n in range(1,51):
    if n % 3 == 0 and n % 5 == 0 :
        print("fizzbuzz")
    elif n % 5 == 0 :
        print("buzz")
    elif n % 3 == 0 :
        print("fizz")
    else :
        print(n)