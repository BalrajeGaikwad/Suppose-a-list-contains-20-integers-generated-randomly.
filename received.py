"""
 Suppose a list contains 20 integers generated randomly. Receive a number from the keyboard and report position of all occurrences of this number in the list.

"""

import random

numbers=[random.randint(1,10) for _ in range(20)]
#numbers=random.randint(1,20)
print("list : ",numbers)

num=int(input("Enter the number want too search :"))

position=[]
for i in range(len(numbers)):
    if numbers[i]==num:
        position.append(i)


if position:
    print((f"{num} is found at the given position {position}"))
else:
    print(f"{num } not found in list")
