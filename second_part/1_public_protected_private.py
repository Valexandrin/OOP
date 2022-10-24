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
