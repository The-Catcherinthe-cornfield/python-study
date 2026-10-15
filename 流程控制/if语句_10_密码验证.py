#密码应用:
i = 3
s = "python123"
while(i>=0):
    a = input("请输入登录密码:")
    if(a!=s):
        print(f"密码错误,你还有{i}次登陆机会")
        i-=1
    else:
        print("登录成功")
print("账号已锁定")
