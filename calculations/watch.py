"""
 *****************************************************************************
   FILE:        watch.py

   AUTHOR:      Professors

   ASSIGNMENT:  Calculations

   DESCRIPTION: Professors' program for Watch problem.
 *****************************************************************************
"""

def main():

    timeStr = input("What time does your upside-down watch read (hours:minutes)? ")

    # Deconstruct input
    colon = timeStr.index(":")    
    hours = int(timeStr[:colon])
    minutes = int(timeStr[colon + 1:])

    # Calculate hours and minutes
    hours = (hours + 5) % 12 + 1
    minutes = (minutes + 90) % 60

    print("The right-side-up time is: {:d}:{:02d}".format(hours, minutes))

# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
