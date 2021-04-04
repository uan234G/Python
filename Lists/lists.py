myList = ["banana", "apple", "orange"]
print(myList)

myList2 = [5, "apple", "apple", True, 0.0023]  # lists can have duplicate items

item1 = myList2[4]
# negative index ..[-1] = last item .. [-2]= second to last
print(item1)

# print length of any list
print(len(myList))
print(len(myList2))

for i in myList:
    print(i)

for i in myList2:
    print(i)

if "apple" in myList2:
    print("YES")
else:
    print("NO")

myList.append("lemon")
# appends to end of list
print(myList)
myList.insert(0, "lemon")
# adds to 0 index of list
print(myList)
