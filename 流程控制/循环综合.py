#练习1:
# a = 0
# i = 1
# n = int(input("请输入一个正整数:"))
# while i<=n:
#     if i%3==0 and i%5!=0:
#         print(i ,end=" ")
#         a+=1
#     i+=1
# print(f"正整数个数为{a}")

#练习2:
# min = 100          # 不要用max,用max_score或hi同理用low
# max = 0
# i =0
# sum = 0
# while True:
#     score = int(input("请输入成绩:"))
#     if score<=100 and score>=0:
#         i+=1
#         sum+=score
#         if score>=max:
#             max=score
#         if score<=min:
#             min=score
#     elif score==-1:    #  下次可以先把不满足的条件写最前面
#         break
#     else:
#         print("成绩要在 0 到 100 之间")
# print(f"正整数个数为{i}")
# print(f"平均数为:{sum/i}")
# print(f"最大数为{max},最小数为{min}")

#练习3数字反转:
# i = 1
# w = 1
# n = int(input("请输入一个正整数:"))
# while True:
#     n/=10
#     if n>=1:
#         w+=1
#     else:
#         break
#
# while i<=w:
#      r = n%(10**i)
#      i+=1
#      print(r)
#可以不用算位数的:
# n = int(input("请输入一个正整数:"))
# reverse = 0
# while n>0:
#     reverse = reverse*10+n%10       #*10空出一个位置把取个位n%10的数字放进去
#     n//=10       #整除舍掉个位
# print(reverse)

#练习4:
# n = int(input("请输入一个正整数:"))
# original =n
# reverse = 0
# while n>0:
#     reverse = reverse * 10 + n % 10
#     n//=10
# if reverse==original:
#     print(f"{original}是一个回文数")
# else:
#     print(f"{original}不是一个回文数")

#练习5:
# for i in range(100,1000):
#     original = i
#     ge = i%10
#     shi = i//10%10
#     bai = i//100%10
#     sum = ge**3+shi**3+bai**3   几次方的表示
#     if sum == original:
#         print(original)

#练习6:
# i = 0
# a = 1
# b = 1
# while i<=20:
#     c = a+b
#     a
#     i+=1

#*************
#答案:
# a = 1
# b = 1
# for i in range(20):     #可以用for来表示次数,后面不引用i即可
#     print(a, end=" ")
#     a, b = b, a + b

#***********************
# a = 2
# b = 1
# total = 0
# for i in range(20):
#     a,b = a+b,a      #******同时赋值
#     total+= a/b
# print(f"{total:.2f}")

#练习7:
# num1 = 0
# num2 = 0
# num3 = 0
# num4 = 0
# a = input("请输入一行字符:")
# for i in a:
#     for j in range(10):
#         if i==str(j):
#             num1+=1
#     for k in ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'):
#         if i==k:
#             num2+=1
#     if i==" ":
#         num3+=1
#     else:
#         num4+=1
# print(f"数字数为:{num1}")
# print(f"英文字母数为:{num2}")
# print(f"空格数为:{num3}")
# print(f"其他字符数为:{num4}")
#
# *******改错:遍历输入用循环,条件判断用条件把所有可能列进if中
# text = input("请输入一行字符:")
#
# letters = 0
# digits = 0
# spaces = 0
# others = 0
#
# for ch in text:
#     if "a" <= ch <= "z" or "A" <= ch <= "Z"    考虑大小写
#         letters += 1
#     elif "0" <= ch <= "9":
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         others += 1
#
# print(f"英文字母数为:{letters}")
# print(f"数字数为:{digits}")
# print(f"空格数为:{spaces}")
# print(f"其他字符数为:{others}")

#练习8:
# i = 1
# answer = 42
# while True:
#     a = int(input("请输入猜测的数:"))
#     if a>answer:
#         print("猜大了")
#         i +=1
#         continue
#     elif a<answer:
#         print("猜小了")
#         i +=1
#         continue
#     else:
#         print("猜对了")
#         break
# print(f"猜了{i}次")

# #练习9:
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 1:
#         total += i
#     i = i + 1
# print(total)
