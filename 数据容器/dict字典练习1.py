#练习1:查找单词及其对应出现次数                构造字典的键与值对应
a = input("请输入一串英文:")
worlds = a.split()       #关键在这:先别想字典先找出键即单词
counts = {}
for word in worlds:
    counts[word] = counts.get(word, 0) + 1   #字典名[键]=值,且字典自动去重,先执行get找一个就往左边的字典里存并且值加一如已存在则覆盖
for x,y in sorted(counts.items(), key=lambda x: x[1], reverse=True):   #counts.items()表示遍历的是键值对,key=lambda x: x[1]表示sorted的排列决定因素是值也就是下标为1的位置,reverse=True表示排倒序
   print(f"单词:{x} 出现次数:{y}")

