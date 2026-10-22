students = [
    {"name": "小明", "score": 88},
    {"name": "小红", "score": 95},
    {"name": "小刚", "score": 72},
]
#可以先想把序排好先,之后再想怎么打印
rank = sorted(students, key=lambda x: x["score"], reverse=True)    #sorted是备份一份新的,如果想备着用不立刻打印那就要找一个变量来接收!
i = 1
sum = 0
# for student in rank:
#     print(f"{i}. {student['name']} {student['score']}")
#     i+=1
#     sum = sum + student['score']

for i,student in enumerate(rank,start=1):    #enumerate(a,b)用来处理既要元素又要其对应序号,a表示从哪里遍历,b表示序号从几开始,默认为0
    print(f"{i}. {student['name']} {student['score']}")
    sum = sum + student['score']

print(f"平均分为:{sum/len(rank):.1f}")