palindromes = {x for x in range(1, 101) if str(x) == str(x)[::-1]}

print("Set of palindromic numbers from 1 to 100: ", palindromes)
