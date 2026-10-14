#练习1:
# fruits = ["苹果", "香蕉", "橙子"]
# fruits.append("葡萄")
# print(fruits)
#
# fruits.insert(1,"西瓜")
# print(fruits)
#
# fruits[0]="梨"
# # fruits = ['梨', '西瓜', '香蕉', '橙子', '葡萄']
# print(fruits)
#
# fruits.pop(2)
# print(fruits)
#
# last = fruits.pop()
# print(last)
#
# del fruits[0]
# print(fruits)

#练习2:
# names = ["小明", "小红", "小刚"]
# for name in names:
#     print(name)
# for name in names[::-1]:
#     print(name)

#练习3:
# j = False
# j1 = False
# i = 0
# t = -1
# scores = [88, 92, 75, 92, 60, 92]
# print(f"列表的长度为:{len(scores)}")
# for score in scores:
#     if score==92:
#         i+=1
#     if score==75:
#         j = True
#         continue
#     if score==100:
#         j = True
#         continue
# for an in range(len(scores)):     #用len配合[]来找位置range别漏掉
#     if scores[a]==92:
#         t = a
#         break
# print(f"92出现的次数为:{i}")
# print(f"75是否存在:{j}")
# print(f"100是否存在:{j1}")
# print(t)

#练习4:
# nums = [5, 2, 9, 1, 7]
# # nums.sort()
# # print(nums)
# nums.reverse()
# print(nums)
# nums.reverse()
# print(nums)

# nums2 = [5, 2, 9, 1, 7]
# new = sorted(nums2)     #*******sorted是排序时顺便再把原本的数据存下来
# print(new)
# print(nums2)

#练习5:      去重复:创造一个空列表*******  not in 语句
# nums = [3, 1, 3, 5, 1, 2, 3]
# result = []
# for num in nums:
#     if num not in result:
#         result.append(num)
# print(result)

#练习6:
# min1 = 100
# max1 = 0
# sum = 0
# nums = [88, 92, 75, 60, 99]
# for num in nums:
#     sum += num
#     if num > max1:
#         max1 = num
#     if num < min1:
#         min1 = num
# print(sum)
# print(f"{sum/5:.1f}")
# print(max1)
# print(min1)

#练习7:列表嵌套
# nums = [12, 7, 8, 15, 20, 33]
# result = []
# for num in nums:
#     if num % 2 == 0:
#         result.append(num)
# print(result)
# scores = [
#     ["小明", 88, 92, 75],
#     ["小红", 90, 85, 95],
#     ["小刚", 60, 72, 68],
# ]
# for score in scores:
#     name = score[0]
#     score_only = score[1:]
#     print(score_only)
#     total = 0
#     for item in score_only:
#         total += item
#     print(f"{name}的总分为: {total},平均分为:{total/len(score_only):.2f}")

#练习8:
# a = [1, 3, 2]
# b=a.copy()       #copy是只复制,sorted是又复制又排序
# b.append(4)
# print(b)
# print(a)

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






