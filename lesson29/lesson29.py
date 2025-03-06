# Lesson 29
word = input("enter a word: ")
vowels = list("aeiou")
conson = 0
for n in word:
    if n.isalpha and n.lower() not in vowels:
        conson += 1
print(conson)