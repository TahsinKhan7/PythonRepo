#Fizzbuzz task

print('Fizzbuzz considers a range of numbers and returns "fizz" if a number inside the range is divisible by 3, buzz if divisible by 5, fizzbuzz if dvisible by 3 and 5')
input_1 = int(input('pick a number for the starting value of the range'))
input_2 = int(input('pick another number for the ending value for the range'))

for current_value in range(input_1, input_2):
    if current_value % 3 == 0 and current_value % 5 == 0:
        print("fizzbuzz")
        continue
    elif current_value % 3 == 0:
        print("fizz")
        continue
    elif current_value % 5 == 0:
        print("buzz")
        continue
    print(current_value)