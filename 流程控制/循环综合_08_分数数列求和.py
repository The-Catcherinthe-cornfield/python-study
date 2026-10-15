#***********************
#（练习6 里的另一问：同样的数列，求前 20 项之和）
a = 2
b = 1
total = 0
for i in range(20):
    a,b = a+b,a      #******同时赋值
    total+= a/b
print(f"{total:.2f}")
