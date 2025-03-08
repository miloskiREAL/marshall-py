# Lesson 32
word1 = input("enter a word: ")
word2 = input("enter a word: ")
temp = set(word1 + word2)
final = []
for n in temp:
    if n in word1 and n in word2:
        final.append(n)
print(sorted(final))



