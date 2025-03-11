# Lesson 37
def compress():
    compressed = ""
    for n in sorted(list(set(word))):
        count = 0
        compressed += n
        for i in word:
            if n == i:
                count += 1
        compressed += str(count)
        
    if len(compressed) >= len(word):
        return word
    else:
        return compressed
word = str(input("enter a word: ")).lower()
print(compress())