class Goods:
    price = 100

Goods.price = 200
setattr(Goods, 'size', 10)

print(Goods.__dict__['size'])
print(getattr(Goods, 'price', False)) # вернет False, если нет переменной в пространстве имен

g = Goods()

setattr(g, 'length', 15)

prop = (g.__dict__.keys())
print(*prop, sep=' ')

delattr(g, 'length')
print(*g.__dict__.keys())

print(hasattr(g, 'min'))