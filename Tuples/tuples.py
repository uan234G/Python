# ordered, allows duplicates BUT immutable!!

mytuple = "max", 30, "Las Vegas"
iterabletuple = tuple(["mario", 67, "LA"])

print(mytuple)
print(iterabletuple)

for i in mytuple:
    print(i)


new_tuple = ['a', 'r', 'y', 'y', 'z', 'f']
# length
print(len(new_tuple))
# occurance count
print(new_tuple.count('y'))
# idx of specific element
print(new_tuple.index('z'))

# convert tuple to list
my_list = list(new_tuple)

####### SLICE TUPLE #####

tuple_a = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
tuple_b = tuple_a[2:5]
print(tuple_b)
