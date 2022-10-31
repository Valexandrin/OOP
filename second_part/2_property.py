#ex4
class Car:
    def __init__(self) -> None:
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        if isinstance(model, str) and len(model) in range(2,100):
            self.__model = model

car = Car()
car.model = 'Toyota'


#ex5
class WindowDlg:
    def __init__(self, title, width, height) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print("{title}: {width}, {height}".format(
            title = self.__title,
            width = self.__width,
            height = self.__height,
        ))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if isinstance(width, int) and width in range(0, 10001):
            self.__width = width
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if isinstance(height, int) and height in range(0, 10001):
            self.__height = height
            self.show()


wnd = WindowDlg('Диалог 1', 100, 50)


#ex6
class StackObj:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        if isinstance(next, StackObj):
            self.__next = next
        else:
            self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, str):
            self.__data = data


class Stack:
    def __init__(self, top: StackObj = None) -> None:
        self.top = top

    def push(self, obj):
        if not self.top:
            self.top = obj
        else:
            end = self.top
            while end.next:
                end = self.top.next
            end.next = obj

    def pop(self):
        end = self.top
        if not end:
            return None
        if not end.next:
            self.top = None
            return end
        while end.next and end.next.next:
            end = self.top.next
        res = end.next
        end.next = None
        return res


    def get_data(self):
        res = []
        end = self.top
        if not end:
            return res
        while end.next:
            res.append(end.data)
            end = self.top.next
        res.append(end.data)
        return res


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()


#ex7
class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __check_coord(cls, coord):
        if not type(coord) in (int, float):
            return False
        if cls.MIN_COORD <= coord <= cls.MAX_COORD:
            return True


    @staticmethod
    def norm2(vector):
        return vector.x**2 + vector.y**2

    def __init__(self, x, y) -> None:
        self.__x = self.__y = 0
        if self.__check_coord(x):
            self.__x = x
        if self.__check_coord(y):
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if self.__check_coord(x):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if self.__check_coord(y):
            self.__y = y


#ex8
class TreeObj:
    def __init__(self, indx: int, value=None) -> None:
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj

class DecisionTree:
    def __init__(self) -> None:
        pass

    @classmethod
    def predict(cls, root: TreeObj, x: list):
        while not root.value:
            if x[root.indx]:
                root = root.left
            else:
                root = root.right
        return root.value

    @classmethod
    def add_obj(cls, obj: TreeObj, node: TreeObj=None, left=True):
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj

root = DecisionTree.add_obj(TreeObj(0))
v_11 = DecisionTree.add_obj(TreeObj(1), root)
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]
res = DecisionTree.predict(root, x)

#ex9
from math import sqrt, pow
from typing import List

class LineTo:
    def __init__(self, x, y) -> None:
        if self.check_coord(x) and self.check_coord(y):
            self.x, self.y = x, y
            self.x0 = self.y0 = 0

    @staticmethod
    def check_coord(coord):
        return type(coord) in (int, float)

    @property
    def length(self):
        return sqrt(pow(self.x-self.x0, 2) + pow(self.y-self.y0, 2))

    @property
    def end(self):
        return self.x, self.y

    def set_start(self, *args):
        self.x0, self.y0 = args


class PathLines:
    def __init__(self, *args) -> None:
        self.path: List[LineTo] = []
        for i in args:
            self.add_line(i)

    def get_path(self):
        return self.path

    def get_length(self):
        return sum([i.length for i in self.path])

    def add_line(self, line: LineTo):
        if self.path:
            line.set_start(*self.path[-1].end)
        self.path.append(line)
