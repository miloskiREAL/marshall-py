# Lesson 41
points = { 
    'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}
def score(word):
    score = 0
    for char in word.upper():
        if char.isalpha():
            score += points[char]
    if len(word) == 7:
        score += 50
    return score
num = int(input("how many words do you want to enter: "))
words = []
for n in range(num):
    words.append(input("enter a word: "))
maxScore = 0
maxWord = ""
for word in words:
    curScore = score(word)
    if maxScore < curScore:
        maxScore = curScore
        maxWord = word
print(f"the maximum score is {maxScore} belonging to the word {maxWord}")
    



    