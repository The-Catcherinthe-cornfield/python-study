import math
from random import randint
import datetime as dt


r = float(input("请输入半径:"))
print(f"面积等于:{math.pi*r*r:.2f}")
print(f"周长等于:{math.pi*r*2:.2f}")

print("-"*30)

nums = []
for _ in range(5):
    nums.append(randint(1,100))
nums.sort()
print(nums)

print("-"*30)

print(dt.date.today())