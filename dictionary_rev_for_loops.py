#Dictionary within a dictionary:
# of the format
# = {key:values>>{key:value, key:value...}
library_accounts = {1:{'name':'Richard','books': 3},
                   2:{'name':'Joana', 'books': 30},
                   3:{'name':'Brand', 'books': 31}
                   }
# We cna display our initial keys using .key() after the dictionary
#print(library_accounts.keys())

#we can use .values() to display all of the initial dictionaries values in the given dictionary
#print(library_accounts.values())

# #We can nest display out internal keys simply by placing dictionary[internal key]
# # note here it is a [key] not an [index]
# print(library_accounts[2])
#
# # We can further nest to target specific values
# # we target keys to retrun its corresponding vlaues
# print(library_accounts[3]['name'])
# print(library_accounts[3]['books'])
#
# #
# # to return multiple again, you must use a for statement (the following statement does not work
# # print(library_returns[3]['name','books'])
#
# # so for lists you use [specific index], to return two specific idexes, use a for loop.
# # to access a dictionaries specific values, use dic[key] or a for loop for multipile keys
# #  returning values of multiple keys
#
# for objt in library_accounts:
#     #print(objt)

#we can further place either .values() further disply the values within the values of a secondary nested dictionary
for objt in library_accounts.values():
        #print(objt.keys())
        #print(objt.values())
        #print(objt)

        for value in objt.values():
            print(value)

# for specific keys???
# for objt in library_accounts.values():
#     #print(objt.keys())
#     for keyz in objt:
#           print(keyz.keys())
