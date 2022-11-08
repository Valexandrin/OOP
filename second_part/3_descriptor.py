#ex6
class FloatValue:
    @classmethod
    def verify_value(cls, value):
        if type(value) != float:
            raise TypeError("Присваивать можно только вещественный тип данных.")

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_value(value)
        setattr(instance, self.name, value)

class Cell:
    value = FloatValue()

    def __init__(self, value=0.0) -> None:
        self.value = value


class TableSheet:
    def __init__(self, N, M) -> None:
        self.cells = [[Cell() for i in range(M)] for j in range(N)]

i = iter(range(15))
tabel = TableSheet(5, 3)
for row in tabel.cells:
    for cell in row:
        cell.value = float(next(i) + 1)
