class Animal:
    print('Welcome to my zoo!')

    #Instance Attributes
    def __init__(self):                 # Initializer
        self.alive = True
        self.eyes = True
        self.breathe = True
        self.move = True

# Inheritance Mammal
class Mammal(Animal):
    def __init__(self):
        super().__init__()                  ## 'Super()' required for inheritance attributes
        self.__species = 'Monkey'
        self.__feature_1 = 'Fur'
        self.__feature_2 = 'Tail'
        self.__feature_3 = 'Females can produce milk'
        self.__food = 'peanuts, bananas and other fruit'

    def mam_species(self):
        print(f'{self.__species}s are an example a mammal.')

    def mam_features(self):
        print(f'Some of their mammalian features are: {self.__feature_1}, {self.__feature_2} and {self.__feature_3}.')

    def mam_eat(self):
        print(f'The {self.__species} eats {self.__food}.')

    def underwater(self):
        print(f'{self.__species}s can stay underwater, but only for a certain period of time.')

# Inheritance Reptile
class Reptile(Animal):
    def __init__(self):
        super().__init__()                  ## 'Super()' required for inheritance attributes
        self.__species = 'Snake'
        self.__feature_1 = 'Scales'
        self.__feature_2 = 'Cold-blooded'
        self.__feature_3 = 'Heat-vision'
        self.__food = 'A variety of animals e.g. Mice'

    def rep_species(self):
        print(f'{self.__species} are an example of an reptile.')

    def rep_features(self):
        print(f'Some of their reptilian features are: {self.__feature_1}, {self.__feature_2} and {self.__feature_3}.')

    def rep_eat(self):
        print(f'The {self.__species} eats {self.__food}.')

    def underwater(self):
        print(f'{self.__species}s can breathe underwater for an extended period of time.')

# Inheritance Fish
class Fish(Animal):

    def __init__(self):
        super().__init__()                  ## 'Super()' required for inheritance attributes
        self.__species = 'Shark'
        self.__feature_1 = 'Scales'
        self.__feature_2 = 'Gills'
        self.__feature_3 = 'Fins'
        self.__food = 'other fish'

    def fish_species(self):
        print(f'A {self.__species} is an example of a fish.')

    def fish_features(self):
        print(f'Some of their main features are: {self.__feature_1}, {self.__feature_2} and {self.__feature_3}.')

    def fish_eat(self):
        print(f'The {self.__species} eats {self.__food}')

    def underwater(self):
        print(f'{self.__species}s can breathe underwater indefinitely due to their gills.')


########
# Mammal instantiating
print('Mammal at my zoo:')
mammal_meth = Mammal()

# Mammal Calling/Printing methods/results
mammal_meth.mam_species()   #Note to self: do call method/function instead of using print (otherwise output is 'None')
mammal_meth.mam_features()
mammal_meth.mam_eat()

########

## Encapsulation Test ##
print(' ')
print('Encapsulation Test (trying to change "Fur" to "Scales" for monkey):')
monkey_features = Mammal()
monkey_features.mam_features()
# Changing the 'Fur' feature to 'Scales'
monkey_features.__feature_1 = 'Scales'
monkey_features.mam_features()
# The results of the features result should still be 'Fur' and not changed to 'Scales'
# as __feature_1 is encapsulated


########
## Polymorphism Test ##
print(' ')
print('Polymorphism Test:')
# Creating a common interface
def poly_test(Animal):
    Animal.underwater()

# Instantiating the objects
under_monk = Mammal()
under_snake = Reptile()
under_fish = Fish()

# Passing the objects to show polymorphism of the 'underwater' method
poly_test(under_monk)
poly_test(under_snake)
poly_test(under_fish)