# Lesson 12
ang1 = int(input("enter an angle\n"))
ang2 = int(input("enter an angle\n"))
ang3 = int(input("enter an angle\n"))
if (ang1 + ang2 + ang3) == 180 :
    if ang1 == ang2 == ang3 :
        print("equilateral")
    elif ang1 == ang2 or ang2 == ang3 or ang1 == ang3:
        print("isoceles")
    else :
        print("scalene")
else:
    print("not a triangle")