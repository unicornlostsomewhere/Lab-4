#Создать класс List (список), в котором
# реализовать методы для работы со списком (не менее 5).

class List:
    def __init__(self, fruit, potato, sleep):
        self.fruit = fruit
        self.potato = potato
        self.sleep = sleep
    def start(self):
        print("Начало программы.")

    def info(self):
        self.car = "Volvo"
        self._phone = "Samsung"
        self.__credit_card = "Mastercard"

    def add(self, fruit, potato, sleep):
        return fruit + potato + sleep

    def get_fruit(self, fruit):
        return fruit

line = List("абрикос", "бульба", "сон")
line.start()
print(line.add(line.fruit, line.potato, line.sleep))
print(line.get_fruit("абрикос"))


