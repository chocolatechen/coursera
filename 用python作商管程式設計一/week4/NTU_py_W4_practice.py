unit_cost = int(input("unit cost: ")) # 單位進貨成本
unit_price = int(input("unit price: ")) # 零售價格
probable_demand = int(input("probable demand: ")) # 需求個數
order_quantity = int(input("order quantity: ")) # 訂貨量

sales = 0

for i in range(probable_demand + 1):
    probability = float(input(f"probability of selling {i}: ")) # 賣出n個的機率
    # 營收 =  (訂貨量,需求個數)取小的 * 賣出n個的機率 * 每個的利潤
    sales += min(i, order_quantity) * probability * unit_price

# 利潤 = 營收 - 訂貨量 * 單位進貨成本
profit = int(sales - order_quantity * unit_cost)
print(profit)
