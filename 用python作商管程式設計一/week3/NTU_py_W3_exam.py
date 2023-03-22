spend_money = int(input())

last = 0
first = True
repay = 1000 - spend_money

five_hundred = repay // 500
repay = repay - 500 * five_hundred
one_hundred = repay // 100
repay = repay - 100 * one_hundred
fifty = repay // 50
repay = repay - 50 * fifty
ten = repay // 10
repay = repay - 10 * ten
five = repay // 5
repay = repay - 5 * five
one = repay

if five_hundred != 0:
    last = last + 1
if one_hundred != 0:
    last = last + 1
if fifty != 0:
    last = last + 1
if ten != 0:
    last = last + 1
if five != 0:
    last = last + 1
if one != 0:
    last = last + 1

if five_hundred != 0:
    last = last - 1
    first = 0
    if last != 0:
        print(f"500, {five_hundred};", end = "")
    else:
        print(f"500, {five_hundred}", end = "")
        
if one_hundred != 0:
    last = last - 1
    if first: #是第一個
        if last != 0: #不是最後一個
            print(f"100, {one_hundred};", end = "")
        else: #是最後一個
            print(f"100, {one_hundred}", end = "")
    else: #不是第一個
        if last != 0: #不是最後一個
            print(f" 100, {one_hundred};", end = "")
        else: #是最後一個
            print(f" 100, {one_hundred}", end = "")
    first = 0
    
if fifty != 0:
    last = last - 1
    if first: #是第一個
        if last != 0: #不是最後一個
            print(f"50, {fifty};", end = "")
        else: #是最後一個
            print(f"50, {fifty}", end = "")
    else: #不是第一個
        if last != 0: #不是最後一個
            print(f" 50, {fifty};", end = "")
        else: #是最後一個
            print(f" 50, {fifty}", end = "")
    first = 0
    
if ten != 0:
    last = last - 1
    if first: #是第一個
        if last != 0: #不是最後一個
            print(f"10, {ten};", end = "")
        else: #是最後一個
            print(f"10, {ten}", end = "")
    else: #不是第一個
        if last != 0: #不是最後一個
            print(f" 10, {ten};", end = "")
        else: #是最後一個
            print(f" 10, {ten}", end = "")
    first = 0
    
if five != 0:
    last = last - 1
    if first: #是第一個
        if last != 0: #不是最後一個
            print(f"5, {five};", end = "")
        else: #是最後一個
            print(f"5, {five}", end = "")
    else: #不是第一個
        if last != 0: #不是最後一個
            print(f" 5, {five};", end = "")
        else: #是最後一個
            print(f" 5, {five}", end = "")
    first = 0
    
if one != 0:
    last = last - 1
    if first: #是第一個
        if last != 0: #不是最後一個
            print(f"1, {one};", end = "")
        else: #是最後一個
            print(f"1, {one}", end = "")
    else: #不是第一個
        if last != 0: #不是最後一個
            print(f" 1, {one};", end = "")
        else: #是最後一個
            print(f" 1, {one}", end = "")
    first = 0
