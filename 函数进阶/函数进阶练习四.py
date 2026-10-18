def add_append(scores, score):
    scores.append(score)

def add_new(scores, score):
    scores = scores + [score]  #这里是创建了一个新的列表,而打印scores还是原来的列表
    return scores


lst = [1,2,3,4]
add_append(lst,10)
print(lst)
add_new(lst,10)
print(lst)