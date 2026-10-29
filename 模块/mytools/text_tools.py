def count_words(text:str)->int:
    """返回英文单词个数"""
    return len(text.split())

def reverse_text(text:str)->str:
    """将字符串反转之后再输出"""
    result = ""
    for i in text[::-1]:
        result += i
    return result


