#dog_weight = 50
#dog_name = "Vlčák"

class Dog: #Přepis objektu
    # name = "Vlčák"
    # weight = 50

    def __init__(self): #print self odkazuje na třídu Dog /
        self.name = "Vlčák"
        self.weight = 25


#print(f"Jméno: {dog_name} a váha: {dog_weight}kg")

dog = Dog() # vždy první proměná malým. 2. Objekt každé slovo velkým / Istance třidy = objekt / v ojektu má vlastnosti
print(f"Jméno: {dog.name} a váha: {dog.weight}kg")