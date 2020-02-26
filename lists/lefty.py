"""
 *****************************************************************************
   FILE:        lefty.py

   AUTHOR:      Professors

   ASSIGNMENT:  Lists

   DESCRIPTION: Professors' solution program.
 *****************************************************************************
"""

LEFT_HAND = "QWERTASDFGZXCVB"

def main():
    user_input = input("Enter words separated by spaces: ")
    strings = user_input.split()

    # Look at each word in the input
    for word in strings:

        # Use its_lefty to track if word is still all left hand.
        its_lefty = True
        for char in word:
            if char.upper() not in LEFT_HAND:
                its_lefty = False

        if its_lefty:
            print("This word is only written with the left hand:", word)



# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
