class ListObject:
    def __init__(self, data, next_obj=None):        
        self.data = data
        self.next_obj = next_obj
    
    def link(self, obj):
        self.next_obj = obj

lst_in = [
    '1. Первые шаги в ООП',
    '1.1 Как правильно проходить этот курс',
    '1.2 Концепция ООП простыми словами',
    '1.3 Классы и объекты. Атрибуты классов и объектов',
    '1.4 Методы классов. Параметр self',
    '1.5 Инициализатор init и финализатор del',
    '1.6 Магический метод new. Пример паттерна Singleton',
    '1.7 Методы класса (classmethod) и статические методы (staticmethod)',
]

head_obj = ListObject(lst_in[0])
curr_obj = head_obj
for item in lst_in[1:]:
    next_obj = ListObject(item)
    curr_obj.link(next_obj)
    curr_obj = next_obj

while head_obj.next_obj:
    data = head_obj.data
    print(data)
    head_obj = head_obj.next_obj
print(head_obj.data)