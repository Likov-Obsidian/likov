class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print("Животное издает звук")
class Dog(Animal):
    def make_sound(self):
        print("Гав")
class Cat(Animal):
    def make_sound(self):
        print("Мяу")
def animal_chorus(animals):
    for animal in animals:
        animal.make_sound()
animals = [Dog("Sharik"), Cat("Matroskin")]
animal_chorus(animals)