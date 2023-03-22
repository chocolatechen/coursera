unit_cost = int(input("unit cost: ")) # 單位進貨成本
unit_price = int(input("unit price: ")) # 零售價格
probable_demand = int(input("probable demand: ")) # 需求個數
salvage_value = int(input("salvage_value: ")) # 殘值

probability = []
profit = 0
except_profit = []
max_profit = 0
optimistic_order_quantity = 0

for i in range(probable_demand + 1):
    probability.append(float(input(f"probability of selling {i}: "))) # 賣出n個的機率
for order_quantity in range(probable_demand + 1):
    for demand_quantity in range(probable_demand + 1):
        # 若訂貨量大於需求個數則殘值為其相減，反之則為0
        rest = order_quantity - demand_quantity if order_quantity - demand_quantity > 0 else 0
        #rest = order_quantity - demand_quantity if order_quantity >= demand_quantity else 0
        # 每種訂貨量之利潤 =  賣出n個的機率 * [(訂貨數, 需求個數)取小的 * 單位利潤 - 訂貨量 * 單位進貨成本] + 沒賣掉的機率 * 殘值 * 剩餘量
        profit += probability[demand_quantity] * (min(order_quantity, demand_quantity) * unit_price - unit_cost * order_quantity +salvage_value * rest)
        if demand_quantity == probable_demand:
            except_profit.append(profit)
            profit = 0

for i in range(probable_demand + 1):
    if max_profit < except_profit[i]:
        max_profit = except_profit[i]
        optimistic_order_quantity = i

print(f"{optimistic_order_quantity} {int(max_profit)}")
