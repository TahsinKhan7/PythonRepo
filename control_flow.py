# Control Flow
# Controlling where code runs and does not
# depending on our code making evaluations that return true or false.

# using if statments
# Adgenda
## if
## else if -elif
## else
## switch or case
## If condition format below...

age = int(input("What is your age?"))
driver_1 = input("Do you have a licence?")

if age > 18:
    print('sorry, you cannot drink, but may be able to drive depending on where you live')

elif age < 18 and driver_1 == True:     # make sure to put :
    print('you can drive but not drink')

else:
    print('sorry you cannot drive')