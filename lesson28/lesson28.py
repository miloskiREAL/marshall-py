# Lesson 28
text = input("enter a word: ").lower()
anagram = input("enter the anagram: ").lower()
if not text or not anagram:
    print("no text provided")
elif text[0] != anagram[-1]:
    print("not an anagram")
else:
    if text == anagram[::-1]:
        print("yep")
    else: 
        print("nope")