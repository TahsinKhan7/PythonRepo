
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return f'{self.first} {self.last}'

emp_1 = Employee('Tahsin', '', '')
emp_2 = Employee('Test', 'User', 60000)

print(emp_1)
print(emp_2)
print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())
print(Employee.fullname(emp_1))
print(emp_2.fullname())


##############
# emp_1.first = 'Tahsin'
# emp_1.last = 'Khan'
# emp_1.email = 'tahsin_k@live.co.uk'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'test_k@live.co.uk'
# emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)
###########################



# class Animal:
#     def __init__(self, feature_1, feature_2, feature_3):
#         self.__f_1 = feature_1
#         self.__f_2 = feature_2
#         self.__f_3 = feature_3
#
#     def features(self):
#         return f'{self.__f_1}, {self.__f_2}, {self.__f_3}.'
#
# class Monkey(Animal):
#     species= 'mammal'
#     print('A monkey is sitting on a tree:')
#
#
#     def __init__(self, action_1, action_2, action_3,banana_amount, feature_1, feature_2, feature_3):
#         super().__init__(feature_1, feature_2, feature_3)
#         self.act_1 = action_1
#         self.act_2 = action_2
#         self.act_2 = action_3
#         self.ban_x = banana_amount
#
#     def eat(self):
#         return 'The monkey finds a cluster of bananas on the tree, opens one and begins to eat it.'
#
#     def swings(self):
#         return 'The monkey jumps onto a vine and swings to another tree.'
#
#     def dance(self):
#         return 'The monkey starts dancing.'
#
#
# monkey_features = Animal('Tail', 'Fur', 'Females produce milk')
# monkey_actions = Monkey(eat, 'Swings', 'Dance', '', '', '')
#
# #print(Animal.features(monkey_features))
# print(f'Monkeys are {Monkey.species}s, and so their mammalian features are: {monkey_features.features()}')
# print(monkey_actions.eat())
# print(monkey_actions.swings())
# print(monkey_actions.dance())
#
# feature_change = Animal()
# feature_change.features
# feature_change.__f_1='Scales'