'''class account_item:
    def __init__(self, food: list, clothing: list, housing: list, transportation: list, recreation: list):
        self.food = food
        self.clothing = clothing
        self.housing = housing
        self.transportation = transportation
        self.recreation = recreation


list2 = []
search_max = 1800
search_min = 1200

AC1 = account_item([790, 1590], [2200, 1350], [], [1200, 500, 1125], [])

for i in AC1.clothing:
    if search_min <= i <= search_max:
        list2.append(i)


for i in list2:
    print(i)
'''


import enum

# 撰寫有限的類別資料 ex.Type限制在RD、PM、QA
# 寫數字文字對照表
class CostType(enum.Enum):
    food = "食"
    clothing = "衣"
    housing = "住"
    transportation = "行"
    recreation = "娛樂"


class AccountItem2:
    def __init__(self, cost_type: CostType, price: int):
        self.cost_type = cost_type
        self.price = price


'''
AC1 = AccountItem2(CostType.transportation, 1200)
AC2 = AccountItem2(CostType.transportation, 500)
AC3 = AccountItem2(CostType.clothing, 2200)
AC4 = AccountItem2(CostType.clothing, 1700)
AC5 = AccountItem2(CostType.food, 790)
AC6 = AccountItem2(CostType.transportation, 1125)
AC7 = AccountItem2(CostType.food, 1590)
AC8 = AccountItem2(CostType.clothing, 1350)
'''


list1 = []
# list1: List[AccountItem2] = []
list1.append(AccountItem2(CostType.transportation, 1200))
list1.append(AccountItem2(CostType.transportation, 500))
list1.append(AccountItem2(CostType.clothing, 2200))
list1.append(AccountItem2(CostType.clothing, 1700))
list1.append(AccountItem2(CostType.food, 790))
list1.append(AccountItem2(CostType.transportation, 1125))
list1.append(AccountItem2(CostType.food, 1590))
list1.append(AccountItem2(CostType.clothing, 1350))


list2 = []
search_max = 1800
search_min = 1200
search_type = CostType.clothing


for i in list1:
    if i.cost_type == search_type:
        if search_min <= i.price <= search_max:
            list2.append(i)


for i in list2:
    print(i.cost_type, ":", i.price, "\n")






