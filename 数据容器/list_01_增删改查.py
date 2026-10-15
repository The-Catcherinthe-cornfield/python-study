#练习1:
fruits = ["苹果", "香蕉", "橙子"]
fruits.append("葡萄")
print(fruits)

fruits.insert(1,"西瓜")
print(fruits)

fruits[0]="梨"
# fruits = ['梨', '西瓜', '香蕉', '橙子', '葡萄']
print(fruits)

fruits.pop(2)
print(fruits)

last = fruits.pop()
print(last)

del fruits[0]
print(fruits)
