sentence = input("请输入一句英文：")
words = sentence.split()        #数数量应该先拆分成列表用split
# print(words)
# print(words[0])

abbr = ""
for w in words:
    abbr += w[::]

print(f"单词数：{len(words)}")
print(f"缩写：{len(abbr)}")
