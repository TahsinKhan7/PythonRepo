# # For loops
# # for place_holder in list_object
# # execute this block of code
# ids_list = ['fiat', 'Lambo', 'Russian car', 'potato']
#
# counter = 0
# for id in ids_list:
#     #print(ids_list)
#     print(counter+1, '-', id)
#     counter += 1

####### Example of a iterpolated for loop (embedded for loops) ######

# embedded_data = [[1, 2, 3], [7, 12, 1]]
# counter = 0
# for data_list in embedded_data:
#
#     for data in data_list:
#         print(data)



# Loops for dictionaries

accounts = {
    1:{"name": "Arya", "money": "£10000000"},
    2:{"name": "Bob Builder", "money": "£10000"},
    3:{"name": "Sponge", "money": "£500000"}
}
#
# # print(accounts.keys())      # checks values and keys
# # print(accounts.values())   #
#
# # for acc in accounts:
# #     print(acc)
# #     print(type(acc))
# #     #this will display the first couple of keys
# # this will display the first couple of key via []
#
#two ways to do for loops with dictionaries to display intrinsic keys and values
#method 1 using [ ]  brackets for accessing nested keys/values in a dictionary
for key in accounts:
    for embedded_key in accounts[key]:
        print(accounts[key][embedded_key])


#method 2
for acc_dictionaries in accounts.values():
     #print(account_dictionaries)

    for embedded_val in acc_dictionaries.values():
        print(embedded_val)
        # this will display the first couple of values via .value or .key


# list_data = [1, 2, 3, 4, 5]
#
# # list_data=int(input("tell me the number i'm thinking about").strip())
#
# for num in list_data:
#         if num == 3:
#             print('OMG I FOUND NUMBER 3')
#         elif num > 3:
#             print('too far! past 3')
#         else:
#             print('too soon')