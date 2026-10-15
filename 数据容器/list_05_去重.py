#练习5:      去重复:创造一个空列表*******  not in 语句
nums = [3, 1, 3, 5, 1, 2, 3]
result = []
for num in nums:
    if num not in result:
        result.append(num)
print(result)
