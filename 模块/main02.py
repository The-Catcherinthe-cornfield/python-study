from mytools.math_tools import circle_area,is_even
from mytools.text_tools import count_words,reverse_text
import mytools

print(f"18是否为偶数:{is_even(18)}")
print(f"半径为2的圆的面积:{circle_area(2):.2f}")
print(f"单词数为:{count_words("i love corn")}")
print(f"反转:{reverse_text("hello python")}")
print(f"包版本:{mytools.__version__}")   #引入__init__里的就直接从包里引入就行,因为__init__里的东西算包的性质