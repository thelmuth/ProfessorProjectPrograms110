"""
 *****************************************************************************
   FILE:        pool.py  

   AUTHOR:      Professors

   ASSIGNMENT:  Calculations

   DESCRIPTION: Professors' program for pool problem.
 *****************************************************************************
"""

CUBIC_INCHES_PER_GALLON = 231

def main():

    length = float(input("Pool length (feet): "))
    width = float(input("Pool width (feet): "))
    addedDepth = float(input("Additional depth desired (inches): "))
    waterRate = float(input("Water fill rate (gal/min): "))

    # Convert volume to gallons.
    volume = length * 12 * width * 12 * addedDepth
    gals = volume / CUBIC_INCHES_PER_GALLON

    # Calculate total time in minutes
    time = gals / waterRate
    minutes = int(time)
    minFrac = time - minutes

    # Calculate hours, minutes, and seconds
    hours = minutes // 60
    minutes = minutes % 60
    seconds = round(minFrac * 60)

    print("Time: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
