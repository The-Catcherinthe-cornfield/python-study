#7拆包练习:
t = (1, 2, 3)
a,b,c = t
print(a)
print(a,b,c)
print("----------------------------")
o,*rest = t
print(o)
print(rest)

x = 10
y = 20
x,y = y,x
print(x,y)
