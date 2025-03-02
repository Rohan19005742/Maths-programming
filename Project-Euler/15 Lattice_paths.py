# given a grid_size how many different manthatten paths can there be in the grid?

import math

def lattice_paths(grid_size):
    return math.comb(grid_size*2,grid_size)


print(lattice_paths(20))