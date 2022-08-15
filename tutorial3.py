# 位置參數 *args
# 自動將多出的參數包裝成Tuple，並附加到args參數，以這種特性擴充參數
# 再匯入參數進子函式時，更為彈性
# 可以做到輸入不固定數量參數的功能
def my_sum_function(*r):
    total = 0
    for e in r:
        total += e
    print(total)
    print(type(r))


def sum_func(info, *reg):
    print(info)
    total = 0
    for e in reg:
        total += e
    print(total)
    print(type(reg))


my_sum_function(1, 2, 3, 4, 7)

sum_func("Add", 1, 2, 3, 4, 5)


# ==================費氏===================== #
t = 0
result = 0
a = 0
b = 1
while t < 9:
    print(result)
    if t == 0:
        print(b)

    result = a + b
    a = b
    b = result
    t = t + 1

x = 1

ans = 0
while ans <= 50:
    ans = ans + x
    print(x)
    x = x + 1
# ========================================= #

print("**kwargs")
# **kwargs參數
# 自動將多出的參數包裝成字典Dict，並附加到kwargs參數當中。

def print_user_info(id, name, age, **other): # 利用** 把其他參數包在other裡
    print(id)
    print(name)
    print(age)
    print(other)
    print(type(other),"\n")

print_user_info(1, age=27, name="Bob", email="abc@abc.com", address="Taiwan ,Taipei City")


print("lambda function")
# lambda函數   lambda 參數1, 參數2, ...:回傳值
# 匿名函式
# 快速動態定義函式
# 僅能用單行
add = lambda x, y: x + y
print(add(3,5))


def create_lambda_func(p):
    return lambda x, y: p*(x+y)


five = create_lambda_func(5)
print(five(3, 5))

six = create_lambda_func(6)
print(six(3, 5))

