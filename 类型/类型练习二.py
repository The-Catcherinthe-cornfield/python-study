#注解不等于强制类型
def add(a: int, b: int) -> int:
    return a + b


print(add(3, 4))            # 整数相加
print(add("1", "2"))        # 字符串相加
print(add(1.5, 2))          # 浮点数相加
print(add.__annotations__)  # 查看注解本身

