# Lesson 13
month = int(input("enter the month\n"))
date = int(input("enter the day\n"))
if month > 2 :
    print("after")
elif month < 2 :
    print("before")    
else :
    if date < 18 :
        print("before")  
    elif date > 18 :
        print("after")
    else :
        print("special")