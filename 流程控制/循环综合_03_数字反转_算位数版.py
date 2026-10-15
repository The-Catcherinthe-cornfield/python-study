#练习3数字反转:
i = 1
w = 1
n = int(input("请输入一个正整数:"))
while True:
    n/=10
    if n>=1:
        w+=1
    else:
        break

while i<=w:
     r = n%(10**i)
     i+=1
     print(r)
