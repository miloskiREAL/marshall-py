# Lesson 11
coords = input("enter coords\n")
coords = coords.split()
def cast(value):
   return int(value)
coords = list(map(cast, coords))
if coords[0] == 0 or coords [1] == 0:
    print("not in a quadrant")
elif coords[0] > 0:
    if coords[1] > 0:
        print("1")
    else :
        print("4") 
else :
    if coords[1] > 0:
        print("2")
    else:
        print("3")
