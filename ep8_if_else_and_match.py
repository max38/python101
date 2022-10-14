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


#--------

fruit = 'Yamaha'
 
if fruit == 'Hero':
    print("letter is Hero")
    
elif fruit == "Suzuki":
    print("letter is Suzuki")
 
elif fruit == "Yamaha":
    print("fruit is Yamaha")
 
else:
    print("Please choose correct answer")

#-------

fruit = 'Hero'

print_output = {
    'Hero': "letter is Hero",
    'Suzuki': "letter is Suzuki",
    'Yamaha': "fruit is Yamaha",
}

print(print_output[fruit])

print(print_output.get(fruit, "Please choose correct answer"))



######################

fruit = 'Yamaha'
 
if fruit == 'Hero':
    print("letter is Hero")
    
elif fruit == "Suzuki":
    print("letter is Suzuki")
 
elif fruit == "Yamaha":
    print("fruit is Yamaha")
 
else:
    print("Please choose correct answer")
    

fruit = 'test'

match fruit:
    case 'Hero':
        print("letter is Hero")
    case "Suzuki":
        print("letter is Suzuki")
    case "Yamaha":
        print("fruit is Yamaha")
    case default:
        print("Please choose correct answer")
    
#-------------------------

number = 0

match number:
    case 0:
        print("zero")
    case 1:
        print("one")
    case 2:
        print("two")
    case default:
        print("something")
 
#--------

point = (1, 2)

# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

#---------------------

point = (1, 1)

match point:
    case (x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case (x, y):
        print(f"Point is not on the diagonal.")

#----------------------

prediction_result = [2,1,0]
prediction_result = [1,7]
prediction_result = [6]

switch prediction_result :
    case [x] :
        print(f"Result contains single element is {x}")
    case [x,y] :
        print(f"Result contains 2 elements are {x} and {y}")
    case [x,10] :
        print(f"Result contains 2 element but one of them is not exists ({x})")
    case [x,y,z] :
        print(f"Result contains 3 elements are {x}, {y} and {z}")
        
