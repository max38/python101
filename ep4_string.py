

string_variable = str()
string_variable = str(123)

first_name = 'Sukhum'

first_name = "Tom"

text = "12" # ค่า '12' (string) จะไม่เท่ากับ 12 (integer)

paragraph = '''
This is a paragraph. It is
made up of multiple lines and sentences.
'''

paragraph = """
This is a paragraph. It is
made up of multiple lines and sentences.
"""



text = "Hello"
text2 = "World"

concated_string = text + ' ' + text2
print(concated_string) # Return "Hello World"

print(text + text2 + 555) # เกิด TypeError: must be str, not int

# วิธีการแก้ไขต้องแปลงค่า Integer ไปเป็น String ก่อน
print(text + text2 + str(555)) # Return HelloWorld555

text += "World"
print(text) # Return "HelloWorld"



text = "Sukhum"
print(text * 5) # Return "SukhumSukhumSukhumSukhumSukhum"

text *= 2
print(text) # Return "SukhumSukhum"



"เปลี่ยนตัวอักษรไปเป็น lowercase .lower()"
text.lower()
# If text = "SUKHUM", return "sukhum"
# If text = "SuKhUm", return "sukhum"
# If text = "sukhum", return "sukhum"

"เปลี่ยนตัวอักษรไปเป็น uppercase .upper()"
text.upper()
# If text = "SUKHUM", return "SUKHUM"
# If text = "SuKhUm", return "SUKHUM"
# If text = "sukhum", return "SUKHUM"

"สลับตัวอักษรระหว่าง lower/upper .swapcase()"
text.swapcase()
# If text = "SUKHUM", return "sukhum"
# If text = "SuKhUm", return "sUkHuM"
# If text = "sukhum", return "SUKHUM"






"เช็คว่าตัวอักษรนั้นเป็น lowercase ทั้งหมดหรือไม่ .islower()"
"เช็คว่าตัวอักษรนั้นเป็น uppercase ทั้งหมดหรือไม่ .isupper()"
text = "A"
return text.islower() # Return false
return text.isupper() # Return true

text = "a"
return text.islower() # Return true
return text.isupper() # Return false

"เช็คว่าตัวอักษรนั้นเป็นตัวเลขทั้งหมดหรือไม่ .isdigit()"
"เช็คว่าตัวอักษรนั้นเป็นตัวอักษรทั้งหมดหรือไม่ .isalpha()"
text = "12"
return text.isdigit() # Return true
return text.isalpha() # Return false

text = "ABC"
return text.isdigit() # Return false
return text.isalpha() # Return 





greeting_sentence = "Hello Sukhum"
greeting_sentence_len = len(greeting_sentence) # Function นับจำนวน
print(greeting_sentence_len) # Return 12

print(greeting_sentence[1]) # Return "e"
print(greeting_sentence[-1]) # Return "m"
print(greeting_sentence[1:5]) # Return "ello"
print(greeting_sentence[:5]) # Return "Hello"
print(greeting_sentence[2:]) # Return "llo Sukhum"


print(greeting_sentence[::2]) # Return "HloSku"
print(greeting_sentence[::-2]) # Return "mhu le"


"""
How to use:
<variable name type string>.find(value, start, end)

:param str value: Required. The value to search for
:param int start: Optional. Where to start the search. Default is 0
:param int end: Optional. Where to end the search. Default is to the end of the string
"""

# 1 occurence character
text = "ABCDE"
text.find("A") # Return 0

# 2 occurence character
text = "ABCDEAAAAA"
text.find("A") # Return 0
text.find("A", 1) # Return 5
text.find("A", 6) # Return 6

# Non occurence character
text = "ABCDE"
text.find("F") # Return -1

# Using more than 1 character
text = "Hello World"
text.find("Hello") # Return 0

# Using more than 1 character + 2 occurrence
text = "Hello World, Hello World"
text.find("Hello") # Return 0
text.find("Hello", 10, 12) # Return -1
text.find("Hello", 10, 19) # Return -1


"""
How to use:
<variable name>.count(value, start, end)

:param str value: Required. The value to count for
:param int start: Optional. Where to start the count. Default is 0
:param int end: Optional. Where to end the count. Default is to the end of the string
"""

# 1 occurence character
text = "ABCDE"
text.count("A") # Return 1

# 2 occurence character
text = "ABCDEAAAAA"
text.count("A") # Return 6
text.count("A", 1, 7) # Return 2

# Non occurence character
text = "ABCDE"
text.count("F") # Return 0

# Using more than 1 character
text = "Hello World"
text.count("Hello") # Return 1

# Using more than 1 character + 2 occurrence
text = "Hello World, Hello World"
text.count("Hello") # Return 2


text = "Sukhum".replace("u", "X")
print(text)
# Result 'SXkhXm'

text = "Hello World"
is_has_hello = "Hello" in text
print(is_has_hello) # Result True



firstname = 'Sukhum'
beverage = 'milk'
drink_time = 2
money = 45
spend_money = money * drink_time

result_message = 'My name is {}. I like a {} and drink it {} time(s) a day.'.format(firstname, beverage, drink_time)
# Result = 'My name is Sukhum. I like a milk and drink it 2 time(s) a day.'

result_message = """My name is {0}. I like a {1} and drink it {2} time(s) a day. 
The {1} is {3} Baht. I\'m spend {4} Baht per a day.""".format(firstname, beverage, drink_time, money, spend_money)
# Result = "My name is Sukhum. I like a milk and drink it 2 time(s) a day. \nThe milk is 45 Baht. I'm spend 90 Baht per a day."

result_message = "My name is {firstname}. I like a {beverage} and drink it {drink_time} time(s) a day.".format(
    firstname=firstname, beverage=beverage, drink_time=drink_time
)
# Result = 'My name is Sukhum. I like a milk and drink it 2 time(s) a day.'


text = "Sukhum"
number_one = 2
number_two = 1

print(f"number_one is {number_one} and number_two is {number_two}")

calculate_result_text = f"The answer is {number_one} + {number_two} = {(number_one + number_two)}. Calculated by {text}")
print(calculate_result_text)

print(f"text variable has len = {len(text)}.") # Result "text variable has len = 6."
print(f"upper text = {text.upper()}") # Result "upper text = SUKHUM"
print(f"upper substring = {text[1:3].upper()}") # Result "upper substring = UK"

