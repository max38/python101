number = 15

if (number > 10):
    print("number is more than 10.")

if number == 15:
    print("number is 15.")

if number < 10:
    print("number is less than 10.")

number_a = 10
number_b = 15

if type(number_a) == int and type(number_b) == int:
    number_c = number_a + number_b
    print(number_c)




number = 15

if number >= 10:
    print("number is more than or equal 10.")
else:
    print("number is less than 10.")



game_level = input('Enter level (1 - 4): ')

if type(game_level) == str:

    if game_level == '1':
        print('Easy')
    elif game_level == '2':
        print('Medium')
    elif game_level == '3':
        print('Hard')
    elif game_level == '4':
        print('Expert')
    else:
        print('Invalid level selected')
else:
    print(game_level)


x = 5
number_list = [1, 2, 3, 4, 5, 6]

if x in number_list:
    print(f"x={x} is in number_list")
elif sum(number_list) > 30:
    print("Summary of number_list is more than 30")
else:
    print("Not valide in condition")



need_odd_number = False

ืnumber = 5 if need_odd_number else 6

######################

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
for n in numbers:
    print(n)

# loop through string
text_string = 'pythoncode'
for character in text_string:
    print(character)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

    if x == "banana":
        print("x is banana now.")
        break


for i in range(1, 11):   
    if i % 2 == 1:
        continue

    print(i, end = ', ')

##################



number = 1

while number <= 10:
    print(number, end = ', ')
    number += 1


number = 1
while number < 6:
    print(number)

    if number == 3:
        break
    number += 1



number = 0
while number < 6:
    number += 1

    if number== 3:
        continue
    print(i)



first_name = "Sukhum"

while first_name == "Sukhum":
    print("You are in an infinite loop")




first_name = "Sukhum"
hello_count = 0

while first_name == "Sukhum":
    hello_count += 1
    print(f"Hello {first_name}. {hello_count} times.")

    if hello_count > 5:
        break


