import json

# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты
#   (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes sound")

    def eat(self):
        print(f"{self.name} is eating")


# 2. """Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`)."""
class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} is chirping")

    def fly(self):
        print(f"{self.name} is flying")


class Mammal(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} is meowing")

    def walk(self):
        print(f"{self.name} is walking")


class Reptile(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print(f"{self.name} is hissing")

    def crawl(self):
        print(f"{self.name} is crawling")


# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
#    которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

animals = [Bird("Parrot", 2, "blue"),
           Mammal("Cat", 5, "white"),
           Reptile("Snake", 3, "green")]


def make_animal_sound(animals):
    for animal in animals:
        animal.make_sound()


make_animal_sound(animals)


# 4. Используйте композицию для создания класса `Zoo`, который будет
#    содержать информацию о животных и сотрудниках. Должны быть методы
#    для добавления животных и сотрудников в зоопарк.

class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def remove_employee(self, employee):
        self.employees.remove(employee)

# 5. Создайте классы для сотрудников, например, `ZooKeeper`,
# `Veterinarian`, которые могут иметь специфические методы (например, `
# feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class ZooKeeper():
    def feed_animal(self, animal):
        animal.eat()


class Veterinarian():
    def heal_animal(self, animal):
        print(f"{animal.name} is being healed")


Parrot = Bird("Parrot", 2, "blue")
Cat = Mammal("Cat", 5, "white")
Snake = Reptile("Snake", 3, "green")
Krokodile = Reptile("Krokodile", 5, "green")

zoo = Zoo()
zoo.add_animal(Parrot)
zoo.add_animal(Cat)
zoo.add_animal(Snake)
zoo.add_animal(Krokodile)

zoo.add_employee(ZooKeeper())
zoo.add_employee(Veterinarian())

zoo.employees[0].feed_animal(Parrot)
zoo.employees[1].heal_animal(Cat)


# Добавить дополнительные функции в вашу программу, такие как
# сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

def save_zoo(zoo):
    animals = []
    for animal in zoo.animals:
        animals.append({
            "type": animal.__class__.__name__,
            "name": animal.name,
            "age": animal.age,
            "color": animal.color
        })

    with open("zoo.json", "w") as f:
        json.dump({
            "animals": animals
        }, f)

save_zoo(zoo)

def load_zoo():
    animal_classes = {
        "Bird": Bird,
        "Mammal": Mammal,
        "Reptile": Reptile
    }
    with open("zoo.json", "r") as f:
        data = json.load(f)
        animals = data["animals"]
        for animal in animals:
            animal["name"] = animal_classes[animal["type"]](animal["name"], animal["age"], animal["color"])
            zoo.add_animal(animal)
load_zoo()

