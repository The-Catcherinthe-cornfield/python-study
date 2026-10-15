s = "Hello World 123"
su = s.upper()
print(su)
sl = s.lower()
print(sl)
print("-------------------")
#is判断
print("abc123".isalnum())   # True，字母或数字
print("123".isdigit())      # True，纯数字
print("abc".isalpha())      # True，纯字母
print("abc 123".isalnum())  # False，有空格
