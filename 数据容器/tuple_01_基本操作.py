#练习3:
t = (3, 1, 4, 1, 5, 9, 2, 6)
print(len(t))
print(t.count(1))
print(t.index(4))
for i in t:
    print(i,end=" ")
print()
print(5 in t, end="\n")    #直接用in判断就行
print(7 in t)
