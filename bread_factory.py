def dough(water, wheat):
    #print(f'Mixing {water} with {wheat}')
    if water == 'water' and wheat == 'wheat':
        return 'dough'
    else:
        return 'blob of mixture'

#print(dough('water','wheat'))

output=dough('water', 'wheat')
print(output)
print(output == 'dough')
print(dough('water', 'wheat') == 'dough')


def bake(substance):
    # return 'bread'
    if substance == 'dough':
        return 'bread'
    else:
        return 'not bread...:('

print('testing with dough')
print(bake('dough') == 'bread')
print(bake('dough'))

print('testing with a brick')
print(bake('brick')=='not bread.. :(')
print(bake('brick'))

## TEST AND TDD
## for our bread factory
# we should put water and dough and get out bread
# if not we put something else, we should get not bread.. :('


def bread_factory(substance_1, substance_2):
    output_dough = dough(substance_1, substance_2)
    return bake(output_dough)


print('testing factory with water and wheat - expect output to be bread')
print(bread_factory('water', 'wheat') == 'bread')
print(bread_factory('water', 'wheat'))

print('testing factory with water and cement - expect output to be not bread')
print(bread_factory('water', 'wheat') == 'not bread...:(')
print(bread_factory('water', 'wheat'))