class Figure:
    def __init__(self, a, b, c, d): # конструктор класса
        self.sp = (a, b)
        self.ep = (c, d)

    def __str__(self) -> str: # описание класса
        print(f'Figure: start point - {self.sp}, end point - {self.ep}')
    
    def __repr__(self) -> str: # метод, с помощью вывода которого можно создать экземпляр
        print('Figure({a}, {b}, {c}, {d})'.format(
            a = self.sp[0],
            b = self.sp[1],
            c = self.ep[0],
            d = self.ep[1],
        ))

print(Figure.__dict__) # коллекция параметров объекта
print(dir(Figure)) # список доступных методов

f = Figure(1, 2, 10, 20)
print(f.__dict__)

f.__str__()
f.__repr__()

