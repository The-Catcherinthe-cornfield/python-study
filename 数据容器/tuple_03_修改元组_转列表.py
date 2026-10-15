#练习4  改数:
#方法2 转换成列表用到list与tuple函数:
t = (1, 2, 3)
lst = list(t)
lst[0] = 100
t = tuple(lst)
print(t)
