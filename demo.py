from functools import reduce

number = int(input("请输入评委人数"+"\n"))
nameScore = {}
while number < 3:
    print('评委人数不能小于3')
    number = int(input('请再次输入评委人数（n>2）:'))
for i in range(number):
    name = input(f"请输入{i + 1}评委名字")
    score = int(input("请输入分数(0-100)"))
    nameScore[name] = score

print(nameScore)
max_score = max(nameScore.items(), key=lambda x: x[1])
min_score = min(nameScore.items(), key=lambda x: x[1])
print("最大值：" + str(max_score))
print("最小值：" + str(min_score))
nameScore.pop(max_score[0])
nameScore.pop(min_score[0])
print(nameScore)


list1 = list(nameScore.values())
average = reduce(lambda x, y: x + y, list1)
print("去掉最大值与最小值后平均分=" + str(average / len(list1)))
