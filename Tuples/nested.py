# Unpack a nested tuple and list
nested_tuple = (0, 1, (2, 3, 4))

a, b, c = nested_tuple

print(a)
print(b)
print(c)
# 0
# 1
# (2, 3, 4)

print(type(c))
# <class 'tuple'>

a, b, (c, d, e) = t

print(a)
print(b)
print(c)
print(d)
print(e)
# 0
# 1
# 2
# 3
# 4
