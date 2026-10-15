#9元组记录数据:
student = ("小明", 18, 95.5)
a,b,c = student
print(f"姓名:{a},年龄:{b},成绩:{c}")
print("----------------")
points = ((1, 2), (3, 4), (5, 6))
for i in points:
    x,y=i
    print(i,end=" ")
    print(f"{(x**2+y**2)**(1/2):.2f}")
