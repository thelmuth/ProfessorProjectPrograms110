"""
 *****************************************************************************
   FILE:        pig_latin.py

   AUTHOR:      Professors

   ASSIGNMENT:  Lists

   DESCRIPTION: Professors' solution program.
 *****************************************************************************
"""

VOWELS = "aeiou"

def main():

    sentence = input("Enter a sentence: ")
    words = sentence.split()
    new_sentence = ""

    for word in words:
        # Check if word starts with vowel:
        if word[0] in VOWELS:
            new_word = word + "ay"
        else:
            new_word = word[1:] + word[0] + "ay"

        # Add the new word with a space.
        new_sentence += " " + new_word

    # Don't print first space
    print("Pig Latin:", new_sentence[1:])


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
