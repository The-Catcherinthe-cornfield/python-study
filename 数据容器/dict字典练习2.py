#输出成绩:
scores = {
    "小明": {"语文": 88, "数学": 92, "英语": 75},
    "小红": {"语文": 90, "数学": 85, "英语": 95},
    "小刚": {"语文": 60, "数学": 72, "英语": 68},
}
subject = scores.values()
subjects = tuple(subject)
chacter = tuple(scores.keys())
best = ""
ma_x = 0
for i in range(len(chacter)):    #用人数长度来表示循环次数对了并且后面还方便选最大的人
    a = tuple(subjects[i].values())
    total=0  #不要用sum来表示总和
    for j in a:
        total += j

    if total>ma_x:
        ma_x = total
        best=chacter[i]
    print(f"{chacter[i]}的总分为:{total}")
    print(f"{chacter[i]}的平均分为:{total/len(a):.1f}")

print(f"总分最高的人是:{best}")