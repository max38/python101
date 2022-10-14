
def function_name(args...):
    # statements

def function_name(args...):
    # statements
    return value


def hello_world():
    print("Hello World")


def add(number_a, number_b):
    result = number_a + number_b
    return result


def add(number_a, number_b):
    if type(number_a) == int and type(number_b) == int:
        result = number_a + number_b
        return result
    else:
        print("Please provide number_a and number_b are integer variable")
        return None

x = add(4, 5)
y = add("3", 6)

ืnumber_1 = 50
number_2 = 40
z = add(number_1, number_2)


def add(number_a: int, number_b: int):
    if type(number_a) == int and type(number_b) == int:
        result = number_a + number_b
        return result
    else:
        print("Please provide number_a and number_b are integer variable")
        return None



def show_info(name, salary=50000):
    print('Name: %s' % name)
    print('Salary: %d' % salary)

# calling function
show_info(name='Sukhum', salary=105000)


def show_info(name, salary=50000, year=10):
    print('Name: %s' % name)
    print('Salary: %d' % salary)
    print('Year: %d' % year)


## Recursion

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

"""
Recursion Example Results
1
3
6
10
15
21
"""


# lampda

average = lambda a, b: (a + b) / 2
print(average(3, 5))  # Result 4.0
print(average(10, 33))  # Result 21.5

def average(a, b):
    return (a + b) / 2

def average(a, b):
    result = (a + b) / 2
    return result


hi = lambda: print("Hi everyone")
hello = lambda name: print("Hello %s" % name)

hi()
hello("Sukhum")



def snail_movement_calculate(high=1, up=1, down=0.5):
    snail_distance = 0
    day = 1
    while True:
        # Daytime
        snail_distance = snail_distance + up
        print("snail_distance ", snail_distance)

        # Daytime
        if snail_distance >= high:
            print("snail_distance >= high")
            break

        # Night Time
        snail_distance = snail_distance - down
        day = day + 1
        print("day = day + 1")

    print(f"{day} day(s).")
    return day

