# # For loops
# # for place_holder in list_object
# # excecute this block of code
# ids_list = ['fiat', 'Lambo', 'Russian car', 'potato']
#
# counter = 0
# for id in ids_list:
#     #print(ids_list)
#     print(counter+1, '-', id)
#     counter += 1

####### Example of a iterpolated for loop

embedded_data = [[1, 2, 3], [7, 12, 1]]
counter = 0
for data_list in embedded_data:

    for data in data_list:
        print(data)