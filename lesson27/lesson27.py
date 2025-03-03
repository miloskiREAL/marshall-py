# Lesson 27
dirty = list(input("enter a phrase "))
clean = ""
for n in dirty: 
    if (n <= "z" and n >= "a") or (n <= "Z" and n >= "A") or n == " ":
        clean += n
print(clean)