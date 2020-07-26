class Dog(object):
    def __init__(self, name, height, color, weight):
        self.name = name
        self.height = height
        self.color = color
        self.weight = weight
    
    def greating(self):
        print(f"hi dog name is {self.name}, dog color is {self.color}")

blacky = Dog("Blacky", "2ft", "black", "10kg")

blacky.greating()

class Dog1(Dog):
    pass

wolf = Dog1("wolf", "3ft", "white", "20kg")

wolf.greating()

class PetDog(Dog1):
    def __init__(self, owner, city):
        self.owner = owner
        self.city = city
    
    def allDetails(self):
        print(f"all details owner name {self.owner} dog name {self.name}")

petdetails = PetDog("Raki", "bengaluru")

petdetails.allDetails()
///

