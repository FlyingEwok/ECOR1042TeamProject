# Team T-55:
# Nicholas Garth 101227727
# Divya Dushyanthan 101221637
# Dylan Fortier 101221463
# Spencer Green 101196310

from T55_P1_load_data import load_dataset
from T55_P3_sorting import sort_books_title, sort_books_ascending_rate, sort_books_descending_rate, sort_books_publisher, sort_books_category, sort_books_pageCount
from typing import Callable
import time

# Helper Functions
def __invalidCommand() -> None:
    """Written by Nicholas Garth 101227727
    Prints Invalid Command and passes (error handling)"""
    print("Invalid Command")
    pass

def __bookLoadCheck(command: Callable) -> None:
    """Written by Nicholas Garth 101227727
    Performs a check to see if bookDict is loaded, if it is then execute the function
    >>> __bookLoadCheck(sortBookCall)
    Please load the file first
    """
    if 'bookDict' in globals():
        command(bookDict)
    else:
        print("Please load the file first!")
        time.sleep(1)

# User Input Functions
def runProgram() -> None:
    """Written by Nicholas Garth 101227727
    Runs the interaction hub of the program
    >>> runProgram()

    1- Command Line L)oad file
    2- Command Line A)dd book
    3- Command Line R)emove book
    4- Command Line F)ind book by title
    5- Command Line NC) Number of books in a category
    6- Command Line CA) Categories for an author
    7- Command Line CB) Categories for a book title
    8- Command Line G)et book
    9- Command Line S)ort book
    10- Command line Q)uit

    Enter the upper-case letter to the left of the bracket of the option you want:
    """
    while True:
        print("\n1- Command Line L)oad file\n2- Command Line A)dd book\n3- Command Line R)emove book\n4- Command Line F)ind book by title\n5- Command Line NC) Number of books in a category\n6- Command Line CA) Categories for an author\n7- Command Line CB) Categories for a book title\n8- Command Line G)et book\n9- Command Line S)ort book\n10-Command line Q)uit")
        userInput = input("\nEnter the upper-case letter to the left of the bracket of the option you want: ")
        if userInput == 'L':
            global bookDict # make bookDict global so it can be used in any function
            bookDict = load_dataset('Google_Books_Dataset.csv') # REPLACE WHAT THIS VAR = WITH THE LOADFILE FUNCTION!!!!!
        elif userInput == 'A':
            pass # Replace pass with function associated
        elif userInput == 'R':
            pass # Replace pass with function associated
        elif userInput == 'F':
            pass # Replace pass with function associated
        elif userInput == 'NC':
            pass # Replace pass with function associated
        elif userInput == 'CA':
            pass # Replace pass with function associated
        elif userInput == 'CB':
            pass # Replace pass with function associated
        elif userInput == 'G':
            pass # Replace pass with function associated
        elif userInput == 'S':
            __bookLoadCheck(sortBookCall)
        elif userInput == 'Q':
            print("Thank You for using our program\nBye Bye!")
            break
        else:
            __invalidCommand()

# Function 9
def sortBookCall(bookDict: dict) -> None:
    """Written by Nicholas Garth 101227727
    Asks user what sorting command they want to run on their dictionary
    >>> sortBookCall(bookDict)
    T)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn
    Enter the upper-case letter to the left of the bracket of the option you want:
    """
    while True:
        print("\nT)itle   R)ate   P)ublisher  C)ategory   PA)ageCount    RE)turn")
        userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
        if userInput == 'T':
            sort_books_title(bookDict)
        elif userInput == 'R':
            while True: # Ask the user if they want ascending or descending order
                print("\nA)scending   D)escending    RE)turn")
                userInput = input("Enter the upper-case letter to the left of the bracket of the option you want: ")
                if userInput == 'A':
                    sort_books_ascending_rate(bookDict)
                elif userInput == 'D':
                    sort_books_descending_rate(bookDict)
                elif userInput == 'RE':
                    break
                else:
                    __invalidCommand()
        elif userInput == 'P':
            sort_books_publisher(bookDict)
        elif userInput == 'C':
            sort_books_category(bookDict)
        elif userInput == 'PA':
            sort_books_pageCount(bookDict)
        elif userInput == 'RE':
            break
        else:
            __invalidCommand()

# Run the program
runProgram()