"""
判断密码的长度
"""


def check_number(password):
    """
    判断是否含有数字
    """
    number = False
    for i in password:
        if i.isnumeric():
            number = True
            break
    return number


"""
判断密码是否有字母
"""


def check_letter(password):
    letter = False
    for i in password:
        if i.isalpha():
            letter = True
            break
    return letter


times = 5
while times > 0:
    password_str = input("请输入密码" + "\n")
    str_level = 0
    # 判断密码长度
    if len(password_str) >= 8:
        str_level += 1
    else:
        print("密码长度不满足，请输入八位密码")

    # 判断是否包含数字
    if check_number(password_str):
        str_level += 1
    else:
        print("密码应该有数字")

    # 判断是否包含字母
    if check_letter(password_str):
        str_level += 1
    else:
        print("密码应该有字母")

    if str_level == 3:
        print("密码合格，你的密码是" + password_str)
        break
    else:
        print("密码不合格")
        times -= 1
    print()

    if times == 0:
        print("你输入的密码次数超过了5次")
