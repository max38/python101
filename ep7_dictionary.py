
scores = {'james': 1828, 'thomas': 3628, 'danny': 9310}
scores['bobby'] = 4401

print(scores) # Result {'james': 1828, 'thomas': 3628, 'danny': 9310, 'bobby': 4401}

numbers = {1: 'One', 2: 'Two', 3: 'Three'}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# Result {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": {"red", "white", "blue"}
}


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# x = "Mustang"


<dict object>.get(key, default_value)
#---------------------------
x = thisdict.get("model")
# x = "Mustang"

y = thisdict.get("month")
# y = None

z = thisdict.get("month", 8)
# z = 8



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

<dict object>.keys()
#---------------------------
x = thisdict.keys()
# x = dict_keys(['brand', 'model', 'year'])



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

<dict object>.values()
#---------------------------
x = thisdict.values()
# x = dict_values(['Ford', 'Mustang', 2020])


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

<dict object>.items()
#---------------------------
x = car.items()
# x = dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#---------------------------
"Tips: Check if Key Exists"
x = "model" in thisdict
print(x) True



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"

#---------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
<dict object>.update(dictionary)
#---------------------------
thisdict.update({"color": "red"})


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#---------------------------

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
<dict object>.update(dictionary)
#---------------------------
thisdict.update({"year": 2020})


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#---------------------------
<dict object>.pop(dictionary_key)
#---------------------------
x = thisdict.pop("model")
print(thisdict)
# Result {'brand': 'Ford', 'year': 1964}
# x = 'Mustang'

#---------------------------
del thisdict["year"]



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#---------------------------
<dict object>.copy()
#---------------------------
mydict = thisdict.copy()


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)



x = thisdict

x['year'] = 2000
print(x['year'])
# Result 2000

print(thisdict['year'])
# Result 2000