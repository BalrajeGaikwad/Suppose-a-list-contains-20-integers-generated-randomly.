"""
Suppose a list has 20 numbers. Write a program that removes all duplicates from this list.

"""

import random

numbers=[random.randint(1,20) for _ in range(20)]
print(numbers)

unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)

print("list after removing duplicates :",unique)