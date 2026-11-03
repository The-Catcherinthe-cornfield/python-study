class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"姓名:{self.name},年龄:{self.age}")
class Teacher(Person):
    def teach(self):
        print("开始讲课")

teacher = Teacher("张三",30)
teacher.introduce()
teacher.teach()