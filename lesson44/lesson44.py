# Lesson 44
word = str(input("enter word: ")).lower()
keys = sorted(list(set(word)))
freq = {}
for n in keys:
    count = 0
    if n.isalpha():
        for i in sorted(list(word)):
            if i == n:
                count += 1
        freq.update({n : count})
print(freq)