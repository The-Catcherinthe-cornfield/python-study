from tools import is_even,circle_area,count_words


result = is_even(18)
print(f"18是偶数吗:{result}")

r = 2
area =  circle_area(r)
print(f"半径为2的圆面积:{area:.2f}")

shu = count_words("hello world python")
print(f"单词个数:{shu}")