# set tidak dapat melakukan indexing karena set tidak memiliki index 
x = {1,2,7,2,3,13,3}
print(x[0])

"""
Output:
'set' object is not subscriptable
"""
 #Set juga bersifat unik, artinya, data yang Anda simpan pada set tidak akan ada duplikat.
 
x = {1, 2, 7, 2, 3, 13, 3}
print(x)
print(type(x))

"""
Output:
{1, 2, 3, 7, 13}
<class 'set'>
"""

# operasi union & intersection intersection
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# menggabungkan var1 dan var2
union = set1.union(set2)
print("Union:", union)

# mengambil nilai sama dari var1 dan var2
intersection = set1.intersection(set2)
print("Intersection:", intersection)

"""
Output:
Union: {1, 2, 3, 4, 5, 6, 7, 8}
Intersection: {4, 5}
"""

