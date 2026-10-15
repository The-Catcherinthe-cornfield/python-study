#练习6:
#初版（当时没写完，留着当对比）:
# i = 0
# a = 1
# b = 1
# while i<=20:
#     c = a+b
#     a
#     i+=1

#*************
#答案:
a = 1
b = 1
for i in range(20):     #可以用for来表示次数,后面不引用i即可
    print(a, end=" ")
    a, b = b, a + b
