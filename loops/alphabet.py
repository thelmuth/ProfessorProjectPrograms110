"""
 *****************************************************************************
   FILE:        alphabet.py

   AUTHOR:      Professors

   ASSIGNMENT:  Loops

   DESCRIPTION: Professors' program for Alphabet problem.
 *****************************************************************************
"""

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():

    string = input("Enter some text: ")

    string_upper = string.upper()
    result = ""

    # Loop over the letters, keeping track of those not in string
    for letter in LETTERS:
        if letter not in string_upper:
            result += letter

    print("Letters not in the text:", result)


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
