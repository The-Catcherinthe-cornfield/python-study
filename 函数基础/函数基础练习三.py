#通讯录查询
def is_valid_phone(phone):
    """手机号必须是 11 位纯数字，返回 True 或 False"""
    if len(phone) == 11 and phone.isdigit():#运用isdigit判断是否同时是数字才行
        return True
    else:
        return False
def add_contact(book, name, phone):
    """校验通过就存进 book 并返回 True，否则返回 False"""
    if is_valid_phone(phone):
        book[name] = phone
        return True
    else:
        return False
def find_contact(book, name):
    """查到返回电话号码，查不到返回 None"""
    return book.get(name, None)    #get的特性找不到自动返回None不用单独再写一遍
def del_contact(book, name):
    """删除成功返回 True，不存在返回 False"""
    if name in book:     #用in判断键在不在比用get更好
        del book[name]
        return True
    else:
        return False
def show_all(book):
    """打印所有联系人；通讯录为空时提示"通讯录为空" """
    if book:
     for name, phone in book.items():  #同时取出一对键值
         print(f"{name},{phone}")
    else:
        print("通讯录为空")
def main():
    book = {}
    while True:
        print("1. 添加  2. 查询  3. 删除  4. 显示全部  0. 退出")
        choice = input("请选择：")

        match choice:
            case "0":
                print("再见")
                break
            case "1":
                name = input("姓名：")
                phone = input("电话：")
                if add_contact(book, name, phone):#if True/false都是写死的常量,想要运用就把包含他们(return)的函数写进if
                    print("添加成功")
                else:
                    print("手机号格式不对")
            case "2":
                name = input("姓名：")
                phone = find_contact(book, name)
                if phone is None:
                    print("查无此人")
                else:
                    print(f"{name},{phone}")
            case "3":
                name = input("姓名：")
                # TODO：调用 del_contact，返回 False 就提示"没有这个人"
                if del_contact(book, name):
                    print("删除成功")
                else:
                    print("没有这个人")
            case "4":
                show_all(book)
            case _:
                print("无效选择")
main()


