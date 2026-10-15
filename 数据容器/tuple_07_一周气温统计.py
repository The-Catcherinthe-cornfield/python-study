#8一周气温计:
ma_x = 0
mi_n = 50
sum = 0
temps = (28.5, 30.2, 27.8, 31.0, 29.6, 33.1, 26.9)
for temp in temps:
    sum += temp
print(f"{sum/len(temps):.1f}")
for temp in temps:
    if temp > ma_x:
        ma_x = temp
    if temp < mi_n:
        mi_n = temp
print(mi_n)
print(ma_x)
result = sorted(temps,reverse=True)
print(result)
