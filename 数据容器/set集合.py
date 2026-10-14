#1:
# s1 = {1, 2, 3}
# s2 = {}
# s3 = set()
# s4 = {1, 1, 2, 2, 3}
# s5 = set("hello")
#
# print(type(s1))
# print(s2)
# print(type(s2))
# print(type(s3))
# print(s4)
# print(s5)

#2:
# nums = [3, 1, 3, 2, 1, 5, 2]
# st = set(nums)
# print(st)
# print(len(st))
# print(sorted(st))    #返回有序的列表

#3  集合的添加数(不需要转换成列表):
# s = {1, 2, 3}
# s.add(4)
# print(s)
#
# s.add(2)
# print(s)
#
# s.update([5,6])    #一次性添加多个数用update
# print(s)
#
# s.remove(1)
# print(s)
#
# s.discard(100)    #删除不存在的数用discard
# print(s)
#
# # s.clear()
# # print(s)
#
# s.remove(3)
# s.add(30)
# print(s)

# 4 集合的运算:
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
#
# q = a.intersection(b)    #&交集
# print(q)
#
# w = a.union(b)            #|并集
# print(w)
# print(a|b)
# e = a.difference(b)
# print(e)
#
# r = b.difference(a)
# print(r)
#
# t = a.symmetric_difference(b)  #对称集^^^:只出现在其中一个集合的元素
# print(t)

#5:
# a = {1, 2, 3}
# b = {1, 2, 3, 4, 5}
# c = {7, 8}
# q = a|b==b
# print(f"a是否是b的子集:{q}")

# w = a&c!=0    #错误写法因为a&b的结果是个集合永远不等于0
# print(w)

# print(a<=b)  #谁小谁为子集

# print(a.isdisjoint(c))   #判断是否没有共同元素

# print(3 in a)   #判断数是否在a内

# print(len(b))

#6:
# class_a = {"小明", "小红", "小刚", "小美"}
# class_b = {"小红", "小强", "小美", "小丽"}
# print(class_a&class_b)
# print(class_a|class_b)
# print(class_a-class_b)
# print(class_a^class_b)

#7 列表去重:
# nums = [3, 1, 3, 2, 1, 5]
# st = set(nums)
# print(st)
#-------方法二保留顺序------
# nums = [3, 1, 3, 2, 1, 5]
# result = []
# for num in nums:
#     if num not in result:
#         result.append(num)
# print(result)

#8:
# s = input("请输入一个字符串：")
# chars = set(s)

# print(f"一共有 {len(chars)} 种不同字符")   #统计有多少种不同字符直接先转换成集合利用其不重复特性统计长度就行了
# print(sorted(chars))                     #sorted默认从小到大排序

#9:
# a = [1, 2, 3, 4, 5, 3]
# b = [4, 5, 6, 7, 4]
# print(set(a))
# print(set(b)&set(a))
# print(set(a)-set(b))             #---------------→求只有谁有的元素就用其减去另一个
# print(set(b)-set(a))
# print(set(a)|set(b))

#10:
# s =set()
# print(type(s))
# j = {}
# print(type(j))

s = {1, 2, [3, 4]}
print(s)











