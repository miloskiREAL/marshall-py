# Lesson 31
word1 = input("enter word: ")
word2 = input("enter word: ")
if len(word1) == len(word2):
    aList = sorted(word1)
    bList = sorted(word2)
    if aList == bList:
        print("yep")
    else:
        print("nope")
else:
    print("nope")