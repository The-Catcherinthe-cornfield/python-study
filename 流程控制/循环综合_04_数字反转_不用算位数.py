#可以不用算位数的:
n = int(input("请输入一个正整数:"))
reverse = 0
while n>0:
    reverse = reverse*10+n%10       #*10空出一个位置把取个位n%10的数字放进去
    n//=10       #整除舍掉个位
print(reverse)
