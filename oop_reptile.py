from oop_monkey import Animal

class Reptile(Animal):
    species = 'reptile'
    print('A monkey is sitting on a tree:')

    # Instance Attributes
    def __init__(self, action_1, action_2, action_3, banana_num, feature_1, feature_2, feature_3):
        super().__init__(feature_1, feature_2, feature_3)
        self.act_1 = action_1
        self.act_2 = action_2
        self.act_2 = action_3
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
monkey_actions = Monkey('Eat', 'Swings', 'Dance', 5, '', '', '')


# Calling instances/methods
print(f'Monkeys are {Monkey.species}s, and so their mammalian features are: {monkey_features.features()}')
monkey_actions.eat()
monkey_actions.swings()
monkey_actions.dance()

# Encapsulation Test
monkey_features.__f_1 = 'Scales'  # The feature result should still be 'Fur'

# Polymorphism Test
def poly_test(Animal):
    Animal.breathe_underwater()
