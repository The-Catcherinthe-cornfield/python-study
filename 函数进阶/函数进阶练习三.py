call_count = 0

def average(scores):
    global call_count
    total = 0
    for i in scores:
        total += i
    aver =total/len(scores)
    call_count += 1
    return aver


def show_report(name, avg):
    print(f"姓名{name},平均分{avg}")


avg1 = average([88, 92, 75])
avg2 = average([90, 85, 95])
show_report(avg=avg1,name="小明")
show_report("小红",avg2)
print(f"函数总共调用{call_count}次")