# konversi integer - float
print(float(5))

"""
Output:
5.0
"""

# konversi float - integer
print(int(5.6))
print(int(-5.6)) 

""" 
Output:
5
-5
"""

# konversi - dan - ke string 
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))

"""
Output:
25
25
25.0
25.6
"""

# error
print(int("1p"))

"""
Output:
ValueError: invalid literal for int() with base 10: '1p
"""