# Iteration Task
print('List of movies:')
movie_list = ['Avengers', 'Matrix', 'Iron Man', 'Dark Knight', 'Spiderman']
counter = 0

for movie_id in movie_list:
    print(counter+1, '-', movie_id)
    counter += 1

print(' ')
print('List of places:')
places_list = ['UK', 'Spain', 'France', 'Germany', 'Russia']

counter = 0
for places_id in places_list:
    print(counter+1, '-', places_id)
    counter += 1

#########################################
#Dictionary of movies and places

# movies_places = {
#     'movies_list': ['Avengers', 'Matrix', 'Iron Man', 'Dark Knight', 'Spiderman'],
#     'places_list': ['UK', 'Spain', 'France', 'Germany', 'Russia']
# }

#####################################
# print('All movies and places:')
# counter = 0
# for mp_id in movies_places.values():
#      for m_p in mp_id:
#          print(m_p)


######################################
# # for just movies
# print('Movies:')
# for mp_id in movies_places['movies_list']:
#     print(mp_id)

# # for places
# print(' ')
# print('Places:')
# # for just places
# for mp_id in movies_places['places_list']:
#     print(mp_id)
#######################################

#Magic number
#A magic number is a number where the countinuous sum of resultant digits results in a value of 1.

# input_num = int(input('Enter a number, I will tell you if its a magic number!'))
#
# num_string = list(str(input_num))
# num_int = list(map(int, num_string))
#
# print(num_int)
# print(sum(num_int))
#
#
# while sum(num_int) != 1:
#     num_int=list(map(list(str(num_int))))
#     sum(num_int)







