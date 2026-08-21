class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello everyone!")

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


herm = Person("Herm", 20)
herm.greet()
herm.introduce()

denny = Person("Denny", 25)
denny.greet()
denny.introduce()
