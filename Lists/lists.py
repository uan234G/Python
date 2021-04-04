mylist = ["banana", "apple", "orange"]
print(mylist)

mylist2 = [5, "apple", "apple", True, 0.0023]  # lists can have duplicate items

item1 = mylist2[4]
# negative index ..[-1] = last item .. [-2]= second to last
print(item1)

# print length of any list
print(len(mylist))
print(len(mylist2))

for i in mylist:
    print(i)

for i in mylist2:
    print(i)

if "apple" in mylist2:
    print("YES")
else:
    print("NO")

mylist.append("lemon")
# appends to end of list
print(mylist)
mylist.insert(0, "lemon")
# adds to 0 index of list
print(mylist)

# other methos .pop() removes last | .remove("specific item") | .clear() removes all | .reverse() reverse list |
# .sort() sorts original list | .sorted() doesnt change orinal list
# .copy() -copy list
