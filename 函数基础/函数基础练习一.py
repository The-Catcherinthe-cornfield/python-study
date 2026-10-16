def c_to_f(c):
    """摄氏温度转化为华氏温度
    """
    f=9*c/5+32
    return f
def f_to_c(f):
    c=5*(f-32)/9
    return c
def print_table(start, end, step):
   print(f"{'摄氏':<8}{'华氏':>8}")    #注意一行里面写两部分的写法:  :<8表示向左靠齐占8个格子,向右同理
   for c in range(start, end, step):
       print(f"{c:<8}{c_to_f(c):>8.1f}")
print_table(0,101,20)