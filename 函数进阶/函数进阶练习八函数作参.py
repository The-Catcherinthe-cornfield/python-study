def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def apply(func, a, b):
    return func(a,b)

print(apply(add,7,3))
print(apply(sub,7,3))
op = add
print(apply(op, 100, 1))
print(apply(add(), 3, 4))