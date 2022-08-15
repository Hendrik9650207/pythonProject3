# def 函式名稱(參數1, 參數2,...)
#     涵式內容
#     可使用參數1、參數2...來代表傳入的數值
#     return 結果數值

# 傳遞參數 pass by assignment
# immutable object預設結果像是pass by value
# ex. 字串str、整數int、浮點數float...
# mutable object 預設結果像是pass by reference
# ex. 串列list、自定義class物件

def my_add_function(x, y):
    # print(x, y)
    return x + y


print(my_add_function(3, 7))


def add_one_and_print(x):
    x += 1
    print(x)


my_x = 100
add_one_and_print(my_x)
print(my_x)


def my_function(l: list):
    l.append(999)


mylist = [1, 2, 3, 4, 5]
my_function(mylist)
print(mylist)


def Recur(times: int):
    times += 1
    print(times)
    if times < 5:
        Recur(times)
    print("out" + str(times))


Recur(0)


