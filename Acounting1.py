list1 = [1200, 500, 2200, 1700, 790, 1125, 1590]
list2 = []

search_max = 1800
search_min = 1200
for i in list1:
    if i <= search_max and i >= 1200:
        list2.append(i)

for i in list2:
    print(i)
