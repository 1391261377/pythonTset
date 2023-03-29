# print('111')
# a = input("第一个数")
# b = input("第二个数")
# z = input("第二个数")
# q = input("第二个数")
# p = input("第二个数")
# y = input("第二个数")
#
#
# if a > b:
#     print("a>b")
# else:
#     print("b<a")
#
# e = input("第一个数")
# f = input("第二个数")
#
# if e > f:
#     print("a>b")
# else:
#     print("b<a")
import math


def demo(x, y, *args, **kwargs):
    return x, y, args, kwargs


result = demo(11, 22, 33, 44)

print(result[3])
result = filter(lambda x: x % 2, range(1, 10))

print(list(result))


class Person:

    def __init__(self, n="xxx"):
        self.name = n


class Student(Person):

    def __init__(self, n="aaa", s="male"):
        Person.__init__(self)

        self.sex = s

    def show(self):
        print(self.name, self.sex)


s = Student("yyy", "female")

s.show()

members = [{'name': '张三', 'age': 68}, {'name': '李四', 'age': 81}, {'name': '王五', 'age': 65}, {'name': '赵六', 'age': 68}]

result = sorted(members, key=lambda x: (x['age'], x['name']))

print(result)


class Auto:

    def __init__(self, color, weight, wheels):
        self.__color = color

        self.__weight = weight

        self.__wheels = wheels

    def change_color(self, new_color):
        self.__color = new_color


class Truck(Auto):

    def __init__(self, color, weight, capacity, wheels):
        super().__init__(color, weight, wheels)

        self.capacity = capacity


def carry(self):
    pass


print(math.pi)


class Pointer():

    def __init__(self, x, y):
        self.x = x

        self.y = y


class Circle():

    def __init__(self, cp, radius):

        self.cp = cp

        self.radius = radius

    def get_area(self):

        print('圆的面积为：', math.pi * self.radius ** 2)

    def get_circumference(self):

        print('圆的周长：', 2 * math.pi * self.radius)

    def point_circle(self, point):

        d = math.sqrt(pow((point.x - self.cp.x), 2) + pow((point.y - self.cp.y), 2))

        if d > self.radius:

            print('点在圆外')

        elif d < self.radius:

            print('点在圆内')

        else:

            print('点在圆上')


point = Pointer(3, 5)

cp = Pointer(2, 9)

circle = Circle(cp, 8)

circle.get_area()

circle.get_circumference()

circle.point_circle(point)


class Student:
    __school = "Chengdu NSU"

    def __init__(self, name, gender, student_id, major):
        self._name = name
        self._gender = gender
        self._student_id = student_id
        self._major = major

    @classmethod
    def get_school(cls):
        return cls.__school

    def change_major(self, new_major):
        self._major = new_major


class StudentCadre(Student):
    def __init__(self, name, gender, student_id, major, position):
        super().__init__(name, gender, student_id, major)
        self.position = position


def fun(a, b=23):
    print(b)
    print(a)


fun(1)
