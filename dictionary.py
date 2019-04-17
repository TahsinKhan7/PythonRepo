# dictionaries

#crazy = ['Snow', 'The North', 'Cerci', 'Kings Landing']

# dictionaries keep information with keys and values pairs
# In dictionaries you do not look up an index, rather a key.
# much like looking up a word in a dictionary

# key = reference to object
# value = what ever data is stored: could be a string , list, number even other dictionaries.

# Abstracting - Defines/creating a dictionary (also known as hash in ruby or object in JS)
# Creating a dictionary
# {'keys': 'value',
# 'keys2': 'value2',}...
# note is the value is a integer, you do not put single quotes ' '
# Also do not put a comma after the last value

# student_1 ={
#     # key   # values,
#     'name':'Arya',
#     'stream':'Dev-ops',
#     'grade': 5,
#     'completed modules': ['git', 'github', 'business week', 'variables', 'data types']
# }
# print(student_1)
# print(type(student_1))
#
# # it is dictionary <class 'dict'>
# # you cant treat this like a list
# # you must refer to the classes instead
#
# # # Accessing values of keys (retrieve a specific key)
#
# print(student_1['stream'])
#
# print(student_1['completed modules'])
#
# #retrieving from a list class/key and from within its list
# # simply put in square brackets the index you want to retrieve
#
# print(student_1['completed modules'][2])
#
# # changing a classes object
# student_1['name']='A girl has no name'
##############
# student_2 ={
#     # key   # values,
#     'name':'Jon Snow',
#     'stream':'Dev-ops',
#     'grade': 5,
#     'completed modules': ['git', 'github', 'business week', 'variables', 'data types']
# }
# # Adding to a class
# # student_2['completed modules'] += 'git'
#
# print(student_2['name'])
#
# # adding to a list
# student_2['completed modules'] += ['html']
# student_2['completed modules'] += ['agile']
# print(student_2['completed modules'])
#
# # note you can also do student_1['completed modules].append('html')
# # += is essentially an increment or 'add on' to an existing object
#
# print(student_2['completed modules'].count('git'))
#
# student_2['completed modules'].append('c#')
# # you can directly print the above by assining a vairable to it and do .append(variable)
# print(student_2['completed modules'])

# # update function
#
# d = {1: "one", 2: "three"}
# d1 = {2: "two"}
#
# # updates the value of key 2
# d.update(d1)
# print(d)
#
# d1 = {3: "three"}
#
# # adds element with key 3
# d.update(d1)
# print(d)
#
# #the below updates a class value in
# d1={3: "three"}
# print(d1)

GoT_char ={
#     # key   # values,
     'name':'name_placeholder ',
     'gender': 'gender_placeholder',
     'house':'house_placeholder',
}
print('Create a GoT character')
user_input_name = input('What is your characters name?')
insert_name={'name': user_input_name }
GoT_char.update(insert_name)
#### note you can just use GoT_char['name']= 'new value' ####

user_input_gender = input('What is your characters gender?')
insert_gender={'gender': user_input_gender }
GoT_char.update(insert_gender)

user_input_house = input('Which house are they a part of? (Pick houses Targaryen, Lannister, Arryn, Tully, Baratheon, Tyrell)').strip().lower().capitalize()

print(user_input_house)
houses = ['Targaryen', 'Lannister', 'Arryn', 'Tully', 'Baratheon', 'Tyrell']
print(user_input_house in houses)

if user_input_house in houses:
    insert_house={'house': user_input_house  }
    GoT_char.update(insert_house)
else: print('Please enter a correct house')

print('your characters name is:' + GoT_char['name'], ',', ' gender is' + GoT_char['gender'] + " " + 'and is from house' + GoT_char['house'])

