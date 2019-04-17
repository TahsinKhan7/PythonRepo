# check for
## universal -> everyone can watch
## pg, general viewing, some scences may not.
## 12. films classified 12A and video works classified 12 contains material that is not general
## 15, No one  younger than 15 may see a 15 film in the cinema
## 18, no one younger than 18 may see an 18 film in a cinema

print('welcome to CineWorld!)')

movie = input('What is the movie rating?')

if movie == 'pg':
    print('You may watch this movie with a parent/gaurdian')
elif movie == '12':
    print('You can only watch this movie if you are 12 and over')
elif movie == '15':
    print('You can only watch this movie if you are 15 and over')
elif movie == '18':
    print('You can only watch this movie if you are 18 and over')
else: print('please enter a correct rating')

#########################################
age = input('What is your age?')

if age < 12:
    print('You may watch pg only movies and may require a parent/gaurdian')
elif age >= '12':
    print('You can watch this movie if you are 12 or over')
elif age >= '15':
    print('You can watch this movie if you are 15 and over')
elif movie >= '18':
    print('You can watch this movie if you are 18 and over')
else: print('please enter a correct age')