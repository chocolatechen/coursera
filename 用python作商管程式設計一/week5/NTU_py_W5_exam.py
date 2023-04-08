'''
loop start
    計算每個城鎮間的距離，以及其受益的總人數與涵蓋的城鎮
    挑出最多受益人數的城鎮蓋基地台，並記錄他
    將其涵蓋的城鎮人數歸零
loop end
'''

str = input("number of the city, signal station, allow distance: ").split()
num_town = int(str[0])          # 城鎮數
require = int(str[1])           # 基地台需求數
distance = int(str[2])          # 可接受距離
city_x = []                     # 城鎮x座標
city_y = []                     # 城鎮y座標
population = []                 # 城鎮人數

#讀取數據
for x in range(num_town):
    data = input().split()
    city_x.append(int(data[0]))
    city_y.append(int(data[1]))
    population.append(int(data[2]))

total_people = 0                                            # 總受益人數
max_people = 0                                              # 比較最多受益人數用
build = []                                                  # 紀錄欲蓋基地台之城鎮
benefit_town = [[0] * num_town for _ in range(num_town)]    # 紀錄受益城鎮
people = [0] * num_town                                     # 紀錄在每個城鎮蓋基地台可受益之人數

for i in range(require):
    for x in range(num_town):
        for y in range(num_town):
            if pow( pow(city_x[x] - city_x[y], 2) + pow(city_y[x] - city_y[y], 2), 0.5) <= distance:
                people[x] += population[y]
                benefit_town[x][y] = 1

    for x in range(num_town):
        if max_people < people[x]:
            max_people = people[x]
            town = x

    total_people += max_people
    build.append(town + 1)
    for x in range(num_town):
        if (benefit_town[town][x] != 0):
            population[x] = 0

    people = [0] * num_town
    max_people = 0

print(f"{build} {total_people}")
