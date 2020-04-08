"""
 *****************************************************************************
   FILE:        robot.py

   AUTHOR:      Professors

   ASSIGNMENT:  Amazon Warehouse Robot

   DESCRIPTION: Professors' solution program.
 *****************************************************************************
"""
"""
Project 7: Amazon Warehouse Robot
Tom Helmuth
Authority program.
"""

import random

DIRECTIONS = ["R", "L", "U", "D"]
WAREHOUSE_PILES = ["stack of 782 eyelash curlers",
                   "carton of Alanis Morissette CDs",
                   "55-gallon drum of high-fructose corn syrup"]


def input_warehouse():
    """Inputs a warehouse into a grid.
    You may want to comment out this function and replace it with a hard-coded
    warehouse for testing. That said, you MUST make sure it is back to its
    original form for submission, so we can test your robot in different
    warehouses."""

    WIDTH = 8

    warehouse = []
    for _ in range(WIDTH):
        row = ["empty"] * WIDTH
        warehouse.append(row)

    for row in range(WIDTH):
        warehouse[row][0] = "obstacle"
        warehouse[row][WIDTH - 1] = "obstacle"

    for column in range(WIDTH):
        warehouse[0][column] = "obstacle"
        warehouse[WIDTH - 1][column] = "obstacle"

    warehouse[4][2] = "robot"

    warehouse[2][3] = "obstacle"
    warehouse[3][3] = "obstacle"
    warehouse[4][3] = "obstacle"
    warehouse[5][3] = "obstacle"
    warehouse[3][5] = "obstacle"
    warehouse[3][6] = "obstacle"
    warehouse[4][5] = "obstacle"
    warehouse[4][6] = "obstacle"

    warehouse[2][1] = "package A"
    warehouse[1][6] = "dropoff A"
    warehouse[6][5] = "package B"
    warehouse[3][4] = "dropoff B"

    return warehouse


def print_room(room):
    """Prints a robot's room.
    You should not change this function."""
    for row in room:
        for element in row:
            if element == "empty":
                print(" ", end="")
            elif element == "robot":
                print("R", end="")
            elif element == "obstacle":
                print("O", end="")
            elif element == "dirt":
                print(".", end="")
            elif element.startswith("package"):
                print(element[-1].lower(), end="")
            elif element.startswith("dropoff"):
                print(element[-1].upper(), end="")


        print()
    print()


def robot_location(room):
    """Finds the robot's location in the room.
    You should not change this function"""

    for row in range(len(room)):
        for col in range(len(room[0])):
            if room[row][col] == "robot":
                return (row, col)


def all_delivered(warehouse, steps):
    """Helper Function. Returns True if all packages have been delivered, False otherwise."""
    for row in warehouse:
        for element in row:
            if element.startswith("dropoff"):
                return False

    return True


def move_robot(room, direction, packages_held):
    """Moves the robot in the given direction, if it doesn't hit an obstacle.
    You will need to change/add to this function!"""

    # Find robot's location
    (robot_row, robot_col) = robot_location(room)

    # See what is at robot's intended new location
    intended_row = robot_row
    intended_col = robot_col

    if direction == "R":
        intended_col = robot_col + 1
    elif direction == "L":
        intended_col = robot_col - 1
    elif direction == "U":
        intended_row = robot_row - 1
    elif direction == "D":
        intended_row = robot_row + 1

    intended_contents = room[intended_row][intended_col]

    # Check if entering a dropoff point.
    if intended_contents.startswith("dropoff"):
        # Drop off package!
        if intended_contents[-1] in packages_held:
            print("Robot delivered package {}.".format(intended_contents[-1]))
            room[intended_row][intended_col] = "robot"
            room[robot_row][robot_col] = "empty"

            # Remove package from list
            index_of_package = packages_held.index(intended_contents[-1])
            packages_held.pop(index_of_package)

        else:
            print("Robot does not have package", intended_contents[-1],
                  "and cannot enter the dropoff area.")

    # If not obstacle, move there! Otherwise, don't move robot
    elif intended_contents != "obstacle":
        room[intended_row][intended_col] = "robot"
        room[robot_row][robot_col] = "empty"
    else:
        print("Ouch, who put that {} there?".format(random.choice(WAREHOUSE_PILES)))

    return intended_contents

def move_carry_deliver_helper(warehouse, direction, packages_held, steps):
    """ Helper Function. Moves robot and prints out messages associated
        with the movement. This is primarily used in testing. """
    intended_contents = move_robot(warehouse, direction, packages_held)
    location = robot_location(warehouse)

    if intended_contents.startswith("package"):
        package = intended_contents[-1]
        packages_held.append(package)
        print("Robot picked up package {}.".format(package))

    # Print the info!
    print("After {} steps, robot moved {}, and is at location {}.".format(steps, direction, location))
    for package in packages_held:
        print("Robot is carrying package {}.".format(package))

    print_room(warehouse)


def walk_around_warehouse(warehouse):
    """Has robot conduct random walk until all packages are delivered."""

    # Print the original warehouse. Do not remove.
    print_room(warehouse)

    # Track number of steps and packages held
    steps = 0
    packages_held = []

    while not all_delivered(warehouse, steps):
        direction = random.choice(DIRECTIONS)

        move_carry_deliver_helper(warehouse, direction, packages_held, steps)

        steps += 1

    return steps

def deliver_all_packages(warehouse):
    """Do not change this function."""
    steps = walk_around_warehouse(warehouse)
    print("It took the robot {} steps to deliver all the packages!".format(steps))

##################################################
#                                                #
# None of the functions below should be changed. #
#                                                #
##################################################

def deliver_all_packages(warehouse):
    """A function used in testing.
    You should not change this function."""
    steps = walk_around_warehouse(warehouse)
    print("It took the robot {} steps to deliver all the packages!".format(steps))


def main():
    """The main function.
    You should not change this function."""
    warehouse = input_warehouse()
    deliver_all_packages(warehouse)


if __name__ == "__main__":
    main()
