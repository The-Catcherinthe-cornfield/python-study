def register(name, age, city):
    print(f"姓名{name} 年龄{age} 来自{city}")


register("张三",18,"北京")
register(name="张三",age=18,city="北京")
register("张三",age=18,city="北京")
# 如果要混用位置参数必须在关键字前面,否则会报错