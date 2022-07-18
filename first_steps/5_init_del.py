from random import randint, choice

class Money:
    def __init__(self, amount):
        self.amount = amount

my_money = Money(100)
your_money = Money(1000)


class Point:
    def __init__(self, x, y, color='black'):
        self.x = x
        self.y = y
        self.color = color

points = []
x, y = 1, 1
for pt in range(1000):
    pt = Point(x, y)
    points.append(pt)
    x += 2
    y += 2

points[1].color = 'yellow'


class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)       

elements = []
for obj in range(217):
    obj = choice([Line, Rect, Ellipse])(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))    
    elements.append(obj)

for element in elements:
    if isinstance(element, Line):
        element.sp = (0, 0)
        element.ep = (0, 0)



class TriangleChecker:
    def __init__(self, a, b, c):
        self.sides = [a, b, c]               

    def is_triangle(self):
        not_int = [elem for elem in self.sides if not isinstance(elem, int)]
        if not_int:
            res = 1
        elif [elem for elem in self.sides if elem <= 0]:
            res = 1
        else:
            for side in self.sides:
                if sum(self.sides) - side <= side:
                    res = 2
                    break
                res = 3
        print(res)


tr = TriangleChecker(3,4,5)
tr.is_triangle()



class Graph:
    def __init__(self, data: list) -> None:
        self.data = data
        self.is_show = True

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show:
            return ' '.join(str(elem) for elem in self.data)
        print("Отображение данных закрыто")
    
    def show_graph(self):        
        res = self.show_table()
        if res:
            print("Графическое отображение данных: {}".format(res))        
    
    def show_bar(self):
        res = self.show_table()
        if res:
            print("Столбчатая диаграмма: {}".format(res))        

    def set_show(self, fl_show):
        self.is_show = fl_show
        

gr = Graph([1,2,3,-7])
gr.show_bar()
gr.set_show(fl_show=False)
gr.show_bar()


class CPU:
    def __init__(self, name, fr) -> None:
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume) -> None:
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, mem_slots) -> None:
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots

    def get_config(self):
        mem_slots = ['{} - {}'.format(slot.name, slot.volume) for slot in self.mem_slots]
        res = [
            'Материнская плата: {}'.format(self.name),
            'Центральный процессор: {}, {}'.format(self.cpu.name, self.cpu.fr),
            'Слотов памяти: {}'.format(self.total_mem_slots),
            'Память: {}'.format('; '.join(mem_slots)) 
        ]
        return res


cpu = CPU('наименование', 'тактовая частота')
mem1 = Memory('наименование1', 216)
mem2 = Memory('наименование2', 216)
mb = MotherBoard('наименование', cpu, [mem1, mem2])
mb.get_config()


class Cart:
    def __init__(self) -> None:
        self.goods = []
    
    def add(self, gd):
        self.goods.append(gd)
    
    def remove(self, indx):
        self.goods.pop(indx)
    
    def get_list(self):
        cart = ['{}: {}'.format(item.name, item.price) for item in self.goods]
        return cart
        
class Table:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class TV:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Notebook:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

class Cup:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

tv1 = TV('name', 300)
tv2 = TV('name', 400)
table = Table('name', 500)
notebook1 = Notebook('name', 300)
notebook2 = Notebook('name', 300)
cup = Cup('name', 30)

cart = Cart()
cart.add(tv1)
cart.add(tv2)
cart.add(table)
cart.add(notebook1)
cart.add(notebook2)
cart.add(cup)