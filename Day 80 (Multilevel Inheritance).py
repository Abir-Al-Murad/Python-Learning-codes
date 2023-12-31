class animal:
    def __init__(self,name,species):
        self.name = name
        self.sepecies = species
    def show_details(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.sepecies}")

class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="Dog") #Eikhane animal class er species er value diye disi but name declare kori nai
        self.breed = breed                       #Tai name sob class e likhte hoy
    def show_details(self):
        animal.show_details(self)
        print(f"Breed : {self.breed}")

class goldenretriever(dog):
    def __init__(self,name,colour): #upore name declare kori nai tai eikhane abr name dite hoice
        dog.__init__(self,name,breed="Golden Retriever") #class dog er breed eikhane diye disi but name dei nai.
        self.colour = colour
    def show_details(self):
        dog.show_details(self)
        print(f"Colour : {self.colour}")

o = dog("Kutta","black")
o.show_details()
f = goldenretriever("Tommy","White")
f.show_details() #eta 1st  e jabe class golde..pore dog pore animal and animal theke print kore dog print korbe and last
# e golden.... print korbe