f1 = lambda x: x * 2 if x > 0 else 0
f2 = lambda: 42
# f3 = lambda x:x= x + 1  lambda后面只能接有结果的东西
f4 = lambda x: print(x)

print(f1(-3))
print(f2())
f4(5)

def df1(x):
    if x > 0:
        return x*2
    else:
        return 0

def df2():
    return 42


df2()
print(df2())
print(df1(-3))