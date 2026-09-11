x = 'Wahyu'
print(type(x))

"""
Output: 
<class 'str'>
"""

# dapat menggunakan lebih dari satu baris (multi line)
linemulti_line = """Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu."""

print(multi_line)

"""
Output:
Halo!
Kapan terakhir kali kita bertemu?
Kita bertemu hari Jum’at yang lalu.
"""

# string menggunakan urutan karakter (indeks)
x = 'Wahyu'
print(x[0])

""" 
Output:
D
"""

# ini tidak bisa, karna string bersifat immuntable
x = 'Dicoding'
x[0] = 'F'

""" 
Output:
TypeError: 'str' object does not support item assignment
"""


# indexin, slicing
x = 'Wahyu'
print(x[2:])

"""
Output:
coding
"""