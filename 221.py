perfect_cubes = {x for x in range(1, 101) if int(x**(1/3))**3 == x}

print("Set of perfect cubes from 1 to 100: ", perfect_cubes)
