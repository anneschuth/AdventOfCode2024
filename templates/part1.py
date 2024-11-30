from collections import defaultdict, OrderedDict, Counter
from copy import deepcopy
from functools import cmp_to_key
import math
import regex as re

# f = open('input.txt')
f = open('input_test.txt')


def print_grid(grid):
    for l in grid:
        print("".join([str(x) for x in l]))
    print()


def process_grid(grid):
    return 0


grid = []
for line in f.readlines():
    if not line.strip():
        continue
    grid.append(list(line.strip()))

print_grid(grid)
s = process_grid(grid)

print(s)
