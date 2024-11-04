#Author: Scott Wehrwein and Caroline Hardin
# Date: 5/7/2019, updated 11/3/2024
# Skeleton for Lab 6: A square footage calculator.

#TODO prompt user

    
    #if the user wanted an integer
    
        #prompt them for input until they enter valid input (a digit > 0)
    
        #print("Invalid entry - please enter a positive number")

    # if the user wanted a string
        # prompt them for intput until they enter "s" or "r"
        # before checking, remove any leading or trailing spaces or newlines, and change to lower case
 
        #print("Invalid entry - please enter either s for square or r for rectangle")

#TODO calculate square feet
   
    


def main():
    
    num_rooms = prompt_user("the number of rooms", "integer")
    
    total = 0
    for i in range(1,num_rooms+1):
        total += 0 #TODO fill this in

    print("Total square footage:", total)
    
