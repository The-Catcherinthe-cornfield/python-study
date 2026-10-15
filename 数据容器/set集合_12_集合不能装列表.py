#10 的实验：集合里放列表会怎样
s = {1, 2, [3, 4]}    #这一行会报 TypeError: unhashable type: 'list'
print(s)
