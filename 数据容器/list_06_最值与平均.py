#练习6:
min1 = 100
max1 = 0
sum = 0
nums = [88, 92, 75, 60, 99]
for num in nums:
    sum += num
    if num > max1:
        max1 = num
    if num < min1:
        min1 = num
print(sum)
print(f"{sum/5:.1f}")
print(max1)
print(min1)
