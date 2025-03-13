# Lesson 45
# Words to Length
def wordLength(words):
    w2l = {}
    for n in words:
        w2l[n] = len(n)
    return w2l
wordN = int(input("how many words: "))
words = []
for u in range(wordN):
    words.append(input("enter a word: "))
print(wordLength(words))
# Fibonacci Sequence
fibDict = {0:0, 1:1} 
term = int(input("enter which term you want to go to: "))
for u in range(2, term + 1):
    fibDict[u] = fibDict[u - 1] + fibDict[u - 2]
print(fibDict)
