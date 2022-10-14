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
    
#-----
    
values = {
    "green": "apple",
    "yellow": "banana",
    "red": "cherry"
}

for key in values:
    print(key)
    print(values[key])
    
    
fruits = ["apple", "banana", "cherry", "testy"]

for i, v in enumerate(fruits):
    if i == 0:
        print("First loop")
    print(i, v)
    

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
    print(number)



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


