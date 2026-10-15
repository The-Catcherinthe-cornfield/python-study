#练习3:
j = False
j1 = False
i = 0
t = -1
scores = [88, 92, 75, 92, 60, 92]
print(f"列表的长度为:{len(scores)}")
for score in scores:
    if score==92:
        i+=1
    if score==75:
        j = True
        continue
    if score==100:
        j = True
        continue
for an in range(len(scores)):     #用len配合[]来找位置range别漏掉
    if scores[an]==92:            #（原来这里写的是 scores[a]，变量名笔误，拆分时改成 an）
        t = an
        break
print(f"92出现的次数为:{i}")
print(f"75是否存在:{j}")
print(f"100是否存在:{j1}")
print(t)
