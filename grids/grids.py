"""
 *****************************************************************************
   FILE:        grids.py

   AUTHOR:      Professors

   ASSIGNMENT:  Grids

   DESCRIPTION: Professors' solution program.
 *****************************************************************************
"""

from professors import input_data

# Complete these functions.  Don't change the headers (def line:
# function names and parameters) or the docstrings. The program is
# already designed to use these.

def locate_target(grid, target):
    """ Return a list of the locations (tuples) of target within grid. """

    grid_size = len(grid)
    return [(r, c)
            for r in range(grid_size)
            for c in range(grid_size)
            if grid[r][c] == target]


def is_in_bounds(grid, loc_tuple):
    """ Return True if loc_tuple is a legal position within grid.
        Return False otherwise. """

    # For convenience, get the grid size (all grids are square), and pull
    # apart the given loc_tuple:
    grid_size = len(grid)
    row_loc = loc_tuple[0]
    col_loc = loc_tuple[1]

    return (0 <= row_loc < grid_size and
            0 <= col_loc < grid_size)


def sum_all_neighbors(grid, location_list, direction):
    """ For each location in location_list, determine its neighbor in the 
        given direction, if it exists.  Return the sum of all such 
        neighbors. """

    # To save yourself some effort, make use of this:
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                  (1, 0), (1, -1), (0, -1), (-1, -1)]

    neighbor_sum = 0

    dr, dc = directions[direction]
    for r, c in location_list:
        rp, cp = r + dr, c + dc
        if is_in_bounds(grid, (rp, cp)):
            neighbor_sum += grid[rp][cp]
    
    return neighbor_sum 


def print_zero_grid(grid, location_list):
    """ Prints the grid with each entry at the locations in location_list
        replaced by the digit 0. Does not actually modify grid.  
        The output should be in square form, each number in a row followed by
        a space, and each row terminated with a newline. """

    grid_size = len(grid)
    for r in range(grid_size):
        for c in range(grid_size):
            fmt = "0 " if (r, c) in location_list else "{} "
            print(fmt.format(grid[r][c]), end="")
        print()
    
#######################################
#    DO NOT MODIFY BELOW THIS POINT   #
#######################################    

def main():
    """ The main function. """

    # Do not modify this function
    
    grid, target, direction = input_data()

    # Request a list of all locations of target in the given_grid:
    location_list = locate_target(grid, target)

    # Print the grid with each instance of target replaced by a zero:
    print_zero_grid(grid, location_list)

    # Print the location list
    for entry in location_list:
        print(entry)

    # Request the sum of neighbors of those locations in direction:
    neighbor_sum = sum_all_neighbors(grid, location_list, direction)
    print(neighbor_sum)


        
if __name__ == '__main__':
    main()
