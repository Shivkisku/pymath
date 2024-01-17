set1 = {1, 2, 3}
set2 = {"a", "b", "c"}
pairs = {(x, y) for x in set1 for y in set2}

print("Set 1: ", set1)
print("Set 2: ", set2)
print("Pairs of elements from Set 1 and Set 2: ", pairs)
