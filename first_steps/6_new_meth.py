# ex_6
class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return f'Ошибка: нельзя создавать объекты абстрактного класса'

obj = AbstractClass()
print(obj)


# ex_7
class SingletonFive:
    number = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.number < 5:
            cls.__instance = super().__new__(cls) # вызываем метод класса-родителя
            cls.number += 1

        return cls.__instance


    def __init__(self, name) -> None:
        self.name = name

# ex_8
TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            instance = super().__new__(DialogWindows)
        else:
            instance = super().__new__(DialogLinux)

        setattr(instance, 'name', *args)
        return instance

TYPE_OS = 1
dlg_1 = Dialog("123")
TYPE_OS = 2
dlg_2 = Dialog("1234")

assert dlg_1.name == "123", "неверное значение локального атрибута name класса DialogWindows"
assert dlg_2.name == "1234", "неверное значение локального атрибута name класса DialogLinux"


# ex_9
class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def clone(self):
        return Point(self.x, self.y)

pt = Point(1, 2)
pt_clone = pt.clone()


# ex_10
class Factory:
    def build_sequence(self):
        return list()

    def build_number(self, string):
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq

ld = Loader()
s = input()
res = ld.parse_format(s, Factory())
