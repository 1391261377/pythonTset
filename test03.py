import copy
lst_l = ['1', '2', '3']
print(lst_l)
print(len(lst_l))
newLst = lst_l.copy()
print(newLst)
lst_2 = (1, 2, 3, 4)

# copy.copy()
# 深复制
# copy.deepcopy()
for i in lst_2:
    print(i)
