# Lesson 33
import math
n = int(input("how many values: "))
values = []
for i in range(n):
    values.append(int(input("enter a value: ")))
mean = sum(values) / len(values)
length = len(values)
values.sort()
if length % 2 != 0:
    median = values[length // 2]
else: 
    median = (values[(length // 2)]+ values[(length // 2) - 1]) / 2
print(f"median is {median} mean is {mean}")