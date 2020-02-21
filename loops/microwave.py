"""
 *****************************************************************************
   FILE:        microwave.py

   AUTHOR:      Professors

   ASSIGNMENT:  Loops

   DESCRIPTION: Professors' program for Microwave problem.
 *****************************************************************************
"""

def main():

    digits = input("Enter the digits as input to the microwave: ")

    # Get the seconds and minutes
    colon_index = digits.find(":")
    seconds = int(digits[colon_index + 1:])
    minutes = int(digits[:colon_index])

    # Total time in seconds
    total_time = seconds + 60 * minutes

    # Loop over the total seconds
    for _ in range(total_time):
        print("%i:%0.2i" % (minutes, seconds))

        # Decrement seconds by 1 each loop
        seconds -= 1

        # If seconds goes below 0, reset to 59 and decrement minutes
        if seconds < 0:
            seconds = 59
            minutes -= 1



# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
