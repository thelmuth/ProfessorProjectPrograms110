"""
 *****************************************************************************
   FILE:        worddown.py

   AUTHOR:      Professors

   ASSIGNMENT:  Lists

   DESCRIPTION: Professors' solution program.
 *****************************************************************************
"""

def main():
    num_words = int(input("How many words are in your worddown? "))

    # Create the list of words.
    word_list = []
    for word_id in range(1, num_words + 1):
        word = input("Enter word {}: ".format(word_id))
        word_list.append(word)
   
    print()
    print("Let the worddown begin!")

    # Loop over the words (in reverse order), checking for Easter eggs.
    for word_index in range(num_words - 1, -1, -1):
        current_word = word_list[word_index]
        if current_word == "Mars":
            print(current_word + " (finally!)")
        elif current_word == "Moon":
            print(current_word + " (it's not made of cheese!)")
        elif current_word == "shuttle":
            print(current_word + " (everyday I'm shuttling!)")
        else:
            print(current_word + "...")

    print("Blastoff!")


# this invokes the main function.  It is always included in our
# python programs
if __name__ == "__main__":
    main()
