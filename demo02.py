import string

import temp as temp


# def caesar(f, r):
#     lower = string.ascii_lowercase
#     upper = string.ascii_uppercase
#     before = string.ascii_letters
#     after = lower[r:] + lower[:r] + upper[r:] + upper[:r]
#     table = "".maketrans(before, after)
#     return f.translate(table)
#
#
# f = "Python is a great programming language."
# e = caesar(f, 3)
# print(e)

# chars = ['a', 'c', 'x', 'd', 'p', 'a', 'm', 'q', 's', 't', 'a', 'c']
# char1s = 'abcdefghigklmnopqrstuvwxyz'
# dict = {}
# for a in chars:
#     if dict.get(a) is None:
#         dict[a] = 1
#     else:
#         dict[a] = dict[a] + 1
# print(dict)
# for i, j in dict.items():
#     if j == temp:
#         print(i, '=', j)
#     else:
#         continue


# def dian(n):
#     import random
#     shu = 0
#     for i in range(1, n + 1):
#         s = random.randint(1, 6)
#         shu += s
#         print("五个筛子的点数和是：", shu)
#
#
# dian(5)

#
def palindrome(a):
    if len(a) < 2:
        return True
    if a[0] != a[-1]:
        return False
    return palindrome(a[1:-1])


b = input("请输入一个字符串：")
if palindrome(b):
    print("Ture，该字符串是回文字符串")
else:
    print("False，该字符串不是回文字符串")
