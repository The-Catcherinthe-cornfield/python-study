#练习9 删除元素:      for遍历遇上列表时要注意for默认从0下标一直往后选取而删除元素时列表的下标会变化
nums = [2, 4, 6, 8, 10]
result = []
for x in nums:
    if x % 2 != 0:
        result.append(x)   #改用存而不是if判定删除或者倒着删除

nums = result
print(nums)

nums = [2, 4, 6, 8, 10]

for i in range(len(nums) - 1, -1, -1):    #len是长度陛下标数多1所以减1就是从最后一个数开始
    if nums[i] % 2 == 0:
        del nums[i]

print(nums)
