class Person:
    pass


person_1 = Person()
person_1.age = 22
person_1.name = "Reza"


class Game:
    def __init__(self):
        self.money = None

    def set_money(self, money):
        self.money = money

    def get_money(self):
        return self.money


game = Game()
game.set_money(2000)
print(game.get_money())


class SuperMarket:
    def __init__(self, product, price):
        self.Product = product
        self.Price = price


HayatMarket = SuperMarket("Milk", 22000)

print("\nStatic Method Sample Code")
print()

class Sample:
    goal_money = 3000

    @staticmethod
    def increase_goal_money(value):
        Sample.goal_money += value


sample = Sample()
print(Sample.goal_money)
Sample.increase_goal_money(100000)
print(Sample.goal_money)
