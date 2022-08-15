import random
me = int(input("[0]蟲 [1]雞 [2]老虎 [3]棒  請出拳:"))
com = random.randint(0, 3)
trans = ["蟲", "雞", "老虎", "棒"]

print("你出的", trans[me])
print("對手:", trans[com])

if me == com:
    print("平手")
elif me == (com + 1) % 4:
    print("勝利")
else:
    print("輸了")


