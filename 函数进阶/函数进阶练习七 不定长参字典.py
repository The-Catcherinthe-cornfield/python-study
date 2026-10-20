def build_profile(name, **info):    #**info表示等着实际额外补充的关键词传参字典类型
    """打印姓名、附加信息条数，以及每一条键值对"""
    print(name)
    print(f"额外补充的信息条数为:{len(info)}")
    for key, value in info.items(): #用for循环抽出键值对
        print(f"{key}:{value}")   #两个{}{}可以打印出对应的键值对还可以套入f_string中不必像items一样打印出的是字典键值对


build_profile("小明", age=18, city="北京", hobby="篮球")
build_profile("小红")