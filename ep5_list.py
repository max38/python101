value_list_1 = list()
value_list_2 = []
value_list_3 = [1, 2, 3, 4, 4, 4, 4]
value_list_4 = ["Hello", "World", "Thailand"]
value_list_5 = [1, 3, "a", "b"]

value_list_6 = [
    1, 2, ["a", "b"], 4, [20, 13, 34]
]

print(value_list_6[0])  # Result 1
print(value_list_6[2])  # Result ["a", "b"]
print(value_list_6[2][0])  # Result "a"


value_string_list = ["a", "b", "c", "d", 5, 6, 7, 7, 7]
len(value_string_list) # Function นับจำนวน // Return 9

print(value_string_list[-1]) # Result 7
print(value_string_list[1:5]) # Result ['b', 'c', 'd', 5]
print(value_string_list[:5]) # Result ['a', 'b', 'c', 'd', 5]
print(value_string_list[2:]) # Result ['c', 'd', 5, 6, 7, 7, 7]

print(value_string_list[::2]) # Result ['a', 'c', 5, 7, 7]
print(value_string_list[::-2]) # Result [7, 7, 5, 'c', 'a']


'''
<list object>.append(value)
'''
#---------------------------
fruits = ['apple', 'banana']
fruits.append("orange")
print(fruits) # Result ['apple', 'banana', 'orange']

a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a) # Result ???

'''
<list object>.clear()
'''
#---------------------------
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits) # Result []


'''
<list object>.count(value)
'''
#---------------------------
fruits = ['apple', 'banana', 'cherry', 'cherry']
x = fruits.count("cherry") # Result x = 2
x = fruits.count("apple") # Result x = 1


'''
<list object>.extend(iterable)  
'''
# Any iterable (list, set, tuple, etc.)
#---------------------------
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits) # Result ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']
print(cars) # Result ['Ford', 'BMW', 'Volvo']


'''
<list object>.index(value)
'''
#---------------------------
numbers = [4, 55, 64, 32, 16, 32]
x = numbers.index(32) # Result x = 3
y = numbers.index(32, 4, 6) # Result y = 5

is_has_number = 55 in numbers
print(is_has_number) # Result True
print(10 in numbers) # Result False


'''
<list object>.insert(position, value)
'''
#---------------------------
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits) # Result ['apple', 'orange', 'banana', 'cherry']


'''
<list object>.pop(position)
'''
#---------------------------
characters = ['a', 'b', 'c', 'd', 'e']
x = characters.pop(1) 
print(x) # Result 'b
print(characters) # Result ['a', 'c', 'd', 'e']

y = characters.pop() 
print(y) # Result 'e'
print(characters) # Result ['a', 'c', 'd']


'''
<list object>.remove(value)
'''
#---------------------------
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits) # Result ['apple', 'cherry']


'''
<list object>.reverse()
'''
#---------------------------
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits) # Result ['cherry', 'banana', 'apple']


'''
<list object>.sort(reverse=True|False, key=Function)
'''
#---------------------------
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars) # Result ['BMW', 'Ford', 'Volvo']
cars.sort(reverse=True)
print(cars) # Result ['Volvo', 'Ford', 'BMW']


'''
<list object>.copy()
'''
#---------------------------
fruits = ['apple', 'banana', 'cherry']
fruits_copied = fruits.copy()
print(fruits_copied) # Result ['apple', 'banana', 'cherry']

x = fruits
x.append('orange')
print(x) # Result ['apple', 'banana', 'cherry', 'orange']
print(fruits)  # Result ['apple', 'banana', 'cherry', 'orange']


#---------------------------
characters = ['a', 'b', 'c']
numbers = [1, 2, 3]

x = characters + numbers
print(x) # Result ['a', 'b', 'c', 1, 2, 3]


#---------------------------
characters = ['a', 'b', 'c']

characters += ['d', 'e', 'f']
print(characters)
# Result ['a', 'b', 'c', 'd', 'e', 'f']

#---------------------------
characters = ['a', 'b', 'c']
x = characters * 2
print(x)
# Result ['a', 'b', 'c', 'a', 'b', 'c']

characters *= 2
print(characters)
# Result ['a', 'b', 'c', 'a', 'b', 'c']



text = "I am a happy Sukhum"
text = text.split() 
print(text)
# Result ['I', 'am', 'a', 'happy', 'Sukhum']

text = "I,am,a,happy,Sukhum"
text = text.split(",") 
print(text)
# Result ['I', 'am', 'a', 'happy', 'Sukhum']

#------------------------
text_list = ['I', 'am', 'a', 'happy', 'Sukhum']
text = " ".join(text_list)
print(text)
# Result "I am a happy Sukhum"


"Sukhum" != ["S", "u", "k", "h", "u", "m"]

"""ไม่เท่ากับ List ทางขวามือจะหมายถึง List ของ String อีกที"""

"Sukhum" == "".join(["S", "u", "k", "h", "u", "m"])
