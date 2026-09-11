# key - value 

x = { 'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False }
      #|- Key   #|- Value
print(type(x))

"""
Output:
<class 'dict'>
"""

# nonsupport indexing
x = { 'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False }

print(x[0])

""" 
Output:
KeyError: 0
"""

# cara eksekusi yang benar
x = { 'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False }

print(x ['name'])

""" 
Output:
Wahyudin Ambia
"""

# menambahkan data pada dictionary
x = { 'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False }
x ['Job'] = "Web Developer"

print(x)

"""
Output:
{'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False, 'Job': 'Web Developer'}
"""

# m3nghapus data pada dictionary
x = { 'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False }
del x['isMarried']

print(x)

"""
Output:
{'name': 'Wahyudin Ambia', 'age': 19}
"""

# mengubah data pada dictionary
x = { 'name': 'Wahyudin Ambia', 'age': 19, 'isMarried': False }
x ['name'] = "Dicoding"

print(x)

"""
Output:
{'name': 'Dicoding', 'age': 19, 'isMarried': False}
"""

