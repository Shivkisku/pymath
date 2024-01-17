list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = {x for x in list1 if x in list2}

print("List 1:", list1)
print("List 2:", list2)
print("Common Elements Set:", common_elements)
