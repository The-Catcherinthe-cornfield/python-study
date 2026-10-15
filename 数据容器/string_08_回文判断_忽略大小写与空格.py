#**********不区分大小写和空格版:
text = input("请输入一串字符:").lower().replace(" ","")   #全部变成一样的大或小写即可
if text==text[::-1]:
    print("是")
else:
    print("不是")
