"""
 *****************************************************************************
   FILE:        baby_animals.py

   AUTHOR:      Professors

   ASSIGNMENT:  Lists

   DESCRIPTION: Professors' solution program.
 *****************************************************************************
"""


def collect_animals():
    """ Collect animals from user input and return them in order in a list. """
    animal = input("Enter an animal name (press Enter to end): ")

    animals = []
    while animal != "":
        animals.append(animal)
        animal = input("Enter an animal name (press Enter to end): ")
    return animals


def get_line(subject, is_last):
    """ Return a string for the line of a stanza with the particular subject. 
        is_last is True if and only if the desired line is the last in a stanza. """
    if is_last:
        return subject + "!"
    else:
        return subject + ", doo doo doo doo doo doo"


def print_stanza(subject):
    """ Print one stanza for a song with the particular subject. """
    for line in range(0, 4):
        is_last = line == 3
        print(get_line(subject, is_last))


def print_song(animal):
    """ Print the entire song for a particular animal. """
    print("Now let's sing Baby", animal + "!")
    print("")
    print_stanza("Baby " + animal)
    print("")
    print_stanza("Typing " + animal)
    print("")
    print_stanza("Write some code")


def print_songs(animals):
    """ Print songs for all animals. """
    for animal_index in range(len(animals)):
        print_song(animals[animal_index])
        if animal_index != len(animals) - 1:
            print("")


def main():
    """ A program to accept a list of animal names and one at a time, 
        and print a Baby Shark-inspired song for each one. """
    print("Welcome to the baby animal song generator!")
    print('''(Inspired by Pinkfong's "Baby Shark")''')
    print("")
    animals = collect_animals()
    if len(animals) != 0:
        print_songs(animals)
    else:
        print("No animals entered! No song today :-(")


if __name__ == "__main__":
    main()
