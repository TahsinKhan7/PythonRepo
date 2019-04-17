# Control flow loops
# we can use "iterators: while and for
# While
# while <condition>:
#   <execute code if while is true>
# while True:
#     print('what yould you like to do?')
#     response=input('>')

#note, be careful of infinite loops may damage the device
# note, the response above stops the flow from going infinite

#counter car example
#note the order the counter is begin done

# car = ['farrari', 'Fiat Panda', 'fiat panda 4*4', 'Skoda Felicia Fun']
# counter = 0
# max_size_list = len(car)
# print('total number of cars:', max_size_list)
#
# while counter < max_size_list:
#     print(counter, '->', car[counter].capitalize())
#     counter += 1

# GoT_character = ['Jon Snow', 'Danearys Targaryen', 'Tyrion']
# GoT_house = ['Stark', 'Targaryen', 'Lannister']
# counter = 0
# print('GoT characters and corresponding houses:')
#
# while counter < len(GoT_character):
#     print(counter, '->', GoT_character[counter].capitalize(),'->', GoT_house[counter].capitalize())
#     counter += 1


# GoT_character = ['Jon Snow', 'Danearys Targaryen', 'Tyrion']
# GoT_house = ['Stark', 'Targaryen', 'Lannister']
# counter = 0
# print('GoT characters and corresponding houses:')
#
# while counter < len(GoT_character):
#     print(counter, '->', GoT_character[counter].capitalize(),'->', GoT_house[counter].capitalize())
#     counter += 1

#Break
#we can use break to forcefully stop a while loop specified
# keep asking user for input
# break if user types exit

while True:
    input_value= input('input anything')
    input_value.strip()
    if input_value == 'exit':
        break
    elif input_value== input_value.upper():
        print('do not capitalize')

