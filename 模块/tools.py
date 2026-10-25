import math


def is_even(n:int)->bool:
    """判断整数是否为偶数"""
    if n % 2 == 0:
        return True
    else:
        return False

def circle_area(r:float)->float:
    """计算圆的面积"""
    return math.pi * r**2

def count_words(text:str)->int:
    """判断英文字符串单词个数"""
    return len(text.split())