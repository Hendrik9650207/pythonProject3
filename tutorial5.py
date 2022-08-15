# 作業域變更：在此區定義的變數，會被視為區域變數，外部程式無法直接存取。
# 在if...else、for/while、try/except/finally不會改變作用域。
# 在def、class、lambda內才會改變作用域


# if True:
    # x = 10
# x += 5
# print(x)
# for i in range(0, 10):
    # pass
# print(i)

x = 0
def func1():
    global x # global使得子函數能夠更改全域變數
    x = 1000
    print("func1", x)


func1()


# 說明:一開始宣告一全域變數y，並令其等於1。
# 在func2的裡面再宣告一個子函數func3
# 在func3中運用nonlocal去更改func2中的變數
y = 1
def func2():
    y = 100

    def func3():
        nonlocal y
        y = y + 101
        print("func3", y)

    func3()
    print("func2", y)


func2()
print("global", y)


# Input
# input("提示")
# 以字串儲存