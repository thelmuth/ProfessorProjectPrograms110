"""
 *****************************************************************************
   FILE:        pizza.py

   AUTHOR:      Professors

   ASSIGNMENT:  Calculations

   DESCRIPTION: Professors' program for Pizza problem.
 *****************************************************************************
"""

import math

def main():

    standard_diameter = int(input('What is the diameter of a "standard" size pie? '))
    slice_count = int(input("How many slices are in a standard size pie? "))
    slices = int(input("How many standard slices do you want? "))
    diameter = int(input("What is the diameter of the pies you will buy? "))

    # Calculate number of pies
    pies = slices * (standard_diameter ** 2.0) / ((diameter ** 2) * slice_count)
    pies_ceiling = int(math.ceil(pies))

    print("You will need to buy", pies_ceiling, str(diameter) + "-inch diameter pies.")



# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
