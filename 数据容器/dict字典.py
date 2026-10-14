#练习1:查找单词及其对应出现次数                构造字典的键与值对应
a = input("请输入一串英文:")
worlds = a.split(" ")       #关键在这:先别想字典先找出键即单词
counts = {}
for word in worlds:
    counts[word] = counts.get(word, 0) + 1   #字典名[键]=值,且字典自动去重,get找到一次word值就加一
for x,y in sorted(counts.items(), key=lambda x: x[1], reverse=True):   #counts.items()表示遍历的是键值对,key=lambda x: x[1]表示sorted的排列决定因素是值也就是下标为1的位置,reverse=True表示排倒序
   print(f"单词:{x} 出现次数:{y}")

#2:
scores = {
    "小明": {"语文": 88, "数学": 92, "英语": 75},
    "小红": {"语文": 90, "数学": 85, "英语": 95},
    "小刚": {"语文": 60, "数学": 72, "英语": 68},
}
