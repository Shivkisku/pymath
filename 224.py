set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
set3 = {5, 6, 7, 8, 9}

common_elements = {x for x in set1 if x in set2 and x in set3}

print("Set 1: ", set1)
print("Set 2: ", set2)
print("Set 3: ", set3)
print("Common Elements: ", common_elements)
