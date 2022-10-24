# ex3
class Clock:
    def __init__(self) -> None:
        self.__time: int = 0

    def __check_time(cls, tm):
        if isinstance(tm, int) and 0 <= tm < 100000:
            return True
        return False

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time


#ex4
class Money:
    def __init__(self, money: int = None) -> None:
        if self.__check_money(money):
            self.__money = money

    def __check_money(cls, value):
        if isinstance(value, int) and value >= 0:
            return True
        return False

    def set_money(self, money):
        if self.__check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, obj):
        if self.__check_money(obj.__money):
            self.__money += obj.__money


#ex6
class Book:
    def __init__(self, author, title, price) -> None:
        self.__author = author
        self.__title = title
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price


#ex7
class Line:
    def __init__(self, *args) -> None:
        self.__x1, self.__y1, self.__x2, self.__y2 = args

    def set_coords(self, *args):
        self.__x1, self.__y1, self.__x2, self.__y2 = args

    def get_coords(self):
        return self.__x1, self.__y1, self.__x2, self.__y2

    def draw(self):
        print(*self.get_coords())


#ex8
class Point:
    def __init__(self, x, y):
        if self.__check_coords(x) and self.__check_coords(y):
            self.__x = x
            self.__y = y

    def __check_coords(cls, val):
        if isinstance(val, (int, float)):
            return True
        return False

    def get_coords(self) -> tuple:
        return self.__x, self.__y



class Rectangle:
    def __init__(self, *args) -> None:
        if len(args) == 4:
            x1, y1, x2, y2 = args
            self.__sp = Point(x1, y1)
            self.__ep = Point(x2, y2)
        else:
            self.__sp = args[0]
            self.__ep = args[1]


    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print("Прямоугольник с координатами: {coords} ".format(
            coords = self.get_coords(),
        ))

rect = Rectangle(0, 0, 20, 34)
