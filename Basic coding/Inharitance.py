class Pet:
    def __init__(self, name ,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")


class Cat(Pet):
    def speak(self):
        print("meow")
class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim",19)
p.show()

d=Dog("Dill",2)
d.speak()

c = Cat("Bill",34)
c.speak()
c.show()