class Student:
    school="黑马程序员"
    def __init__(self,name,score):
        self.name=name
        self.score=score



a = Student("小明",85)
b = Student("小红",92)
a.score=90
print(f"小明的分数为:{a.score}")
print(f"小红的分数为:{b.score}")
Student.school="黑马AI学院"
print(a.school)
print(b.school)
a.school="个人自学"
print(a.school)
print(b.school)
print(Student.school)