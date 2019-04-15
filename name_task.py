# # name
# # print('what is your name?')
# name = input('What is your name?')
#
# # age
# print('Your name is' + name)
# age = input('What is your age?')
#
# # print(type(age))
# # print('your age is' + age)
#
# print('your name is' + name + 'and you are' + age + 'years old')
#
# # interpolation is using variables inside strings themselves
# # this can be done by simply putting the variable at any point of the 'string'
# # in (variable) brackets and the valaue will appear on the result. this i sinterpolation
#
# print('your name is' + name + 'and you are (age) years old')
# # notice the (age) variable is interpolated in brackets
#
# mothers_age = input("Also, what is your mothers age?")
#
# # turning a variable into a integer
# # this is called casting when you change an objects class
# # e.g.
# age_int = int(age)
# print(type(age_int))
# print(f'your name is {name} and you are {age} years old')

# # We can use pseudo code do granulate our code...

# # Asks user for name & saves in variable
# name = input("What is your name?")
# last_name = input("What is your last name?")
#
# # Ask users for age & save in variable and cast as integer
# age = int(input("What is your age?"))
#
# print(f'Your name is {name} and you are {age} years old')
#
# # Asks user for mothers & fathers age & cast as integer
# age_mother = int(input("What is your mothers age?"))
# age_father = int(input("What is your fathers age?"))
#
# # Save in variable and cast as integer
# print(f'Your mothers age is {age_mother}')
#
# # Calculate difference between age for mother and father
# age_diff_m = age_mother - age
# age_diff_f = age_father - age
#
# # prints user name and age difference between mother and father
# print(f'Your name is {name} and the difference in age between you and your mother is {age_diff_m} and father is {age_diff_f} years')

# # interpolation