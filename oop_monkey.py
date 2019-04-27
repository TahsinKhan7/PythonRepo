class Animal:
    # Instance Attributes
    def __init__(self, feature_1, feature_2, feature_3):
        self.__f_1 = feature_1
        self.__f_2 = feature_2
        self.__f_3 = feature_3

    # Instance Methods
    def features(self):
        return f'{self.__f_1}, {self.__f_2}, {self.__f_3}.'

# Inheritance 'child' of Animal class:
class Mammal(Animal):
# Instance Attributes
    def __init__(self, eat, swings, dance, banana_num, feature_1, feature_2, feature_3):
        super().__init__(feature_1, feature_2, feature_3)
        self.__species = 'Monkey'
        self.act_1 = eat
        self.act_2 = swings
        self.act_2 = dance
        self.ban_x = banana_num

    # Instance Methods
    def eat(self):
        print(f'The monkey finds a cluster of bananas on the tree and proceeds to eat {self.ban_x} of them.')

    def swings(self):
        print('The monkey jumps onto a vine and swings to another tree.')

    def dance(self):
        print('The monkey starts dancing.')

    # Polymorphism example (method included in other animals)

    def breathe_underwater(self):
        print('Monkeys can breathe underwater but only for a very short period of time')


# Instantiating
monkey_features = Animal('Fur', 'Tail', 'Females produce milk')
monkey_actions = Mammal('Eat', 'Swings', 'Dance', 5, '', '', '')


# Calling instances/methods
#print(f'Monkeys are {Monkey.species}s, and so their mammalian features are: {monkey_features.features()}')
monkey_actions.eat()
monkey_actions.swings()
monkey_actions.dance()

# Encapsulation Test
monkey_features.__f_1 = 'Scales'  # The feature result should still be 'Fur'


def poly_test(Animal):
    Animal.breathe_underwater()

