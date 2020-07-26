class Human(object):
    def __init__(self, name):
        self.name = name
    
    def greeting(self):
        print(f"hello, my name is {self.name}.")

hasan = Human("hasan")
print(hasan.name)
hasan.greeting()