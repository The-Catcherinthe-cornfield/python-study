def make_card(name, age, city="未知", phone="未知"):   #这里填未知等着之后自己输入如没有输入则可以显示出未知表示未填
    """打印一张名片"""
    print(f"姓名:{name}")
    print(f"年龄:{age}")
    print(f"城市:{city}")
    print(f"电话:{phone}")

make_card("小明", 18, "北京", "13800000000")
make_card("小红", 20)
make_card("小刚", 22, phone="13900000000")  #默认参数可以修改,但要写在右边
