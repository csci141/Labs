# Author:
# Date:
# Description:

import sys
import random

def random_pick(words, numbers):
    """ Generate a random winning lottery pick. The winning
    pick is a string containing one item from words (a list
    of strings) and one item from numbers (a list of ints),
    concatenated in a randomly chosen order. The random
    choices are made independently, so the chance of each
    possible pick is equal."""
    
    # (TASK 1) - Pseudocode:
    # Pick one of the numbers randomly
    # Pick one of the words randomly  
    # Pick which order they go in randomly
    # return the combined lottery pick as a string
 

def get_guess(words, numbers):
    """ Prompt the user until they enter a pick that contains one
        of the given words and begins or ends with one
        of the given numbers. When a valid guess is entered, return
        it.
        Precondition: numbers contains only one-digit numbers. """
    
    # (TASK 2) - Pseudocode:
    # while the user has not entered a valid pick:
    #    prompt the user for a pick
    #    check if it's valid (see docstring for the precise definition of valid)
    #    if not, print a message saying what's missing
    #    if it is, return the valid pick


def main():
    """ Generate a lottery pick and check whether a user has guessed it
        correctly.  """
    word_choices = ["shucksan", "baker", "glacier"]
    number_choices = [1, 2, 3]
    
    print("Welcome, and thanks for playing Lotter.io!")
    print("Today's word choices are:", end=" ")
    print(word_choices)
    print("and the number choices are", end=" ")
    print(number_choices)
    print("The winning pick is a word and a number, in either order.")

    # (TASK 0) - Pseudocode:
    # if the program was run with no command line arguments:
    #     generate a winning pick by calling the random_pick function
    # otherwise:
    #     use the first command-line argument as the winning pick

    
    # Get a guess from the user:
    guess = get_guess()
    
    #check if the guess is valid. If it is not, ask again.
    
    # (TASK 3) - Pseudocode:
    # determine the user's word and number choices by checking
    # whether the first or last character is among number_choices,
    # then split the string into the number part and the word part
    
    # print a message for whichever of the following cases is applicable:
    #   - their pick matches character for character, therefore they win
    #   - the word and number are both correct but the pick doesn't match
    #   - the word is correct but the number is incorrect
    #   - the number is correct but the word is incorrect
    #   - all other cases: neither the word nor the number is correct

        
if __name__ == "__main__":
    main()

