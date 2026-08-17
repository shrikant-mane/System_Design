from abc import ABC, abstractmethod

class CoffeeComponent(ABC):
    @abstractmethod
    def cost(self):
        pass


class Cofee(CoffeeComponent):
    def cost(self):
        return 100

class CoffeeDecorator(CoffeeComponent):
    def __init__(self, coffee):
        self.coffee = coffee

class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 30

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 20

class WhippedCreamDecorator(CoffeeDecorator):
    def cost(self):
        return self.coffee.cost() + 40


coffee = Cofee()
coffee = MilkDecorator(coffee)
print(coffee.cost())

coffee = SugarDecorator(coffee)
print(coffee.cost())

coffee = WhippedCreamDecorator(coffee)
print(coffee.cost())




