class Animal:
    print('Welcome to the zoo!')

    #Instance Attributes
    def __init__(self):
        self.zoo = True

# Inheritance Mammal
class Mammal(Animal):
    def __init__(self):
        super().__init__()                  ## 'Super()' required for inheritance attributes
        self.__species = 'Monkey'
        self.__feature_1 = 'Fur'
        self.__feature_2 = 'Tail'
        self.__feature_3 = 'Females can produce milk'
        self.__food = 'bananas and other fruit'

    def species(self):
        print(f'{self.__species}s are an example of an mammal species.')

    def features(self):
        print(f'Their mammalian features are: {self.__feature_1} , {self.__feature_2} and {self.__feature_3}.')

    def eat(self):
        print(f'They eat {self.__food}.')

    def underwater(self):
        print('Monkeys can breathe underwater, but only for a very short period of time.')

# Inheritance Reptile
class Reptile(Animal):
    def __init__(self):
        super().__init__()                  ## 'Super()' required for inheritance attributes
        self.__species = 'Snake'
        self.__feature_1 = 'Scales'
        self.__feature_2 = 'Cold-blooded'
        self.__feature_3 = 'Heat-vision'

    def species(self):
        print('Snakes are an example of an reptile.')

    def features(self):
        print('Their reptilian features are: Scales, Cold-blood and heat-vision.')

    def eat(self):
        print('They eat a variety of animals from mice to birds.')

    def underwater(self):
        print('Snakes can breathe underwater for an extended period of time.')

# Inheritance Fish
class Fish(Animal):

    def __init__(self):
        super().__init__()                  ## 'Super()' required for inheritance attributes
        self.__species = 'Shark'
        self.__feature_1 = 'Scales'
        self.__feature_2 = 'Gills'
        self.__feature_3 = 'Fins'

    def species(self):
        print(f'A {self.__species} is an example of a fish')

    def features(self):
        print('Their main features are: Gills, Scales and Fins.')

    def eat(self):
        print('Sharks eat other fish')

    def underwater(self):
        print('Sharks (and many fishes) can breathe in underwater indefinitely due to their gills.')


#######
# General instantiating
# General Calling/Printing results

#######
## Encapsulation Test ##
monkey_features = Mammal()
monkey_features.features()
# Changing the 'Fur' feature to 'Scales'
monkey_features.__feature_1 = 'Scales'
monkey_features.features()
# The results of the features result should still be 'Fur' and not changed to 'Scales'
# as __feature_1 is encapsulated

## Polymorphism Test ##

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
