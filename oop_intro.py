# OOP

class Animal:
    # define how it looks (in terms of code) by initialising
    # create methods for this class

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print('INNNNNNN......anddddddd....outtttt')

    def eat(self):
        print('Nom NOM NOMMMMMMM...NOOMMM!!!')#

    def poty(self):
        print('... 0.0....')

cat = Animal()
#note classes must start with a capital
cat.breathe()
cat.eat()
cat.poty()


