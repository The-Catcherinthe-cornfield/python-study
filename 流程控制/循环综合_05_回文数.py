#练习4:
n = int(input("请输入一个正整数:"))
original =n
reverse = 0
while n>0:
    reverse = reverse * 10 + n % 10
    n//=10
if reverse==original:
    print(f"{original}是一个回文数")
else:
    print(f"{original}不是一个回文数")
