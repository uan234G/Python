# Lists: ordered, mutable, allows duplicate elemenets
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# slice - speciy start idx and stop idx.
a = mylist[1:5]
print(a)
# returns [2, 3, 4, 5] | last idx excluded


# print every second item
x = mylist[::2]
print(x)


# reverse list
y = mylist[:: -1]
print(y)

###########
# square values in a list
mylist2 = [1, 2, 3, 4, 5, 6]
squaredlist = [i*i for i in mylist2]

print(mylist2)
print(squaredlist)
