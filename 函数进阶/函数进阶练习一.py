count = 0

def record(name):
    global count  #声明函数中用的是全局变量
    count += 1
    print(f"第{count}次记录:{name}")


def change_local():
    count = 100
    print(count)


record("数学")
record("英语")
record("物理")
print(f"总的记录次数是{count}")
change_local()
print(count)
