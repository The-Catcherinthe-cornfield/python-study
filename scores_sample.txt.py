f = open("scores_clean.txt", encoding="utf-8")

scores = []
for line in f:
    line = line.strip()
    # 这里：把 line 按逗号拆开，取第二段，转成小数，加进 scores
    ...

f.close()

# 这里：打印平均分（保留两位小数）和最高分
...