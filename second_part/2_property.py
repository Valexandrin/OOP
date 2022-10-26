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
car.model = 'T'
print(car.model)

