#成绩统计与报告
def analyze(scores):
    """传入分数列表，返回 (总分, 平均分, 最高分, 最低分)"""
    sum = 0
    ma_x=scores[0]
    mi_n=scores[0]
    for score in scores:
        sum += score
        if score > ma_x:
            ma_x = score
        if score < mi_n:
            mi_n = score
    aver = sum / len(scores)
    return sum,aver, ma_x, mi_n
def report(name, scores):
    """打印一行统计结果"""
    a,b,c,d=analyze(scores)    #怎么加中文描述呢:可以先把数据解包出来因为analyze返回元组,之后在打印的时候再用f_string加中文
    print(f"{name},总分{a},平均分{b:.1f},最高分{c},最低分{d}")
report("小明",[88, 92, 75, 60, 99])