#### note you can just use GoT_char['name']= 'new value' ####
# print(students['student_3']['name])
# print(students['student_3']['completed modules'][0])
GoT_char ={
     'name':{...},
     'gender': {...},
     'house':{...}
}
# displaying whats in your dictionary
print(GoT_char.keys())  # prints all present keys
print(GoT_char.values()) # Prints all values


print('Create a GoT character')
user_input_name = input('What is your characters name?')
insert_name={'name': user_input_name }
GoT_char.update(insert_name)


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
