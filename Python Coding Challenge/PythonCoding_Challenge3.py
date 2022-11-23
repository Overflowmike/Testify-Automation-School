
# Using the OOP features inheritance, create a class Animal with the method sound()
# and then create a cat and dog class that inherits from the animal class.
# the cat and dog class should override the sound class and print a different sound

class Animal:
    sound1 = "moo"
    sound2 = "baa"


    def print_animal_info(self):
        print("\nAnimal {", self.sound1, ",", self.sound2 + " }")


class Cat(Animal):
    sound = "meow"

    def _init_(self, sound1, sound2):
        self.sound1 = sound1
        self.sound2 = sound2


class Dog(Animal):
    sound = "woof"

    def _init_(self, sound1, sound2):
        self.sound1 = sound1
        self.sound2 = sound2


dog1 = Dog()
dog1.print_animal_info()

cat1 = Cat()
cat1.print_animal_info()