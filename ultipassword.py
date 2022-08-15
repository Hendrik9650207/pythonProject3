
import random
ans = random.randint(1, 100)

low = 1
high = 100

while True:
    i = int(input("請輸入數字:"))
    print(i)
    if i == ans:
        print("猜中")
        break
    else:
        print(ans)
        if low <= i < ans:
            low = i

        elif ans < i <= high:
            high = i

        print("最高:", high, "最低", low)

