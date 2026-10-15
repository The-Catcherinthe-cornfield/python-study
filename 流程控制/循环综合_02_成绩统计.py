#练习2:
min = 100          # 不要用max,用max_score或hi同理用low
max = 0
i =0
sum = 0
while True:
    score = int(input("请输入成绩:"))
    if score<=100 and score>=0:
        i+=1
        sum+=score
        if score>=max:
            max=score
        if score<=min:
            min=score
    elif score==-1:    #  下次可以先把不满足的条件写最前面
        break
    else:
        print("成绩要在 0 到 100 之间")
print(f"正整数个数为{i}")
print(f"平均数为:{sum/i}")
print(f"最大数为{max},最小数为{min}")
