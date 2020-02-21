"""
 *****************************************************************************
   FILE:        ball.py

   AUTHOR:      Professors

   ASSIGNMENT:  Loops

   DESCRIPTION: Professors' program for Ball problem.
 *****************************************************************************
"""

def main():

    initial_height = float(input("Enter initial height: "))
    first_bounce = float(input("Enter height of first bounce: "))
    bounces = int(input("Enter number of bounces: "))

    # Calculate bounce index
    bounce_index = first_bounce / initial_height
    distance = 0

    # Loop once for each bounce, tracking distance and the
    # initial height of the next bounce.
    for bounce in range(bounces):
        distance += initial_height + first_bounce
        initial_height = first_bounce
        first_bounce = first_bounce * bounce_index

    print("The total distance the ball traveled is", round(distance, 2), "feet.")



# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
