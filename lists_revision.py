cars = ['Volvo', 'Lambo', 'Skoda', 'Jaguar']
# General list formatpr some_list =[ [], [], [] ]
# can place [] after a lists name to target a specific object within a list
#we can further nest within this to further target values within the list
# so cars[2][0] will arget the S only in Skoda
print(cars[2])
# for car in cars:
#     print(car)


# So we can target values within lists using list[][]...
embeded_list = [['Tahsin'], ['Filipe'], ['Marat']]

print(embeded_list[0][0])


# To target multiple items for a list witin a list, we cna use a for loop
# We can target a list within a list by essentially nesting a for loop
# This lets us target values within values , within values

for data_list in embeded_list:
    #print(data_list)
    for data in data_list:
        print(data)
#e.g. this prints which bypasses the additional square brackets in the list
# Tahsin
# Filipe
# Marat