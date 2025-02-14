# Lesson 4
import math
print ("section one")
sec1 = len(input())
print ("section two")
sec2 = len(input())
print ("section three")
sec3 = len(input())
total = sec1 + sec2 + sec3
cans = 12 * (math.ceil(total / 12))
remain = cans % total 
cost = 14.95 * math.ceil(total / 12)
print("you will need\n",cans, " cans \n",remain," remainder\n$",cost," cost")