value_tuple_1 = tuple()
value_tuple_2 = ("apple", "banana", "cherry")
value_tuple_3 = ("apple", )
value_tuple_4 = ("apple", [1, 2, 3], "cherry")
value_tuple_5 = ("a", "b", "c", "d", "e")

print(value_tuple_2[1]) # Result "banana"
print(value_tuple_4[1]) # Result [1, 2, 3]
print(value_tuple_5[1:3]) # Result ('b', 'c')
print(value_tuple_5[::2]) # Result ('a', 'c', 'e')

value_tuple_4[1].append(4)
print(value_tuple_4[1]) # Result [1, 2, 3, 4]
"""ตัวแปร Python จะเก็บเป็น Pointer 
ใน Case Tuple นี้ Tuple ยังคงชี้ไปที่ Memory ที่เก็บข้อมูล list ที่เดิม 
ไม่สามารถเปลี่ยนแปลง Pointer ไปชี้ที่อื่นได้ เช่นเดียวกับตัวแปรอื่นๆใน Tuple"""



<tuple object>.count(value)
#---------------------------
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) # Result 2


<tuple object>.index(value)
#---------------------------
numbers = (4, 55, 64, 32, 16, 32)
x = numbers.index(32) # Result x = 3
y = numbers.index(32, 4, 6) # Result y = 5

is_has_number = 55 in numbers
print(is_has_number) # Result True
print(10 in numbers) # Result False



thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
thislist = list(thistuple)
print(thislist) # Result [1, 3, 7, 8, 7, 5, 4, 6, 8, 5]


fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
green, yellow, red = fruits # SAME

print(green) # Result apple
print(yellow) # Result banana
print(red) # Result cherry



tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) # Result ('a', 'b', 'c', 1, 2, 3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# Result ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#----------------------------------------


my_set1 = {"value1", "value2", "value3"}
my_set2 = set(["value1", "value2", "value3"])
my_set3 = set("Sukhum")
my_set4 = set()

print(my_set1) # Result {'value1', 'value2', 'value3'}
print(my_set2) # Result {'value1', 'value2', 'value3'}
print(my_set3) # Result {'u', 'm', 'h', 'S', 'k'}
print(my_set4) # Result set()


numbers = {1, 2, 2, 3, 3, 4, 5}
colors = set(["red", "green", "blue", "blue", "yellow"])

print(numbers) # Result {1, 2, 3, 4, 5}
print(colors) # Result {'yellow', 'green', 'blue', 'red'}



numbers = {1, 2, 2, 3, 3, 4, 5}
print(numbers[2])


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

# Result:
# cherry
# banana
# apple


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) # Result True


<set object>.add(value)
#---------------------------
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Result {'orange', 'cherry', 'banana', 'apple'}


<set object>.update(iterable)
":param str Any Iterable: Required"
#---------------------------
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Result
# {'papaya', 'apple', 'mango', 'pineapple', 'cherry', 'banana'}


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# Result
# {'apple', 'cherry', 'banana', 'orange', 'kiwi'}


<set object>.remove(value)
#---------------------------
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) # Result {'cherry', 'apple'}

"Note: If the item to remove does not exist, remove() will raise an error."


<set object>.discard(value)
#---------------------------
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) # Result {'cherry', 'apple'}
"Note: If the item to remove does not exist, discard() will NOT raise an error."


<set object>.clear()
#---------------------------
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) # Result set()


<set object>.union(iterable)
#---------------------------
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.union(set2)
print(set3) # Result {'b', 'a', 'c', 'd'}


set1 = {"a", "b", "c"}
list_value = ["b", "c", "d"]
set2 = set1.union(list_value)
print(set2) # Result {'b', 'a', 'c', 'd'}


<set object>.intersection(iterable)
#---------------------------
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.intersection(set2)
print(set3) # Result {'b', 'c'}

set3 = set1 & set2
# set3 = {'b', 'c'}


<set object>.difference(iterable)
#---------------------------
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.difference(set2)
print(set3) # Result {'a'}

set3 = set2 - set1
# set3 = {'d'}



<set object>.symmetric_difference(iterable)
#---------------------------
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = set1.symmetric_difference(set2)
print(set3) # Result {'a', 'd'}


<set object>.issubset(iterable)
<set object>.issuperset(iterable)
#---------------------------
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}

print("Is a subset of b?", a.issubset(b))
print("Is b super set of a?", b.issuperset(a))

# Result
# Is a subset of b? True
# Is b super set of a? True


<set object>.isdisjoint(iterable)
#---------------------------
set1 = {"a", "b", "c"}
set2 = {"b", "c", "d"}
set3 = {"d", "e", "f"}
print(set1.isdisjoint(set2)) # Result False
print(set1.isdisjoint(set3)) # Result True

