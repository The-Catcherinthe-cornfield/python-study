#8:
s = input("请输入一个字符串：")
chars = set(s)

print(f"一共有 {len(chars)} 种不同字符")   #统计有多少种不同字符直接先转换成集合利用其不重复特性统计长度就行了
print(sorted(chars))                     #sorted默认从小到大排序
