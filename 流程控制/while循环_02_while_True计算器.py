#while True的用法(不用判断直接进行循环,但注意要写break)
a = float(input("请输入第一个数字:"))
b = float(input("请输入第二个数字:"))
while True:
    choice = int(input("请输入你的选择1或2或0 "))
    match choice:
        case 1:
            print(a+b)
        case 2:
            print(a-b)
        case 0:
            print("已退出程序")
            break
        case _:
            print("无效选择")
