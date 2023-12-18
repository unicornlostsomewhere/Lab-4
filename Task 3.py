#Создать классы «Зоомагазин», «Животное», «Рыбы», «Птицы».
# Определить свойства: породу и стоимость для указанных
# животных (рыб, птиц), в каждом классе реализовать
# переопределение метода «способ передвижения».
# Вывести данные о самой дорогой породе. Предусмотреть
# метод записи информации в файл.

class ZooShop:
    def __init__(self):
        self.animals = []
    def add_animal(self, animal):
        self.animals.append(animal)
    def get_most_expensive(self):
        if self.animals:
            most_expensive = max(self.animals, key=lambda animal: animal.price)
            return most_expensive
        else:
            return None
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for animal in self.animals:
                file.write(animal.species + ": " + animal.breed + " - $" + str(animal.price) + "\n")
class Animal:
    def __init__(self, species, breed, price):
        self.species = species
        self.breed = breed
        self.price = price
    def move(self):
        return "Передвигается стандартно как животное."
class Fish(Animal):
    def move(self):
        return "Плавает."
class Bird(Animal):
    def move(self):
        return "Летает крыльями."

zoo = ZooShop()

fish1 = Fish("Fish", "Goldfish", 15)
fish2 = Fish("Fish", "Clownfish", 20)
bird1 = Bird("Bird", "Parrot", 50)

zoo.add_animal(fish1)
zoo.add_animal(fish2)
zoo.add_animal(bird1)

most_expensive_animal = zoo.get_most_expensive()
if most_expensive_animal:
    print("Самая дорогая порода", most_expensive_animal.breed, "которая стоит", most_expensive_animal.breed)

zoo.save_to_file("animals.txt")