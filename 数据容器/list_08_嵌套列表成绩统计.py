#练习7:列表嵌套（第二部分：嵌套列表统计成绩）
scores = [
    ["小明", 88, 92, 75],
    ["小红", 90, 85, 95],
    ["小刚", 60, 72, 68],
]
for score in scores:
    name = score[0]
    score_only = score[1:]
    print(score_only)
    total = 0
    for item in score_only:
        total += item
    print(f"{name}的总分为: {total},平均分为:{total/len(score_only):.2f}")
