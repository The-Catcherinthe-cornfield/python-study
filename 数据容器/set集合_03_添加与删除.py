#3  集合的添加数(不需要转换成列表):
s = {1, 2, 3}
s.add(4)
print(s)

s.add(2)
print(s)

s.update([5,6])    #一次性添加多个数用update
print(s)

s.remove(1)
print(s)

s.discard(100)    #删除不存在的数用discard
print(s)

# s.clear()
# print(s)

s.remove(3)
s.add(30)
print(s)
