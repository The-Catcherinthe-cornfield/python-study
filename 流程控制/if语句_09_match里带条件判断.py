#改错:在case中运用条件判断:case x if x...
score = 1
match score:
     case s if s>90:
         print("优秀")
     case s if s>60:
          print("及格")
     case _:
         print("不及格")
