#7 列表去重 -------方法二保留顺序------
nums = [3, 1, 3, 2, 1, 5]
result = []
for num in nums:
    if num not in result:
        result.append(num)
print(result)
