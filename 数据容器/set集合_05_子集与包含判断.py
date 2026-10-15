#5:
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {7, 8}
q = a|b==b
print(f"a是否是b的子集:{q}")

# w = a&c!=0    #错误写法因为a&b的结果是个集合永远不等于0
# print(w)

print(a<=b)  #谁小谁为子集

print(a.isdisjoint(c))   #判断是否没有共同元素

print(3 in a)   #判断数是否在a内

print(len(b))
