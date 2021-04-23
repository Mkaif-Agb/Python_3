import chalk



class Enemy:
    life = 3

    def attack(self):
        print("ouch!")
        self.life -= 1

    def checklife(self):
        if self.life <= 0:
            print("I am dead")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()


class Dog:
    species = "Mammal"
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self, number):
        print("Woooffff My Name is {} and the number is {}".format(self.name, number))


my_dog = Dog(breed="Lab", name="Tom", spots=False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)
print(my_dog.species)
print(my_dog.bark(6))


class Circle:
    def __init__(self,radius='1'):
        self.radius =radius


    def area(self):
        return self.radius*3.14*self.radius


my_circle= Circle(30)

print(my_circle.radius)
print(my_circle.area())

class Animal:
    def __init__(self):
        print("Animal Created")

    def who(self):
        print("I am an ANIMAL")

    def eat(self):
        print("I am Eating")


myanimal = Animal()
print(myanimal)
print(myanimal.eat())
print(myanimal.who())

class Doge(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("DOG CREATED")

mydoge = Doge()

print(mydoge.who())


class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,value):
        self.balance = self.balance + value
        print(chalk.green("The Amount {} is added to ur Account".format(value)))

    def withdrawal(self,withdrawal):
        if self.balance >= withdrawal:
            self.balance = self.balance - withdrawal
            print(chalk.green("Transaction Accepted"))
        else:
            print(chalk.red("INSUFFICIENT FUNDS"))

    def __str__(self):
        return chalk.blue(f"Owner: {self.owner}\nBalance: {self.balance}")

acc = Account("Kaif",1000)
acc.withdrawal(500)
acc.deposit(100)
print(acc)
acc.withdrawal(1100)
acc.withdrawal(100)
print(acc)
