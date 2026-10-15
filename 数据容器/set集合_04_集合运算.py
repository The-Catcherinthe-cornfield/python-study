# 4 集合的运算:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

q = a.intersection(b)    #&交集
print(q)

w = a.union(b)            #|并集
print(w)
print(a|b)
e = a.difference(b)
print(e)

r = b.difference(a)
print(r)

t = a.symmetric_difference(b)  #对称集^^^:只出现在其中一个集合的元素
print(t)
