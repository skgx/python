"""
Dictionary is an unordered collection of key-value pairs.
It is generally used when we have a huge amount of data.
 Dictionaries are optimized for retrieving data.
"""

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
print("d[2] = ", d[2])
