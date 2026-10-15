#练习5:
t = (1, 2, 3)
lst = list(t)
lst[0] = 100
lst.append(4)           #append就单独写一行不要用它去输出他只是执行一个操作后lst已经改变要去找lst
t = tuple(lst)
print(t)
