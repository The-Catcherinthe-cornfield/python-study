#快递运费计算

class Delivery:
    def calculate_fee(self,weight):
        return weight*5


class ExpressDelivery(Delivery):
   def calculate_fee(self,weight):
       base = super().calculate_fee(weight)
       return base*5+10

a = Delivery()
print(f"普通快递费用:{a.calculate_fee(3):.2f}")
b = ExpressDelivery()
print(f"加急快递费用:{b.calculate_fee(3):.2f}")
