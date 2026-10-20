def total(*args):
    """返回所有数字之和，没有参数时返回 0"""
    total = 0
    for arg in args:
        total += arg
    return total


def average(*args):
    """返回平均值，没有参数时返回 0"""

    if len(args) == 0:
        return 0  #可以先写提前返回的结构更好
    else:
        return total(*args)/len(args)


print(total(1, 2, 3))
print(total())
print(average(88, 92, 75))
print(average())