#dog_weight = 50
#dog_name = "Vlčák"

class Dog: #Přepis objektu
    # name = "Vlčák"
    # weight = 50

    def __init__(self, name, vaha, legs): #print self odkazuje na třídu Dog / metoda = uvnitř objektu
        self.name = name
        self.weight = vaha
        self.legs = legs

    def say_hello(self):
        print(f"Ahoj, já jsem {self.name} a mám {self.weight}kg. a mám {self.legs}")


#print(f"Jméno: {dog_name} a váha: {dog_weight}kg")

dog = Dog("Alík", 1, 4) # vždy první proměná malým. 2. Objekt každé slovo velkým / Istance třidy = objekt / v ojektu má vlastnosti
dog2 = Dog("Hafík", 4, 3)
dog3 = Dog("Hafan", 8,0)

dog.say_hello()
dog2.say_hello()
dog3.say_hello()

# print(f"Jméno: {dog.name} a váha: {dog.weight}kg")
# rint(f"Jméno: {dog2.name} a váha: {dog2.weight}kg")