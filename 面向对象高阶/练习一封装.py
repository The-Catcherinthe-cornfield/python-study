class Student:
    def __init__(self,name,score):
        self.name=name
        self.__score=score
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if score<0 or score>100:
            print("成绩超出范围")
        else:
            self.__score=score


student = Student("小明",85)
print(student.get_score())
student.set_score(95)
print(student.get_score())
student.set_score(120)
print(student.get_score())