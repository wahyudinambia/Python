x = [1, 2.2, 'Wahyu']
print(type(x))

"""
Output: 
<class ‘list’>
"""

# indexing
x = [1, 'Wahyu', True, 1.0]

print(x[2])

""" 
Output:
True
"""
# muntable (dapat diubah nilainya)
x = [1, 2.2, 'Wahyu']
x[0] = 'Indonesia'
print(x)

"""
Output:
['Indonesia', 2.2, 'Wahyu']
"""

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0])
print(x[2])
print(x[-1])
print(x[-3])


"""
Output:
laptop
mouse
microphone
keyboard
"""


# slicing
sequence[start:stop:step]

x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(x[0:5:2])
print(x[1:])
print(x[:3])

"""
Output:
['laptop', 'mouse', 'keyboard']
['monitor', 'mouse', 'mousepad', 'keyboard', 'webcam', 'microphone']
['laptop', 'monitor', 'mouse']

"""