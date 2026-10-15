#练习8:
p = float(input("商品单价:"))
pcs = float(input("购买数量:"))
pay = float(input("实付金额:"))
re = pay-pcs*p
if pay>=pcs*p:
    print(f"应找回{re:.2f}")
else:print("买不起")
