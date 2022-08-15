#a = -3
#print(min(15, 3, 2, 7, 6, a))

my_str = "字串"
my_number = 3.1415926

pstr = "string:%s number:%.4f" % (my_str, my_number)
# print(pstr)

# sstr = "string:{:s} number:{:.4f}".format(my_str,my_number)
# print(sstr)

# fstr = f"字串：{my_str} 數字:{round(my_number,4)}"
# print(fstr)

check = True
print(type(check))
print(type(pstr))

a = 3**3
print(a)

my_list = [1, 2, 3, 4, "string"]
print(my_list)
my_list.append("new string")
print(my_list)
my_list.remove(3)
print(my_list)

print(my_list.index("new string"))

my_list2 = my_list[2:4] # 只包含第2第3個元素，不會包含第4個元素
print(my_list2)

print("\n")
# Tuple 元組 只能當作索引，不能改值
tup = ("apple", "banana", "grape")
print(tup[2])

print("\n")
# Set集合 syntax {data1,data2,...}  or set([data1,data2,...]) 自動過濾重複元素、可以做更改、可以取交集...

s1 = {1, 2, 3, 4, 5, 2, 3, 4}
s1.add("123")
print(s1)
s1.remove(3)
print("s1:", s1)
s2 = {2, 4, 55, 123}
print("s2:", s2)
print(s1 | s2) #聯集
print(s1 & s2) #交集
print(s1 - s2) #差集

print("\n")
# Dictionary字典
# 特色:針對某個物件得到某個數值
# key:value
# {key1:value1,key2:value2,...}
# dict({key1:value1,key2:value2...})
d = {1: "str1", 2: "str2", 3: "str3", "key1": 135}
print(type(d))
print(d)
print(d["key1"])

print("\n")
# 資料轉型
# 型態(數值)
# 數字to字串 浮點數to整數

name = "Bob"
age = 30
# print(name + age) #會顯示TypeError
print(name + ":" + str(age))

money = 500
cost = "120"
print(money-int(cost))

num = 0.9
print(int(num))

# TypeHint提示變數型態
# Syntax Var:type = num
# 只是提示，而非限制
count: int = 1
count = "str"  # 因為前面寫了TypeHint，這一行會一直出現警告
print(count)

# 寫子函式時，可利用TypeHint來提示輸入
# def func(a: int, b: str)
#   print()

# 單行註解
''' 多
    行
    註
    解 
'''

# If else 語法
# 用排版切割程式碼區塊
# 用

i = int(input("請輸入:"))
if i < 0:
    j = 0

elif i == 0:
    j = 1

else:
    j = 2

print(i, "\n")
print(j)

score = int(input("請輸入成績:"))
if score >= 80:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")

print("\n")
# For Loop
i = 0
for i in range(0, 5):
    print(i)

list1 = ["a", "b", "c", "d", "e"]
for i in list1:
    print(i)

print("\n")

# 此方法為產生一tuple輸出
for e in enumerate(list1):
    print(e)
    print(type(e))

for i, e in enumerate(list1):
    print(str(i) + "/" + e)  # 問題在於為何上一段e輸出格式會是(index, 'element')，但是這段e輸出只有 'element'

# while 條件:
#     要執行

t = 0
while t < 5:
    t = t + 1
    print("hi")

