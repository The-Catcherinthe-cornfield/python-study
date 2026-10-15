#练习8:
i = 1
answer = 42
while True:
    a = int(input("请输入猜测的数:"))
    if a>answer:
        print("猜大了")
        i +=1
        continue
    elif a<answer:
        print("猜小了")
        i +=1
        continue
    else:
        print("猜对了")
        break
print(f"猜了{i}次")
