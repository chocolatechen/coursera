unit_cost = int(input("unit cost: ")) # 單位進貨成本
unit_price = int(input("unit price: ")) # 零售價格
probable_demand = int(input("probable demand: ")) # 需求個數

x = 0
probability = []
profit = 0
except_profit = []
max_profit = 0
optimistic_order_quantity = 0

for i in range(probable_demand + 1):
    probability.append(float(input(f"probability of selling {i}: "))) # 賣出n個的機率
for i in range(probable_demand + 1):
    for x in range(probable_demand + 1):
        # 每種訂貨量之利潤 =  賣出n個的機率 * [(需求個數, 訂貨數)取小的 * 單位利潤 - 訂貨量 * 單位進貨成本]
        profit += probability[x] * (min(i, x) * unit_price - unit_cost * i)
        if x == probable_demand:
            except_profit.append(profit)
            profit = 0

for i in range(probable_demand + 1):
    if max_profit < except_profit[i]:
        max_profit = except_profit[i]
        optimistic_order_quantity = i

print(f"{optimistic_order_quantity} {int(max_profit)}")
