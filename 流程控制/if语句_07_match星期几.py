#match的应用1:(相当于swith)
day = int(input("请输入星期几:"))
match day:
    case 1:
        print("星期一")
    case 2:
        print("星期二")
    case 3:
        print("星期三")
    case 4:
        print("星期四")
    case 5:
        print("星期五")
    case 6:
        print("星期六")
    case 7:
        print("星期七")
    case _:
         print("输入错误")
