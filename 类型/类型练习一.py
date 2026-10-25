age: int = 18  #整数类型
name: str = "小明" #字符串类型
scores: list[int] = [88, 92, 75] #外类型为列表,列表内部是整数类型


def c_to_f(c: int)->float:
    return 9 * c / 5 + 32

def is_valid_phone(phone: str)->bool:
    return len(phone) == 11 and phone.isdigit()

def average(total:float,scores:tuple[int,...])->float:    #... 表示元组中任意的元素都是一种类型
    return total / len(scores)

def show_all(book:dict[str, str])->None:      #不返回值直接做事的返回None
    for name, phone in book.items():          #手机号是字符串形式
        print(f"{name}: {phone}")


print(c_to_f(3))
print(is_valid_phone("13978357810"))
print(average(100,(50,50)))
show_all({"张三":"100","李四":"90"})