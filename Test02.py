# i = 1
# while i <= 9:
#     j = 1
#     while(j <= i):    # j的大小是由i来控制的
#         print(f'{i}*{j}={i*j}', end='\t')
#         j += 1
#     print('')
#     i += 1
#


# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f'{j}x{i}={i*j}\t', end='')
#     print()


# names = ['zhao', 'qian', 'sun', 'li']
# username = input("请输入一个姓：")
# if username in names:
#     print("用户该姓已存在")
# else:
#     names.append(username)
#     print("添加成功")
#     print(names)
# n = int(input("请输入行数："))
# i_list = [1]
# str_list = []
# for i in range(1, n + 1):
#     if i == 1:
#         str_list.append(' '.join(str(a) for a in i_list))
#     else:
#         ii_list = [1]
#         for j in range(1, i - 1):
#             ii_list.append(i_list[j - 1] + i_list[j])
#         ii_list.append(1)
#         i_list = ii_list
#         str_list.append(' '.join(str(a) for a in i_list))
# # 居中打印杨辉三角形
# for j in range(n):
#     print(str_list[j].center(len(str_list[n-1])))
# students = [
#     {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': '男'},
#     {'name': '李四', 'age': 28, 'score': 95, 'tel': '1388888666', 'gender': '女'},
#     {'name': '王五', 'age': 21, 'score': 98, 'tel': '1388888999', 'gender': '不明'},
#     {'name': 'chris', 'age': 17, 'score': 58, 'tel': '1388888923', 'gender': '男'},
#     {'name': 'jack', 'age': 23, 'score': 52, 'tel': '1388888928', 'gender': '女'},
#     {'name': 'tony', 'age': 15, 'score': 89, 'tel': '1388888988', 'gender': '不明'},
# ]
# # 统计不及格学生个数
# num = 0
# for i in students:
#     if i['score'] < 60:
#         num += 1
# print('不及格的学生有', num, '个')
# # 打印不及格学生姓名和对应成绩
# for j in students:
#     if j['score'] < 60:
#         print(j["name"], '的成绩为', j["score"])
# # 统计未成年学生个数
# sum = 0
# for x in students:
#     if x['age'] < 18:
#         sum += 1
# print('未成年学生有', sum, '个')
# # 打印手机尾号是8的学生名字
# for g in students:
#     if g['tel'][-1] == '8':
#         print('手机尾号为8的学生是', g["name"])
# #  打印最高分和对应的学生的名字
# max_score = students[0]['score']
# for stu in students:
#     if stu['score'] > max_score:
#         score = stu['score']
# print("最高分是：", max_score)
# for stu in students:
#     if stu['score'] == max_score:
#         print("最高分学生的名字是：", stu['name'])
# # 删除性别不明的所有学生
# for x in students:
#     if x['gender'] == '不明':
#         students.remove(x)
# print("性别不明的学生已删除")
#
#
# # 将列表按学生成绩从大到小排序
# def pai(ele):
#     return ele['score']
#
#
# students.sort(reverse=True, key=pai)
# for stu in students:
#     print(stu)
# n = 0
# while True:
#     sum = 0.08 * (2**n)
#     if sum >= 8848130:
#         break
#     n += 1
# print('需要折叠', n, '次')
# for a in range(1,100//3 + 1):
#     for b in range(1,100//2):
#         c = 100 - (a + b)
#         if a + b + c == 100 and 3*a + 2*b + c/2 == 100:
#             print(f'大马{a}匹，中马{b}匹，小马{c}匹。')


# number = input("请输入一个整数:")
# number = len(str(int(number)))
# print("输入整数的位数为%d" % number)


a = {'周', '杨', '胡', '薛'}
b = {'胡', '李', '张', '王', '周'}
c = {'胡', '李', '王', '薛'}
total = []
for x in a:
    if x not in total:
        total.append(x)
for y in c:
    if y not in total:
        total.append(y)
for z in b:
    if z not in total:
        total.append(z)
print("共有", len(total), "名学生选课")
# 2. 求只选了第一个学科的人的数量和对应的名字
only_a = []
for x in a:
    if x not in b and x not in c:
        only_a.append(x)
print("只选了第一门学科的有：", len(only_a), "人，分别是：", only_a)
# 3. 求只选了一门学科的学生数量和对应的名字
only_one = []
for x in a:
    if x not in b and x not in c:
        only_one.append(x)
for x in c:
    if x not in a and x not in b:
        only_one.append(x)
for x in b:
    if x not in a and x not in c:
        only_one.append(x)
print("只选了一门学科的有：", len(only_one), "人,分别是：", only_one)
# 4. 求只选了两门学科的学生数量和对应的名字
only_two = []
for x in a:
    if x in b and x not in c:
        only_two.append(x)
    elif x in c and x not in b:
        only_two.append(x)
for x in b:
    if x in c and x not in a:
        only_two.append(x)
print("只选了两门学科的有", len(only_two), "人，分别是：", only_two)
# 5. 求只选了三门学科的学生数量和对应的名字
all = []
for x in a:
    if x in b and x in c:
        all.append(x)
print("选了三门学科的有", len(all), "人，分别是：", all)
