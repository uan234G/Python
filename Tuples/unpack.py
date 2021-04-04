# unpacking tuples

my_tuple = "Pedro", 26, "New York"

name, age, city = my_tuple
# #of elements must match tuple

print(name)
print(age)
print(city)


# NUMBERS
t = (0, 1, 2, 3, 4)

a, b, *c = t

print(a)
print(b)
print(c)
# 0
# 1
# [2, 3, 4]

print(type(c))
# <class 'list'>

a, *b, c = t

print(a)
print(b)
print(c)
# 0
# [1, 2, 3]
# 4

*a, b, c = t

print(a)
print(b)
print(c)
# [0, 1, 2]
# 3
# 4
