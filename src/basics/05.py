class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.message = f"hello {self.name} from {self.city}!!!"

    def greet(self):
        print(self.message)

def main():
    name = input("provide your name: ")
    city = input("provide your city: ")
    person = Person(name, city)
    person.greet()

main()
