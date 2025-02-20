# Lesson 10
number = input("enter the number\n")
if int(number[0]) == 8 or int(number[0]) == 9 :
    if int(number[1]) == int(number[2]) :
        if int(number[0]) == 8 or int(number[0]) == 9 :
            print("scammer")
else :
    print("not scammer")