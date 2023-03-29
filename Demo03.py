class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.eat()
        self.sleep()

    def eat(self):
        print("姓名" + self.name + "年龄" + self.age + "在吃饭")

    def sleep(self):
        print("姓名" + self.name + "年龄" + self.age + "在睡觉")


class Student(Person):
    def __init__(self, name, age, code):
        Person.__init__(self, name, age)
        self.code = code
        self.study()

    def study(self):
        print("姓名" + self.name + "年龄" + self.age + "在学习")


class Leader(Student):
    def __init__(self, name, age, code, position):
        Student.__init__(self, name, age, code)
        self.position = position
        self.manage()

    def manage(self):
        print("姓名" + self.name + "管理学生学习")


class Teacher(Person):
    def __init__(self, name, age, position):
        Person.__init__(self, name, age)
        self.manage()
        self.teach()

    def manage(self):
        print("姓名" + self.name + "管理学生学习")

    def teach(self):
        print("姓名" + self.name + "教学")


if __name__ == '__main__':
    student = Student('胡俊杰', "22", "22010230832")
    leader = Leader("李四组长", "22", "22010230832", "学习委员")
    teacher = Teacher("老李", "22", "老师")
