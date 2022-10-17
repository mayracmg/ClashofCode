import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# INPUT: 5 2
# OUTPUT:
# 0 2 4 6 8

# INPUT: 5 3
# OUTPUT:
# 0 3 6 9 12

# INPUT: 3 0
# OUTPUT:
# 0 0 0

n, r = [int(i) for i in input().split()]

result = ""
counter = 0

for i in range(0, n):
    result += str(counter) + " "
    counter += r

print(result.rstrip())
