class AbstractClass:
    def __new__(cls, *args, **kwargs):
        return f'Ошибка: нельзя создавать объекты абстрактного класса'

obj = AbstractClass()
print(obj)


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
