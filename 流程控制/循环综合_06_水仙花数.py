#练习5:
for i in range(100,1000):
    original = i
    ge = i%10
    shi = i//10%10
    bai = i//100%10
    sum = ge**3+shi**3+bai**3   #几次方的表示（原来这句后面漏了 # 号，拆分时补上了）
    if sum == original:
        print(original)
