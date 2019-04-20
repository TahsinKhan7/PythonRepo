# Function format
# def func(para_1,Para_2...):
#       <para blocks>
#  call func(para or not)

#pass      #Use pass to just skip/not execute the function

# def hello_func():
#     pass
# hello_func()

#####Printing#####
# can print within block code or print the call statement itself.
# def hello_func():
#     print('Hello Function!')
# OR
# print(hello_func())
################

######## Calling the function to excute it multiple times###########
# def hello_func():
#  print('hello')
# hello_func()
# hello_func()
################


######## Using return to equate a result to a function and then printing the function call itself #########
# This allows use to equate the function to a specific result and
# carry it through and make more calculations using said function
# Using return equates a given result to the overall output of the function
# we can the print the call function itself to simply print the set overall functions return result

# def hello_func():
#  return 'Hello'
# print(hello_func())
################

###############
### E.g. of using return on a function and executing a print calculation respectively####:
### So, assigning a overal return result to a funciton and then
# pplying print and clculaitons to the funtion call itelf...

# def hello_func():
#  return 'Hello'
# print(hello_func().upper())
# print(len(hello_func().upper()))
# print(type(hello_func().upper()))

#################
#### Defining parameters/variables for our function#####

# def hello_func(greeting, name = 'you'):
#     return f'{greeting}, {name}. function.'
# print(hello_func('Hi'))
# print(hello_func('Hi', name='Tahsin'))
##################

