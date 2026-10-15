#9:
a = [1, 2, 3, 4, 5, 3]
b = [4, 5, 6, 7, 4]
print(set(a))
print(set(b)&set(a))
print(set(a)-set(b))             #---------------→求只有谁有的元素就用其减去另一个
print(set(b)-set(a))
print(set(a)|set(b))
