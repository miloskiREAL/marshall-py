# Lesson 8
x = range(6)
n = 1

for n in x :
    print("enter results")
    results = list(input())
    wins = results.count("W")
    if wins >= 5:
        print(f"player {n + 1} is in group one")
    elif wins >= 3:
        print(f"player {n + 1} is in group two")
    elif wins >= 1:
        print(f"player {n + 1} is in group three")
    else :
        print(f"player {n + 1} is dq")
    n += 1