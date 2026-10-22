def filter_and_map(numbers, condition, transform):
    """挑出满足 condition 的数，把每个挑中的数用 transform 变换后放进新列表返回"""
    lst = []
    for n in numbers:
        if condition(n):   #记得numbers还是个列表不能直接算,要遍历,condition之后的是单个数可以直接算
            lst.append(transform(n))
    return lst


nums = [1, 2, 3, 4, 5, 6]
print(filter_and_map(nums,lambda n: n%2==0 , lambda n: n*n ))
print(filter_and_map(nums, lambda n:n>3, lambda n: n*10))
print(filter_and_map(nums, lambda n:n%2!=0, lambda n: -n))
