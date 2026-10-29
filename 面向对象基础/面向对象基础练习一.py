class Student:
    """学生类:包括姓名,分数,及及格判断"""
    def __init__(self, name, score):
        self.Name = name
        self.Score = score


    def introduce(self):
        if self.Score >= 60:
            print(f"{self.Name}:{self.Score}分,及格")
        else:
            print(f"{self.Name}:{self.Score}分,不及格")

    def is_pass(self):
        if self.Score >= 60:
            return True
        else:
            return False


s1=Student("小明",88)
s2=Student("小红",55)
s1.introduce()
s2.introduce()
print(s1.is_pass(), s2.is_pass())