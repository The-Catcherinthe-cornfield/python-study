#应用2:
a = float(input("请输入第一个数字:"))
op = input("请输入运算符")
b = float(input("请输入第二个数字:"))
match op:
    case '+':
        print(f"运算结果为:{a+b:.2f}")
    case '-':
        print(f"运算结果为:{a-b:.2f}")
    case '*':
        print(f"运算结果为:{a*b:.2f}")
    case '/':
        if b!=0:
            print(f"运算结果为:{a/b:.2f}")
        else:
            print("除数不能等于零")
    case _:
        print("运算符错误")
