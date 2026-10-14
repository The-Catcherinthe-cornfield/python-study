#练习3:
# t = (3, 1, 4, 1, 5, 9, 2, 6)
# print(len(t))
# print(t.count(1))
# print(t.index(4))
# for i in t:
#     print(i,end=" ")
# print()
# print(5 in t, end="\n")    #直接用in判断就行
# print(7 in t)

#练习4  改数:
#方法一 构建新元组:
# t = (1, 2, 3)
# s = 100
# a,b,c = t
# r = (s,b,c)
# print(r)
# #方法2 转换成列表用到list与tuple函数:
# t = (1, 2, 3)
# lst = list(t)
# lst[0] = 100
# t = tuple(lst)
# print(t)

#练习5:
# t = (1, 2, 3)
# lst = list(t)
# lst[0] = 100
# lst.append(4)           #append就单独写一行不要用它去输出他只是执行一个操作后lst已经改变要去找lst
# t = tuple(lst)
# print(t)

#练习6 拼接重复与排序:
# t1 = (1, 2)
# t2 = (3, 4)
# t = (3, 1, 4, 1, 5)
# print(t1+t2)
# print(t1*3)
# result = sorted(t)
# print(result)
# print(t)

#7拆包练习:
# t = (1, 2, 3)
# a,b,c = t
# print(a)
# print(a,b,c)
# print("----------------------------")
# o,*rest = t
# print(o)
# print(rest)

# x = 10
# y = 20
# x,y = y,x
# print(x,y)

#8一周气温计:
# ma_x = 0
# mi_n = 50
# sum = 0
# temps = (28.5, 30.2, 27.8, 31.0, 29.6, 33.1, 26.9)
# for temp in temps:
#     sum += temp
# print(f"{sum/len(temps):.1f}")
# for temp in temps:
#     if temp > ma_x:
#         ma_x = temp
#     if temp < mi_n:
#         mi_n = temp
# print(mi_n)
# print(ma_x)
# result = sorted(temps,reverse=True)
# print(result)

#9元组记录数据:
# student = ("小明", 18, 95.5)
# a,b,c = student
# print(f"姓名:{a},年龄:{b},成绩:{c}")
# print("----------------")
# points = ((1, 2), (3, 4), (5, 6))
# for i in points:
#     x,y=i
#     print(i,end=" ")
#     print(f"{(x**2+y**2)**(1/2):.2f}")

#10:
# t = (1)
# print(type(t))

# t = (1, 2, [3, 4])
# t[2].append(5)
# print(t)
# t[2] = [9]

t = (1, 2)
# print(t + (3,))
print(t + (3))