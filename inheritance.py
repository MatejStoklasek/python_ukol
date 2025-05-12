class Animal:
    def __init__(self, name, ):
        self.__name = name

    def get_name(self):
        # Zde může být další kód
        return self.__name

    def set_name(self, name):
        self.__name = name.upper()

    def speak(self):
        print("I am an animal")

class Cat(Animal):
    def speak(self):
        super().speak()
        print(f"Mnau: {self.get_name()}")



# Toto je kočka
animal = Cat("Žofka")
animal.speak()
animal.set_name("Žirafa")
print(animal.get_name()) # ŽIRAFA