# Class類別
#
# class類別名稱:
#     def__init__(self,參數1,參數2,...):
#         #初始化內容，可以傳入參數
#         #使用self.變數=數值，來定義類別內的變數數值
#     def 函數名稱(self,參數1,參數2,...):
#         #函數內容，可使用self.變數，來操作類別內的變數
#         #self.函式(...)，呼叫其他函式


# 列舉
import enum
class JobTypes(enum.Enum):
    Empty = 0
    RD = 1
    PM = 2
    QA = 3

class human_Being:
    def __init__(self, name, age, job: JobTypes):
        self.name = name
        self.age = age
        self.job = job
        # print("init")

    def greet(self):
        print("Hi,I'm " + self.name + ".")

    def change_name(self, new_name):
        self.name = new_name


# inheritance繼承

# class Chinese(human_Being):
    # def greet(self):
        # print("我是" + self.name + "。")


# cp1 = Chinese("張三", 30)
# cp1.greet()


# p1 = human_Being("Rex", 30)
# p1.greet()
# print("\n")
# p1.change_name("William")
# p1.greet()

# p2 = human_Being("Alice", 28)
# p2.greet()


# JobTypes
# 列舉enum

p1 = human_Being("William", 30, JobTypes.RD)
print(p1.job.value)
