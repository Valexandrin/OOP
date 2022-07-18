class Point:
    min_val = 0
    max_val = 10


    @classmethod  # работает с атрибутами класса, но не экземпляра класса
    def validate(cls, arg):
        return cls.min_val <= arg <= cls.max_val


    def __init__(self, x, y) -> None:
        self.x = self.y = 0        
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
    

    def get_coords(self):
        return (self.x, self.y)


    @staticmethod  # работает с переданными при вызове значениями
    def multiply(x, y):
        return x*y + Point.max_val


p1 = Point(3, 40)
p2 = Point(1, 2)
# print(p1.get_coords())
# print(p2.get_coords())
print(Point.multiply(10, 2))
# print(p1.__dict__)
# print(dir(p1))
