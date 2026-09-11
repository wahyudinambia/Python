x = (1, "Wahyu", 1+3j)
print(type(x))

"""
Output:
<class 'tuple'>
"""

# indexing - slicing pada tuple
x = (5, 'program', 1+3j)
print(x[1])
print(x[0:3])

""" 
Output:
program
(5, 'program', (1+3j))
"""

# tuple bersifat immutable (tidak dapat di ubah nilainya)
x = (5, 'program', 1+3j)
x[1] = 'Wahyu'

"""
Output:
'tuple' object does not support item assignment
"""