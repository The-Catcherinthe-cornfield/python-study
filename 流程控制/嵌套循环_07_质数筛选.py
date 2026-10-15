#练习7:
for n in range(2,101):
    is_prime = True    #运用标志变量
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n,end=" ")
