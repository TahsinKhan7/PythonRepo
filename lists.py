# # List
# # Lists keep information organised
# # Lists are defined by square brackets [ ]
#
# crazy_ppl=[]
# crazy_ppl=['Joana', 'luis', 'Ana li']
#
# #printing all of the list
# print(crazy_ppl)
# print(type(crazy_ppl))
#
# #Access one object inside the list
# # lists by the following index: [0, 1, 2, ...]
# print(crazy_ppl[1])
# print(type(crazy_ppl[1]))
# print(crazy_ppl[2])
# print(type(crazy_ppl[2]))
#
# # type displays the list class as 'list'

# i_want = ['banana', 'apple', 'orange', 5, 'kiwi', 'peach', 'grape', 'blueberries', 'strawberries', 'avocados']
# print(type(i_want))
#
# print(i_want[0])
# print(type(i_want[0]))
#
# print(i_want[9])
# print(type(i_want[9]))
#
# print(f'I like {i_want[0]}')

# # replace an object
# i_want[0] = "cherry"
# print(f'new list: {i_want}')
# print(i_want[0])
#
# # len
# want_len = len(i_want)
# print(f' length of list {want_len}')
#
# i_want += ["bread"]
# print(i_want)
# print(i_want[-1][0::2])
#
# want_len = len(i_want)
# print(f' length of list {want_len}')



# # #
# new example
crazy_ppl=[]
crazy_ppl=['Joana', 'luis', 'Ana li', 'Jon Snow', 'Arya']
# # printing all of the list
#
# print(crazy_ppl)
# print(type(crazy_ppl))
#
# # Access one object inside the list
# # lists by the following index: [0, 1, 2, ...]
# print(crazy_ppl[1])
# print(type(crazy_ppl[1]))
# print(crazy_ppl[2])
# print(type(crazy_ppl[2]))

# note we can use [-negative numbers] to count/index backwards according to a list

# add an item to a list
# use += ['item']
# another word for a list is 'array'
# another way to add a list value is use .append('')
# e.g.

print(len(crazy_ppl))

crazy_ppl.append('Daneareys Targarian')

print(len(crazy_ppl))

print(crazy_ppl[-1])

# we can use slice s[i:j] or s[i:j:k] to target specific characters of the object



#re assign an index with a new value
print(crazy_ppl)
crazy_ppl[0]=('Sansa')
print(crazy_ppl)

# insert to replace a specific index
print(crazy_ppl.insert(0, 'Tyrion'))
print(crazy_ppl)

# We can also use the following method to replace to a specific index on a list
crazy_ppl[:0]=["hello"]
print(crazy_ppl)

# Ranges/Slicing are defined with :
# Take an index and prints up to the index but not including the last item

# print(crazy_ppl[0:4])
# :0 print from 0 but not including 0
# [0:1] means zero up to but not including 1

# Using double ::  jumps objects. E.g.
# [0::2] means to jump through the list in steps of 2
# print(crazy_ppl[::3])

# removing a object from a list
# use .pop(index number)
crazy_ppl.pop()
print(crazy_ppl)

# or
crazy_ppl.pop(3)
print(crazy_ppl)

#  "Tuples"
#  Immutable list
# Tuples are lists which cannot be changed (without assigning/defining it to a new list)

essentials = ('bread', 'coffee', 'wifi')
# essentials[2] = ('laptop')
print(essentials)
print(essentials[1])

# print(crazy_ppl.count('Sansa Stark'))
# .count can be used to find a specific object in a list

