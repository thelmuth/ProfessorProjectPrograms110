"""
 *****************************************************************************
   FILE:        hogwarts.py  

   AUTHOR:      Professors

   ASSIGNMENT:  Hogwarts

   DESCRIPTION: Professors' program for Hogwarts problem.
 *****************************************************************************
"""

def main():
    print("Welcome to the Hogwarts Start-of-Term Feast!")

    gryffindor = int(input("Number of Gryffindor students: "))
    hufflepuff = int(input("Number of Hufflepuff students: "))
    ravenclaw = int(input("Number of Ravenclaw students: "))
    slytherin = int(input("Number of Slytherin students: "))
    
    new_students = int(input("Number of new students: "))
    
    place_new = (new_students // 2) * 4
    place_settings = gryffindor + ravenclaw + slytherin + hufflepuff + place_new
    
    print("You'll need", place_settings, "place settings for the Start-of-Term Feast!")


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
